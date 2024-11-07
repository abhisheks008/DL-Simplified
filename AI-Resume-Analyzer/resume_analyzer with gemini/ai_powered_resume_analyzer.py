from flask import Flask, jsonify, request
from flask_cors import CORS
import config
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Configure generative AI model
genai.configure(api_key=config.API_KEY)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

app = Flask(__name__)
CORS(app)


# Function to interact with Gemini AI
def gemini_generate_response(prompt):
    chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt]}])
    response = chat_session.send_message(prompt)
    return response.text


# 1. PDF Parsing
def parse_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# 2. Split Text into Chunks
def split_text_into_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=200, length_function=len)
    return text_splitter.split_text(text=text)


# 3. Summarize Resume
def resume_summary(chunks):
    prompt = f'''
    Provide a detailed summarization of the resume below:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# 4. Analyze Strengths
def resume_strength(chunks):
    prompt = f'''
    Analyze the strengths of the resume below and provide detailed insights:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# 5. Analyze Weaknesses
def resume_weakness(chunks):
    prompt = f'''
    Analyze the weaknesses of the resume below and suggest improvements to make it better:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# 6. Job Title Suggestions
def job_title_suggestion(chunks):
    prompt = f'''
    Based on the resume content below, suggest suitable job roles:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# Flask Route to Process Resume
@app.route('/analyze_resume', methods=['POST'])
def analyze_resume():
    if 'fileUploaded' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files["fileUploaded"]

    try:
        # Parse and process resume PDF
        resume_text = parse_pdf(file)
        chunks = split_text_into_chunks(resume_text)

        # Generate responses for different analyses
        summary = resume_summary(chunks)
        strengths = resume_strength(chunks)
        weaknesses = resume_weakness(chunks)
        job_titles = job_title_suggestion(chunks)

        # Prepare JSON response
        response = {
            "summary": summary,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "job_titles": job_titles
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS
import config
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Configure generative AI model
genai.configure(api_key=config.API_KEY)
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

app = Flask(__name__)
CORS(app)


# Function to interact with Gemini AI
def gemini_generate_response(prompt):
    chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt]}])
    response = chat_session.send_message(prompt)
    return response.text


# 1. PDF Parsing
def parse_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# 2. Split Text into Chunks
def split_text_into_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=200, length_function=len)
    return text_splitter.split_text(text=text)


# 3. Summarize Resume
def resume_summary(chunks):
    prompt = f'''
    Provide a detailed summarization of the resume below:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# 4. Analyze Strengths
def resume_strength(chunks):
    prompt = f'''
    Analyze the strengths of the resume below and provide detailed insights:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# 5. Analyze Weaknesses
def resume_weakness(chunks):
    prompt = f'''
    Analyze the weaknesses of the resume below and suggest improvements to make it better:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# 6. Job Title Suggestions
def job_title_suggestion(chunks):
    prompt = f'''
    Based on the resume content below, suggest suitable job roles:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    {chunks}
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    '''
    return gemini_generate_response(prompt)


# Flask Route to Process Resume
@app.route('/analyze_resume', methods=['POST'])
def analyze_resume():
    if 'fileUploaded' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files["fileUploaded"]

    try:
        # Parse and process resume PDF
        resume_text = parse_pdf(file)
        chunks = split_text_into_chunks(resume_text)

        # Generate responses for different analyses
        summary = resume_summary(chunks)
        strengths = resume_strength(chunks)
        weaknesses = resume_weakness(chunks)
        job_titles = job_title_suggestion(chunks)

        # Prepare JSON response
        response = {
            "summary": summary,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "job_titles": job_titles
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
