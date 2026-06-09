# Text Summarizer using Deep Learning

This project implements and compares two primary approaches to Text Summarization: **Abstractive Summarization** (using Deep Learning Transformers) and **Extractive Summarization** (using Statistical Natural Language Processing).

The system evaluation is performed on a standard text sample using 4 distinct models to highlight the differences in semantic understanding, sentence structure, and formulation.

## 🛠️ Models Implemented

### 1. Abstractive Summarization (Hugging Face Transformers)
Abstractive models understand the underlying context of the text and generate novel sentences to formulate the summary, mimicking human-like generation.
* **T5 (Text-to-Text Transfer Transformer):** Evaluated using `t5-small`. Highly efficient for standard structural summaries.
* **BART (Bidirectional and Auto-Regressive Transformers):** Evaluated using `facebook/bart-large-cnn`. Specifically fine-tuned on news architectures, delivering natural, fluid, and coherent summaries.

### 2. Extractive Summarization (`sumy` library)
Extractive models evaluate the existing text and score sentences based on structural algorithms, pulling out the highest-ranked sentences verbatim without altering words.
* **TextRank:** Graph-based ranking algorithm inspired by Google's PageRank, evaluating sentence importance based on word overlaps and connections.
* **LSA (Latent Semantic Analysis):** Algebraic/statistical method that applies Singular Value Decomposition (SVD) to capture hidden semantic patterns across sentences.

---

## 🚀 How to Setup and Run

### Step 1: Install Dependencies
Ensure you have the required Python packages installed in your active environment:
```bash
pip install -r requirements.txt