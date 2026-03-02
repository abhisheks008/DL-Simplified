# YouTube Transcript Summarizer using NLP

## 🎯 Overview
A deep learning project that extracts YouTube video transcripts and generates concise summaries using state-of-the-art NLP transformer models (BART, PEGASUS, T5). Built for [DL-Simplified Issue #940](https://github.com/abhisheks008/DL-Simplified/issues/940).

## 📁 Project Structure
```
Youtube_Transcript_Summarizer/
├── Dataset/
│   └── README.md                          # Dataset info (dynamic YouTube transcripts)
├── Images/
│   ├── model_comparison.png               # Model comparison bar chart
│   ├── rouge_scores.png                   # ROUGE evaluation scores
│   ├── word_reduction.png                 # Word count reduction pie charts
│   └── README.md                          # Visualization info
├── Model/
│   ├── youtube_transcript_summarizer.py   # Core summarizer engine (3 models)
│   ├── app.py                             # Gradio web application
│   └── README.md                          # Detailed documentation (project template)
├── requirements.txt                       # Python dependencies
└── README.md                              # This file
```

## 🚀 Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run CLI summarizer (generates all comparison charts)
cd Model
python youtube_transcript_summarizer.py

# Run web app (Gradio)
cd Model
python app.py
```

## 🤖 Models Used
| Model | Description |
|-------|-------------|
| `facebook/bart-large-cnn` | Detailed, news-style abstractive summaries |
| `google/pegasus-xsum` | Extreme/short single-sentence summaries |
| `t5-small` | Fast and lightweight text-to-text summarization |

## 📊 Features
- **Multi-model summarization** — Compare BART, PEGASUS, and T5 side by side
- **ROUGE evaluation** — Quantitative comparison with ROUGE-1, ROUGE-2, ROUGE-L scores
- **Visualization** — Auto-generated comparison charts and pie charts
- **Gradio web app** — Interactive browser-based interface
- **Text preprocessing** — Filler word removal, noise cleaning, smart chunking

## 📌 Issue Reference
- **Issue:** [DL-Simplified #940 — YouTube Transcript Summarizer using NLP](https://github.com/abhisheks008/DL-Simplified/issues/940)
- **Author:** [Shreya R Hipparagi](https://github.com/ShreyaRHipparagi)
