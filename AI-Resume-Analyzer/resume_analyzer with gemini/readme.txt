
# Resume Analyzer
## Overview

The **Resume Analyzer** is a web application that allows users to upload a resume PDF and get detailed insights, including a summary, strengths, weaknesses, and suggested job titles. The application uses **Google's Gemini Generative AI** for processing and analyzing the content of the resume. The back-end is powered by Flask, and the front-end uses **Streamlit** for a smooth user interface.

## Features

- **Upload Resume PDF**: Allows users to upload a resume file in PDF format.
- **Analyze Resume**: Automatically analyzes the uploaded resume to generate insights on:
  - Resume Summary
  - Resume Strengths
  - Resume Weaknesses
  - Suggested Job Titles
- **Interactive UI**: The user can select between different analysis options (Summary, Strengths, Weaknesses, and Suggested Job Titles) using a radio button.
- **Generative AI Integration**: Utilizes **Gemini Generative AI** for analyzing and generating insights based on the resume content.

## Requirements

Make sure you have the following libraries installed to run this application:

1. Flask
2. Flask-CORS
3. Streamlit
4. PyPDF2
5. Google Generative AI (Gemini)
6. LangChain

You can install all required libraries by running:

```bash
pip install -r requirements.txt
```

## Installation

### 1. Set Up Flask Backend

First, you need to set up the Flask backend that handles the resume analysis and interacts with the Gemini AI.

1. Clone or download the project files.
2. Set up a virtual environment and activate it.
3. Install the dependencies using the command:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your **Google Generative AI API Key** in a `config.py` file. Make sure to include the key:

    ```python
    API_KEY = 'your-api-key-here'
    ```

5. Run the Flask backend server:

    ```bash
    python app.py
    ```

The server should be running at `http://localhost:5000`.

### 2. Set Up Streamlit Frontend

1. After setting up the Flask backend, go to the frontend directory and install the necessary dependencies:

    ```bash
    pip install -r frontend_requirements.txt
    ```

2. To start the Streamlit app, run:

    ```bash
    streamlit run frontend_app.py
    ```

The Streamlit app will start, and you can visit it in your browser (usually `http://localhost:8501`).

## Usage

1. **Upload Resume**: Click the "Choose a Resume PDF file" button to upload your resume in PDF format.
2. **Analyze Resume**: After uploading, click the "Analyze Resume" button. The app will process the resume and generate insights.
3. **View Results**: Once the analysis is complete, you can choose from the available analysis options:
    - Summary
    - Strengths
    - Weaknesses
    - Suggested Job Titles

## Example

- **Summary**: A detailed overview of the resume content.
- **Strengths**: Insights into the strengths based on the content of the resume.
- **Weaknesses**: Suggestions to improve weak areas in the resume.
- **Suggested Job Titles**: Potential job roles based on the resume content.

## Troubleshooting

- If the app is not working as expected, ensure that both the Flask backend and Streamlit frontend are running.
- Make sure the **API Key** for Google Generative AI is set correctly in the `config.py` file.

## Contributing

Feel free to fork the project and submit pull requests for any enhancements or bug fixes. All contributions are welcome!

## License

This project is open-source and available under the MIT License.

---

## Credits

- **Google Generative AI**: For processing and generating responses based on the resume content.
- **Streamlit**: For building the user interface.
- **Flask**: For building the backend API.
- **PyPDF2**: For parsing the PDF resume.
- **LangChain**: For text splitting and chunking.

```

