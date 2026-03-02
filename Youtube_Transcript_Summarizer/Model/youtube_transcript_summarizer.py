"""
YouTube Transcript Summarizer using NLP
========================================
This script extracts transcripts from YouTube videos and generates
concise summaries using multiple transformer-based NLP models.

Models used:
1. facebook/bart-large-cnn (Abstractive Summarization)
2. google/pegasus-xsum (Abstractive Summarization)
3. t5-small (Text-to-Text Transfer Transformer)

Author: Shreya R Hipparagi
Issue: DL-Simplified #940
"""

import re
import os
import time
import warnings
import textwrap
from typing import Optional

import nltk
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for image saving
import matplotlib.pyplot as plt
from transformers import pipeline
from rouge_score import rouge_scorer

warnings.filterwarnings("ignore")

# Download NLTK data
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

# ─────────────────────────────────────────────────
# 1. TRANSCRIPT EXTRACTION
# ─────────────────────────────────────────────────

def extract_video_id(url: str) -> Optional[str]:
    """Extract the video ID from various YouTube URL formats."""
    patterns = [
        r'(?:v=|/v/|youtu\.be/|/embed/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_transcript(video_url: str) -> dict:
    """
    Fetch the transcript of a YouTube video.

    Supports both older and newer versions of youtube-transcript-api.

    Args:
        video_url: YouTube video URL or video ID

    Returns:
        Dictionary with 'text' (full transcript), 'segments' (list of segments),
        and 'word_count' (total word count)
    """
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError(f"Could not extract video ID from: {video_url}")

    try:
        # Try the newer API first (youtube-transcript-api >= 0.6.1)
        from youtube_transcript_api import YouTubeTranscriptApi
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    except TypeError:
        # Fallback for API changes
        try:
            from youtube_transcript_api import YouTubeTranscriptApi
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.get_transcript(video_id)
        except Exception as e:
            raise RuntimeError(
                f"Could not fetch transcript for video '{video_id}'. "
                f"Make sure the video has captions enabled. Error: {e}"
            )
    except Exception as e:
        raise RuntimeError(
            f"Could not fetch transcript for video '{video_id}'. "
            f"Make sure the video has captions enabled. Error: {e}"
        )

    full_text = " ".join([entry["text"] for entry in transcript_list])
    word_count = len(full_text.split())

    return {
        "video_id": video_id,
        "text": full_text,
        "segments": transcript_list,
        "word_count": word_count,
    }


# ─────────────────────────────────────────────────
# 2. TEXT PREPROCESSING
# ─────────────────────────────────────────────────

def preprocess_text(text: str) -> str:
    """Clean and preprocess transcript text."""
    # Remove filler words common in spoken language
    filler_words = [
        r'\bum\b', r'\buh\b', r'\byou know\b', r'\blike\b(?=\s)',
        r'\bso\b(?=\s)', r'\bactually\b', r'\bbasically\b'
    ]
    cleaned = text
    for filler in filler_words:
        cleaned = re.sub(filler, '', cleaned, flags=re.IGNORECASE)

    # Clean up whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    # Remove [Music], [Applause], etc.
    cleaned = re.sub(r'\[.*?\]', '', cleaned)

    return cleaned


def chunk_text(text: str, max_tokens: int = 1024, overlap: int = 100) -> list:
    """
    Split text into overlapping chunks for models with token limits.

    Args:
        text: Input text to chunk
        max_tokens: Maximum tokens per chunk (approximate by words)
        overlap: Number of overlapping words between chunks

    Returns:
        List of text chunks
    """
    words = text.split()
    if len(words) == 0:
        return [text]

    chunks = []
    start = 0

    while start < len(words):
        end = start + max_tokens
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap
        # Avoid infinite loop if overlap >= max_tokens
        if start <= (end - max_tokens):
            start = end

    return chunks


# ─────────────────────────────────────────────────
# 3. SUMMARIZATION MODELS
# ─────────────────────────────────────────────────

class TranscriptSummarizer:
    """
    Multi-model transcript summarizer using Hugging Face Transformers.

    Supports three models:
    - BART (facebook/bart-large-cnn): Best for news-style summarization
    - PEGASUS (google/pegasus-xsum): Best for extreme/short summaries
    - T5 (t5-small): Lightweight, versatile text-to-text model
    """

    MODELS = {
        "bart": {
            "name": "facebook/bart-large-cnn",
            "description": "BART - Best for detailed, news-style summaries",
            "max_input": 1024,
        },
        "pegasus": {
            "name": "google/pegasus-xsum",
            "description": "PEGASUS - Best for extreme/short summaries",
            "max_input": 512,
        },
        "t5": {
            "name": "t5-small",
            "description": "T5 - Lightweight, versatile summarization",
            "max_input": 512,
        },
    }

    def __init__(self):
        self._pipelines = {}

    def _get_pipeline(self, model_key: str):
        """Lazy-load a summarization pipeline."""
        if model_key not in self._pipelines:
            model_info = self.MODELS[model_key]
            print(f"  Loading model: {model_info['name']}...")
            start = time.time()

            if model_key == "t5":
                # T5 requires a prefix for summarization
                self._pipelines[model_key] = pipeline(
                    "summarization",
                    model=model_info["name"],
                    tokenizer=model_info["name"],
                )
            else:
                self._pipelines[model_key] = pipeline(
                    "summarization",
                    model=model_info["name"],
                )

            elapsed = time.time() - start
            print(f"  ✓ Model loaded in {elapsed:.1f}s")

        return self._pipelines[model_key]

    def summarize(
        self,
        text: str,
        model_key: str = "bart",
        max_length: int = 150,
        min_length: int = 40,
    ) -> dict:
        """
        Summarize text using the specified model.

        Args:
            text: Input text to summarize
            model_key: Model to use ('bart', 'pegasus', 't5')
            max_length: Maximum summary length (in tokens)
            min_length: Minimum summary length (in tokens)

        Returns:
            Dictionary with summary text, model info, and timing
        """
        if model_key not in self.MODELS:
            raise ValueError(
                f"Unknown model: {model_key}. Choose from {list(self.MODELS.keys())}"
            )

        model_info = self.MODELS[model_key]
        pipe = self._get_pipeline(model_key)

        # Chunk text if it exceeds model's max input
        chunks = chunk_text(text, max_tokens=model_info["max_input"])

        print(
            f"  Summarizing {len(chunks)} chunk(s) with {model_info['name']}..."
        )

        start_time = time.time()
        summaries = []

        for i, chunk in enumerate(chunks):
            if model_key == "t5":
                chunk = "summarize: " + chunk

            try:
                result = pipe(
                    chunk,
                    max_length=max_length,
                    min_length=min(min_length, max_length - 10),
                    do_sample=False,
                    truncation=True,
                )
                summaries.append(result[0]["summary_text"])
            except Exception as e:
                print(f"  ⚠ Warning: Error on chunk {i+1}: {e}")
                continue

        elapsed = time.time() - start_time
        final_summary = " ".join(summaries)

        original_length = len(text.split())
        summary_length = len(final_summary.split())

        return {
            "model": model_info["name"],
            "model_key": model_key,
            "summary": final_summary,
            "original_length": original_length,
            "summary_length": summary_length,
            "compression_ratio": round(
                (1 - summary_length / max(original_length, 1)) * 100, 1
            ),
            "time_seconds": round(elapsed, 2),
            "num_chunks": len(chunks),
        }

    def compare_models(
        self, text: str, max_length: int = 150, min_length: int = 40
    ) -> pd.DataFrame:
        """
        Run all models on the same text and return a comparison DataFrame.
        """
        results = []
        for model_key in self.MODELS:
            print(f"\n{'='*50}")
            print(f"Model: {self.MODELS[model_key]['description']}")
            print(f"{'='*50}")
            try:
                result = self.summarize(text, model_key, max_length, min_length)
                results.append(result)
                print(
                    f"  ✓ Summary ({result['summary_length']} words, "
                    f"{result['compression_ratio']}% compression)"
                )
            except Exception as e:
                print(f"  ✗ Error: {e}")

        df = pd.DataFrame(results)
        return df


# ─────────────────────────────────────────────────
# 4. EVALUATION (ROUGE SCORES)
# ─────────────────────────────────────────────────

def evaluate_summaries(reference: str, summaries: dict) -> pd.DataFrame:
    """
    Evaluate summaries against a reference using ROUGE metrics.

    Args:
        reference: Reference/gold summary
        summaries: Dict of {model_name: summary_text}

    Returns:
        DataFrame with ROUGE-1, ROUGE-2, ROUGE-L scores
    """
    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"], use_stemmer=True
    )

    results = []
    for model_name, summary in summaries.items():
        scores = scorer.score(reference, summary)
        results.append({
            "Model": model_name,
            "ROUGE-1 (F1)": round(scores["rouge1"].fmeasure, 4),
            "ROUGE-2 (F1)": round(scores["rouge2"].fmeasure, 4),
            "ROUGE-L (F1)": round(scores["rougeL"].fmeasure, 4),
        })

    return pd.DataFrame(results)


# ─────────────────────────────────────────────────
# 5. VISUALIZATION
# ─────────────────────────────────────────────────

def plot_model_comparison(df: pd.DataFrame, save_path: str = None):
    """Generate bar chart comparing model performance metrics."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    metrics = [
        ("compression_ratio", "Compression Ratio (%)", "#4ECDC4"),
        ("summary_length", "Summary Length (words)", "#FF6B6B"),
        ("time_seconds", "Processing Time (seconds)", "#45B7D1"),
    ]

    for ax, (col, title, color) in zip(axes, metrics):
        bars = ax.bar(
            df["model_key"], df[col], color=color, alpha=0.85, edgecolor="white"
        )
        ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
        ax.set_ylabel(title.split("(")[0].strip(), fontsize=10)
        ax.tick_params(axis="x", rotation=15)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.5,
                f"{height:.1f}",
                ha="center",
                va="bottom",
                fontsize=10,
            )

    fig.suptitle(
        "Model Comparison — YouTube Transcript Summarizer",
        fontsize=15,
        fontweight="bold",
        y=1.02,
    )
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  ✓ Chart saved to {save_path}")

    plt.close(fig)


def plot_rouge_scores(rouge_df: pd.DataFrame, save_path: str = None):
    """Generate grouped bar chart for ROUGE scores."""
    fig, ax = plt.subplots(figsize=(10, 6))

    x = range(len(rouge_df))
    width = 0.25
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1"]

    for i, col in enumerate(["ROUGE-1 (F1)", "ROUGE-2 (F1)", "ROUGE-L (F1)"]):
        offset = (i - 1) * width
        bars = ax.bar(
            [xi + offset for xi in x],
            rouge_df[col],
            width,
            label=col,
            color=colors[i],
            alpha=0.85,
            edgecolor="white",
        )
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.005,
                f"{height:.3f}",
                ha="center",
                va="bottom",
                fontsize=9,
            )

    ax.set_xlabel("Model", fontsize=12)
    ax.set_ylabel("Score", fontsize=12)
    ax.set_title("ROUGE Evaluation Scores", fontsize=14, fontweight="bold")
    ax.set_xticks(list(x))
    ax.set_xticklabels(rouge_df["Model"])
    ax.legend(loc="upper right")
    ax.set_ylim(0, 1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  ✓ Chart saved to {save_path}")

    plt.close(fig)


def plot_word_count_reduction(
    original: int, summaries: dict, save_path: str = None
):
    """Pie chart showing word count reduction for each model."""
    fig, axes = plt.subplots(1, len(summaries), figsize=(5 * len(summaries), 5))
    if len(summaries) == 1:
        axes = [axes]

    colors_pair = [
        ("#FF6B6B", "#FFE5E5"),
        ("#4ECDC4", "#E5FFF9"),
        ("#45B7D1", "#E5F5FF"),
    ]

    for ax, ((name, summary), (c1, c2)) in zip(
        axes, zip(summaries.items(), colors_pair)
    ):
        summary_words = len(summary.split())
        removed = original - summary_words
        sizes = [summary_words, max(removed, 0)]
        labels = [
            f"Summary\n({summary_words} words)",
            f"Removed\n({max(removed, 0)} words)",
        ]

        ax.pie(
            sizes,
            labels=labels,
            colors=[c1, c2],
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 10},
        )
        ax.set_title(name, fontsize=12, fontweight="bold")

    fig.suptitle(
        f"Word Count Reduction (Original: {original} words)",
        fontsize=14,
        fontweight="bold",
        y=1.02,
    )
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  ✓ Chart saved to {save_path}")

    plt.close(fig)


# ─────────────────────────────────────────────────
# 6. MAIN EXECUTION
# ─────────────────────────────────────────────────

def summarize_video(
    video_url: str,
    model_key: str = "bart",
    max_length: int = 150,
    min_length: int = 40,
) -> dict:
    """
    End-to-end: extract transcript from YouTube and summarize it.

    Args:
        video_url: YouTube video URL
        model_key: Which model to use ('bart', 'pegasus', 't5')
        max_length: Max summary length
        min_length: Min summary length

    Returns:
        Dictionary with transcript, summary, and metadata
    """
    print("=" * 60)
    print("  YouTube Transcript Summarizer")
    print("=" * 60)

    # Step 1: Extract transcript
    print("\n📥 Step 1: Extracting transcript...")
    transcript_data = get_transcript(video_url)
    print(f"  ✓ Transcript extracted: {transcript_data['word_count']} words")

    # Step 2: Preprocess
    print("\n🧹 Step 2: Preprocessing text...")
    cleaned_text = preprocess_text(transcript_data["text"])
    print(f"  ✓ Cleaned text: {len(cleaned_text.split())} words")

    # Step 3: Summarize
    print(f"\n🤖 Step 3: Generating summary with {model_key.upper()}...")
    summarizer = TranscriptSummarizer()
    result = summarizer.summarize(cleaned_text, model_key, max_length, min_length)

    # Step 4: Display results
    print(f"\n{'─' * 60}")
    print("📊 RESULTS")
    print(f"{'─' * 60}")
    print(f"  Model:             {result['model']}")
    print(f"  Original Words:    {result['original_length']}")
    print(f"  Summary Words:     {result['summary_length']}")
    print(f"  Compression:       {result['compression_ratio']}%")
    print(f"  Time:              {result['time_seconds']}s")
    print(f"\n📝 SUMMARY:")
    print(f"  {textwrap.fill(result['summary'], width=70)}")
    print(f"{'─' * 60}")

    return {
        "transcript": transcript_data,
        "cleaned_text": cleaned_text,
        "result": result,
    }


if __name__ == "__main__":
    # Demo with a sample video
    DEMO_URL = "https://www.youtube.com/watch?v=arj7oStGLkU"  # TED Talk

    print("\n🎬 Demo: Summarizing a TED Talk\n")

    # Single model summary
    output = summarize_video(DEMO_URL, model_key="bart")

    # Multi-model comparison
    print("\n\n🔄 Running multi-model comparison...")
    summarizer = TranscriptSummarizer()
    cleaned = output["cleaned_text"]
    comparison_df = summarizer.compare_models(cleaned)
    print("\n📊 Comparison Table:")
    print(comparison_df.to_string(index=False))

    # Save visualizations
    images_dir = os.path.join(os.path.dirname(__file__), "..", "Images")
    plot_model_comparison(
        comparison_df,
        save_path=os.path.join(images_dir, "model_comparison.png"),
    )

    # ROUGE evaluation (using BART summary as reference)
    if len(comparison_df) >= 2:
        reference_summary = comparison_df.iloc[0]["summary"]
        model_summaries = {
            row["model"]: row["summary"]
            for _, row in comparison_df.iterrows()
        }
        rouge_df = evaluate_summaries(reference_summary, model_summaries)
        print("\n📊 ROUGE Scores:")
        print(rouge_df.to_string(index=False))
        plot_rouge_scores(
            rouge_df,
            save_path=os.path.join(images_dir, "rouge_scores.png"),
        )

        # Word count reduction chart
        plot_word_count_reduction(
            original=len(cleaned.split()),
            summaries=model_summaries,
            save_path=os.path.join(images_dir, "word_reduction.png"),
        )

    print("\n✅ All visualizations saved to Images/ folder!")
