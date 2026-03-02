"""
YouTube Transcript Summarizer — Gradio Web Application
=======================================================
A user-friendly web interface for summarizing YouTube video transcripts
using transformer-based NLP models.

Author: Shreya R Hipparagi
Issue: DL-Simplified #940
"""

import gradio as gr
from youtube_transcript_summarizer import (
    get_transcript,
    preprocess_text,
    TranscriptSummarizer,
    evaluate_summaries,
)

# Initialize the summarizer
summarizer = TranscriptSummarizer()


def summarize_youtube(url: str, model_choice: str, max_len: int, min_len: int):
    """Process a YouTube URL and return the summary."""
    if not url or not url.strip():
        return "❌ Please enter a YouTube URL.", "", ""

    try:
        # Step 1: Get transcript
        transcript_data = get_transcript(url.strip())
        raw_text = transcript_data["text"]
        word_count = transcript_data["word_count"]

        # Step 2: Preprocess
        cleaned_text = preprocess_text(raw_text)

        # Step 3: Summarize
        model_key = model_choice.lower().split(" ")[0]  # "bart", "pegasus", "t5"
        result = summarizer.summarize(
            cleaned_text,
            model_key=model_key,
            max_length=int(max_len),
            min_length=int(min_len),
        )

        # Format output
        stats = (
            f"📊 **Statistics**\n\n"
            f"| Metric | Value |\n"
            f"|--------|-------|\n"
            f"| Model | {result['model']} |\n"
            f"| Original Words | {result['original_length']} |\n"
            f"| Summary Words | {result['summary_length']} |\n"
            f"| Compression | {result['compression_ratio']}% |\n"
            f"| Processing Time | {result['time_seconds']}s |\n"
            f"| Chunks Processed | {result['num_chunks']} |\n"
        )

        transcript_preview = (
            cleaned_text[:1000] + "..."
            if len(cleaned_text) > 1000
            else cleaned_text
        )
        return result["summary"], stats, transcript_preview

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        return error_msg, "", ""


def compare_all_models(url: str, max_len: int, min_len: int):
    """Run all 3 models and return comparison."""
    if not url or not url.strip():
        return "❌ Please enter a YouTube URL."

    try:
        transcript_data = get_transcript(url.strip())
        cleaned_text = preprocess_text(transcript_data["text"])

        summaries_text = ""
        all_summaries = {}

        for model_key in ["bart", "pegasus", "t5"]:
            try:
                result = summarizer.summarize(
                    cleaned_text, model_key, int(max_len), int(min_len)
                )
                all_summaries[result["model"]] = result["summary"]
                summaries_text += (
                    f"\n### {result['model']}\n"
                    f"**Words:** {result['summary_length']} | "
                    f"**Compression:** {result['compression_ratio']}% | "
                    f"**Time:** {result['time_seconds']}s\n\n"
                    f"> {result['summary']}\n\n---\n"
                )
            except Exception as e:
                summaries_text += f"\n### {model_key}\n❌ Error: {e}\n\n---\n"

        # Add ROUGE cross-evaluation if we have at least 2 summaries
        if len(all_summaries) >= 2:
            first_model = list(all_summaries.keys())[0]
            reference = all_summaries[first_model]
            rouge_df = evaluate_summaries(reference, all_summaries)
            summaries_text += (
                f"\n### 📊 ROUGE Scores (Reference: {first_model})\n\n"
            )
            summaries_text += rouge_df.to_markdown(index=False)
            summaries_text += "\n"

        return summaries_text

    except Exception as e:
        return f"❌ Error: {str(e)}"


# ─────────────────────────────────────────────────
# GRADIO UI
# ─────────────────────────────────────────────────

with gr.Blocks(
    title="YouTube Transcript Summarizer",
    theme=gr.themes.Soft(
        primary_hue="teal",
        secondary_hue="blue",
    ),
) as app:

    gr.Markdown(
        """
        # 🎬 YouTube Transcript Summarizer
        ### Powered by NLP Transformer Models (BART, PEGASUS, T5)

        Extract and summarize YouTube video transcripts instantly using
        state-of-the-art deep learning models.

        ---
        """
    )

    with gr.Row():
        with gr.Column(scale=2):
            url_input = gr.Textbox(
                label="🔗 YouTube Video URL",
                placeholder="https://www.youtube.com/watch?v=...",
                info="Paste any YouTube URL with captions/subtitles",
            )

            with gr.Row():
                model_dropdown = gr.Dropdown(
                    choices=[
                        "bart — Best for detailed summaries",
                        "pegasus — Best for short summaries",
                        "t5 — Lightweight & fast",
                    ],
                    value="bart — Best for detailed summaries",
                    label="🤖 Model",
                )

            with gr.Row():
                max_len = gr.Slider(
                    50, 500, value=150, step=10, label="Max Summary Length"
                )
                min_len = gr.Slider(
                    20, 200, value=40, step=10, label="Min Summary Length"
                )

            with gr.Row():
                summarize_btn = gr.Button(
                    "📝 Summarize", variant="primary", size="lg"
                )
                compare_btn = gr.Button(
                    "🔄 Compare All Models", variant="secondary", size="lg"
                )

        with gr.Column(scale=3):
            summary_output = gr.Textbox(
                label="📝 Summary",
                lines=8,
                show_copy_button=True,
            )
            stats_output = gr.Markdown(label="📊 Statistics")

    with gr.Accordion("📄 Transcript Preview", open=False):
        transcript_preview = gr.Textbox(
            label="Cleaned Transcript (first 1000 chars)", lines=6
        )

    with gr.Accordion("🔄 Multi-Model Comparison Results", open=False):
        comparison_output = gr.Markdown()

    # Event handlers
    summarize_btn.click(
        fn=summarize_youtube,
        inputs=[url_input, model_dropdown, max_len, min_len],
        outputs=[summary_output, stats_output, transcript_preview],
    )

    compare_btn.click(
        fn=compare_all_models,
        inputs=[url_input, max_len, min_len],
        outputs=[comparison_output],
    )

    gr.Markdown(
        """
        ---
        ### 📌 Notes
        - **BART** (`facebook/bart-large-cnn`): Produces detailed, coherent summaries (recommended)
        - **PEGASUS** (`google/pegasus-xsum`): Generates very short, punchy summaries
        - **T5** (`t5-small`): Lightweight model, good for quick results
        - Videos must have captions/subtitles enabled
        - First run will download model weights (~1-2 GB per model)

        Built for [DL-Simplified #940](https://github.com/abhisheks008/DL-Simplified/issues/940)
        | Author: **Shreya R Hipparagi**
        """
    )


if __name__ == "__main__":
    app.launch(share=False)
