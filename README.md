# dlassignment2
**Title: Transliteration with an LSTM-Based Sequence-to-Sequence Encoder-Decoder**

**Objective:**
Implement a character-level sequence-to-sequence model using LSTM units to convert words written in Latin script into their Devanagari counterparts. The design must allow easy adjustment of embedding dimensions, hidden state size, number of layers, and choice of recurrent cell.

**Architecture Details:**
- **Encoder:** One or more LSTM layers with an embedding layer for inputs.
- **Decoder:** LSTM layer(s) feeding into a Dense layer with a softmax activation to predict the next character.
- **Configuration Options:** Adjustable embedding dimension, hidden layer size, and stack depth of LSTM layers.

**Dataset:**
- Extracted from the Hindi portion of the Dakshina transliteration corpus.
- Contains parallel pairs of Latin-script words and corresponding Devanagari-script words.
- Preprocessed to generate aligned character sequences for both input and target.

**Hyperparameter Settings:**
- Embedding dimension: 256
- LSTM hidden size: 256
- Number of stacked LSTM layers: 1
- Batch size: 64
- Optimizer: Adam
- Loss: Sparse categorical cross-entropy
- Training epochs: 30

**Training Workflow:**
1. Split the data into training, validation, and test sets.
2. Convert Latin input and Devanagari target characters into one-hot or index-encoded sequences.
3. Train using teacher forcing, supplying the correct previous character to the decoder at each time step.

**Evaluation Strategy:**
- Generate transliterations character by character on test samples.
- Compute accuracy by comparing predicted sequences against ground-truth targets.
- Report performance metrics on the held-out test partition.

**Computational Complexity & Parameter Count:**
- **Operations per timestep:**\
  \(T \times [4(m + k)k + 8k^2 + kV]\)
- **Total parameters:**\
  \(4(m + k + 1)k + 4(2k + 1)k + (kV + V)\)
  where \(m\) = vocab size, \(k\) = hidden units, and \(V\) = output vocab size.

**Example Outputs:**
| Input  | Ground Truth | Model Prediction |
|--------|--------------|------------------|
| ankit  | अंकित       | अंकित            |
| delhi  | दिल्ली       | दिल्ली            |

**Checklist:**
- Model parameters (embedding, hidden size, layer count) are configurable.
- Encoder and decoder implemented with LSTM cells.
- Training run for 30 epochs with proper teacher forcing.
- Evaluation performed on unseen test data with accuracy calculation.
- Complexity formulas and parameter derivations documented.
- Sample transliterations verified and reported.

**Conclusion:**
The system successfully transliterates Latin-script inputs to Devanagari characters using a straightforward LSTM-based encoder-decoder. The model demonstrates strong generalization to unseen Hindi words with a simple yet effective Seq2Seq architecture.

