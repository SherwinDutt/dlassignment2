# -*- coding: utf-8 -*-
"""DlAssignment2*189_2Ques.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10AazA3i0smQpb0XFel7bioSLSCQHMON3
"""

# Install required libraries
!pip install transformers datasets openpyxl

import os
import pandas as pd
import torch
from datasets import Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling, pipeline

# Disable wandb
os.environ["WANDB_DISABLED"] = "true"

# Step 1: Load Excel file
file_path = "TheWeekndLyrics.xlsx"
df = pd.read_excel(file_path)
print(" Excel file loaded.")

# Step 2: Show DataFrame and columns
print("\n Column names:", df.columns.tolist())
print("\n Preview:\n", df.head())

# Step 3: Ensure we have a lyrics column
possible_lyrics_cols = [col for col in df.columns if "lyric" in col.lower()]
if not possible_lyrics_cols:
    # fallback: longest average string length
    text_cols = df.select_dtypes(include=["object"])
    avg_lengths = text_cols.apply(lambda col: col.dropna().astype(str).str.len().mean())
    lyrics_col = avg_lengths.idxmax()
    print(f" No column explicitly named 'lyrics'. Auto-selected based on content: {lyrics_col}")
else:
    lyrics_col = possible_lyrics_cols[0]
    print(f" Detected lyrics column: {lyrics_col}")

# Step 4: Filter out null or empty rows
df = df.dropna(subset=[lyrics_col])
df = df[df[lyrics_col].astype(str).str.strip() != ""]
print(f" Remaining lyrics entries: {len(df)}")

# Step 5: Convert to HuggingFace Dataset
lyrics_list = df[lyrics_col].astype(str).tolist()
dataset = Dataset.from_dict({"text": lyrics_list})

# Step 6: Load GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Step 7: Tokenize data
def tokenize_function(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

tokenized_dataset = dataset.map(tokenize_function, batched=True)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Step 8: Training arguments
training_args = TrainingArguments(
    output_dir="./gpt2-weeknd",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=200,
    save_total_limit=1,
    logging_steps=50,
    prediction_loss_only=True,
    fp16=torch.cuda.is_available()
)

# Step 9: Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Step 10: Train
trainer.train()

# Step 11: Save model
trainer.save_model("./gpt2-weeknd")
tokenizer.save_pretrained("./gpt2-weeknd")

# Step 12: Generate sample lyrics
generator = pipeline('text-generation', model="./gpt2-weeknd", tokenizer=tokenizer)

prompts = [
    "I saw you dancing in a crowded room",
    "I've been tryna call",
    "She told me not to worry",
    "I ran out of tears when I was eighteen",
    "You don't even have to do too much"
]

for prompt in prompts:
    print(f"\n🎤 Prompt: {prompt}")
    output = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    print("🎶", output)