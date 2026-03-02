# Dataset

## YouTube Transcript Summarizer — Dataset Information

This project **does not use a static dataset**. Instead, it dynamically extracts transcripts from YouTube videos in real-time using the [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) Python library.

### How it works:
1. The user provides a **YouTube video URL** (e.g., `https://www.youtube.com/watch?v=VIDEO_ID`)
2. The application extracts the **video ID** from the URL
3. Using `youtube-transcript-api`, the full transcript (auto-generated or manually added captions) is fetched
4. The transcript text is then passed to NLP summarization models

### Data Format:
The transcript API returns data in the following JSON structure:
```json
[
    {
        "text": "hello and welcome to this video",
        "start": 0.0,
        "duration": 3.5
    },
    {
        "text": "today we will discuss deep learning",
        "start": 3.5,
        "duration": 4.2
    }
]
```

### Limitations:
- Videos without captions/subtitles cannot be summarized
- Some auto-generated captions may contain inaccuracies
- Age-restricted or private videos are not accessible

### Sample Videos Used for Testing:
| Video | Topic | Duration | Transcript Length |
|-------|-------|----------|-------------------|
| [TED Talk - Inside the Mind of a Master Procrastinator](https://www.youtube.com/watch?v=arj7oStGLkU) | Psychology | ~14 min | ~2000 words |
| [3Blue1Brown - Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk) | Deep Learning | ~19 min | ~3500 words |
| [Fireship - 100 Seconds of Code](https://www.youtube.com/watch?v=dc-2t26Vuhs) | Programming | ~2 min | ~300 words |
