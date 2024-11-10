
import streamlit as st
import spacy
from sentence_transformers import SentenceTransformer

# @st.cache_resource
def load_nlp_model():
    return spacy.load("en_core_web_sm")

# @st.cache_resource
def load_transformer_model():
    return SentenceTransformer('all-MiniLM-L6-v2')
