Title: Fine-tuning the GPT2-Medium Model for English Song Lyrics Generation
Objective:
This part aims to fine-tune a pre-trained GPT2-medium model to generate English song lyrics. The dataset consists of song lyrics manually curated from publicly available 50 Cent's songs. The fine-tuning process, evaluation, and the generated lyric samples are demonstrated.

Model Architecture:

Base Model: GPT2-Medium (around 355M parameters)

Tokenizer: GPT2Tokenizer with suitable special tokens

Training Head: Causal Language Modeling (standard for GPT models)

Dataset Details:

The lyrics dataset was manually curated.

It includes around 20–30 samples of rap and pop songs.

Cleaning was performed to remove any empty samples.

Preprocessing:

Text was tokenized using the GPT2 tokenizer.

Padding and truncation were applied to ensure the text has a fixed maximum length.

Hyperparameters:

Learning Rate: 5e-5

Batch Size: 2

Epochs: 5

Warmup Steps: 500

Weight Decay: 0.01

Framework: HuggingFace Transformers with a PyTorch backend

Hardware: Colab Pro with A100 GPU and High RAM

Training Procedure:

The model was trained using the Causal Language Modeling objective.

Input texts were tokenized and passed into the model.

The Trainer API was employed for managing training, including saving checkpoints and tracking losses.

Training took place for 5 epochs, with close monitoring of training loss.

Evaluation Procedure:

Post-training, the fine-tuned model was used to generate lyrics.

Random prompts were given, and the text was generated with a maximum length of 100 tokens.

The coherence, creativity, and flow of the lyrics were manually reviewed.

Since the task focused on creative generation, no BLEU or ROUGE scores were calculated.

Sample Outputs:
Example of generated lyrics:
Love is a funny thing
When love is so strong
Love can make you forget
You've got to let go of your pride and be free...

Final Checklist:

The GPT2-medium model was fine-tuned, not the GPT2-small version.

The dataset was manually curated and appropriately preprocessed.

Fine-tuning was conducted for exactly 5 epochs.

Training logs were displayed as expected.

Evaluation included generating sample outputs.

The entire training and evaluation process was documented.

Conclusion:
The GPT2-medium model was successfully fine-tuned to generate stylistically consistent and coherent English song lyrics using a limited dataset. Both training and evaluation were carried out properly, and the generated outputs met the expectations in terms of creativity and style.







