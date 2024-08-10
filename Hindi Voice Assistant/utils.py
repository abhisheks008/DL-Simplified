from groq import Groq
import streamlit as st
import base64
import os
from dotenv import load_dotenv, dotenv_values
from gtts import gTTS
import tempfile

load_dotenv()

client = Groq(api_key=os.getenv("API_key"),)

def speech_to_text(audio):
  with open(audio, 'rb') as audio_file:
    transcription = client.audio.transcriptions.create(
        file= audio_file,
        model = "whisper-large-v3",
        language='hi',
        response_format='text'
    )
    return transcription

def get_answer(message):
  system_message = [
    {
    "role" : "system",
    "content": """You are a helpfull AI chatbot, that answers questions, in Hindi language, asked by User.
    1. You must Avoid discussing sensitive, offensive, or harmful content. Refrain from engaging in any form of discrimination, harassment, or inappropriate behavior.
    3. If the user expresses gratitude or indicates the end of the conversation, respond with a polite farewell.
    """
    }
  ]
  messages = system_message + message

  response = client.chat.completions.create(
           model='llama3-8b-8192',
           messages = messages
    )
  return response.choices[0].message.content


def text_to_speech(input_text):
    tts = gTTS(input_text, lang='hi')
    webm_file_path = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
    tts.save(webm_file_path)
    return webm_file_path

def autoplay_audio(file_path):
    with open(file_path, 'rb') as f:
      data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    md = f"""
    <audio autoplay>
    <source src='data:audio/mp3;base64,{b64}' type='audio/mp3'>
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)
