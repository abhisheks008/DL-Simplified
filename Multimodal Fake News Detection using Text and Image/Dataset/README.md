# Dataset — Multimodal Fake News Detection using Text and Image

## Dataset Used: FakeNewsNet

FakeNewsNet is a comprehensive fake news dataset containing news content and social context data, ideal for multimodal fake news detection using both text and images.

## Dataset Link

https://github.com/KaiDMML/FakeNewsNet

## Minimalistic Version (CSV files — available directly in the repo)

The repo provides ready-to-use CSV files:

| File | Description |
|------|-------------|
| `politifact_fake.csv` | Fake news samples from PolitiFact |
| `politifact_real.csv` | Real news samples from PolitiFact |
| `gossipcop_fake.csv` | Fake news samples from GossipCop |
| `gossipcop_real.csv` | Real news samples from GossipCop |

Each CSV contains: `id`, `url`, `title`, `tweet_ids`

## Full Dataset Structure

Each news article folder contains:
- `news content.json` — article text, images list, publish date
- `tweets/` — tweet objects sharing the news
- `retweets/` — retweet objects

## How to Download

git clone https://github.com/KaiDMML/FakeNewsNet.git
cd FakeNewsNet
pip install -r requirements.txt
python main.py


## Why This Dataset

- Contains both text and images for every news article
- Two subsets — PolitiFact (political news) and GossipCop (entertainment news)
- Ground truth labels verified by professional fact-checkers
- Widely used benchmark in multimodal fake news detection research