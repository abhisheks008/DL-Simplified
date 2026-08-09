import json
import os
from glob import glob

import streamlit as st
import torch
from torch import nn

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "Dataset")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "ner_model.pt")

st.set_page_config(page_title="NER Demo", layout="centered")

st.title("Named Entity Recognition Demo")
st.caption("BiLSTM tagger trained on OntoNotes 5 (simple whitespace tokenization).")

HUMAN_LABELS = {
    "PERSON": "Person",
    "ORG": "Organization",
    "GPE": "Geo-Political Entity",
    "NORP": "Nationality/Religious/Political Group",
    "FAC": "Facility",
    "LOC": "Location",
    "PRODUCT": "Product",
    "EVENT": "Event",
    "WORK_OF_ART": "Work of Art",
    "LAW": "Law",
    "LANGUAGE": "Language",
    "DATE": "Date",
    "TIME": "Time",
    "MONEY": "Money",
    "PERCENT": "Percent",
    "QUANTITY": "Quantity",
    "ORDINAL": "Ordinal",
    "CARDINAL": "Cardinal",
}

def format_label(label):
    if label == "O":
        return "O"
    if "-" not in label:
        return label
    bio, ent_type = label.split("-", 1)
    human = HUMAN_LABELS.get(ent_type, ent_type)
    return f"{human} ({bio})"

@st.cache_resource
def load_label_map():
    label_path = os.path.join(DATASET_DIR, "label.json")
    with open(label_path, "r", encoding="utf-8") as f:
        label_to_id = json.load(f)
    id_to_label = {v: k for k, v in label_to_id.items()}
    return id_to_label

@st.cache_resource
def build_vocab():
    token_counter = {}
    train_files = sorted(glob(os.path.join(DATASET_DIR, "train*.json")))
    for path in train_files:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                item = json.loads(line)
                for token in item["tokens"]:
                    token_counter[token] = token_counter.get(token, 0) + 1

    pad_token = "<PAD>"
    unk_token = "<UNK>"
    vocab = [pad_token, unk_token] + sorted(
        token_counter.keys(), key=lambda t: token_counter[t], reverse=True
    )
    token_to_id = {t: i for i, t in enumerate(vocab)}
    return token_to_id

class BiLSTMTagger(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_labels, pad_id):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_id)
        self.lstm = nn.LSTM(
            embed_dim,
            hidden_dim,
            num_layers=1,
            batch_first=True,
            bidirectional=True,
        )
        self.dropout = nn.Dropout(0.2)
        self.classifier = nn.Linear(hidden_dim * 2, num_labels)

    def forward(self, input_ids):
        x = self.embedding(input_ids)
        x, _ = self.lstm(x)
        x = self.dropout(x)
        logits = self.classifier(x)
        return logits

@st.cache_resource
def load_model(token_to_id, id_to_label):
    pad_id = token_to_id["<PAD>"]
    model = BiLSTMTagger(
        vocab_size=len(token_to_id),
        embed_dim=128,
        hidden_dim=256,
        num_labels=len(id_to_label),
        pad_id=pad_id,
    )
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    return model

id_to_label = load_label_map()
token_to_id = build_vocab()
model = load_model(token_to_id, id_to_label)

text = st.text_area("Enter text", "Barack Obama visited New York in 2012.")

if st.button("Tag Entities"):
    tokens = text.strip().split()
    if not tokens:
        st.warning("Please enter some text.")
    else:
        unk_id = token_to_id.get("<UNK>")
        input_ids = torch.tensor([[token_to_id.get(t, unk_id) for t in tokens]])
        with torch.no_grad():
            logits = model(input_ids)
            pred_ids = logits.argmax(-1).squeeze(0).tolist()
        pred_labels = [format_label(id_to_label.get(i, "O")) for i in pred_ids]

        st.subheader("Predictions")
        st.dataframe({"token": tokens, "label": pred_labels}, use_container_width=True)

st.sidebar.markdown("**Model weights**")
st.sidebar.code(MODEL_PATH)
