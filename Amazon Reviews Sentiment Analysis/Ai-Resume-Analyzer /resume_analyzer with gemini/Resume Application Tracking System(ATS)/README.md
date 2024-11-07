

# ATS Resume Expert

ATS Resume Expert is a Streamlit-based web application that uses Google's Generative AI (Gemini) model to analyze resumes in PDF format against specific job descriptions. The application evaluates the resume content, providing insights and match percentages to help users understand how well their resume aligns with job requirements.

## Features
- **Resume Analysis**: Upload a PDF resume, and the AI evaluates it based on a provided job description.
- **Job Match Scoring**: The AI provides a match percentage between the resume and job description, highlighting strengths, weaknesses, missing keywords, and more.
- **Streamlit UI**: User-friendly interface with text input for job description and resume upload capability.

## Getting Started

### Prerequisites
1. **Python**: Make sure you have Python 3.7+ installed.
2. **Google API Key**: This project requires access to Google Generative AI's Gemini model. Obtain an API key and configure it in the environment.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ATS-Resume-Expert.git
   cd ATS-Resume-Expert
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   Here is a sample `requirements.txt`:
   ```
   streamlit
   dotenv
   pdf2image
   pillow
   google-generativeai
   ```

3. Install **poppler** (required for `pdf2image`):
   - **Windows**: [Download Poppler for Windows](http://blog.alivate.com.au/poppler-windows/), extract, and add `poppler/bin` to your PATH.
   - **Linux**: Run `sudo apt install poppler-utils`.
   - **macOS**: Run `brew install poppler`.

4. Create a `.env` file in the project root with your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

### Running the App
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the provided local URL to access the ATS Resume Expert app.

## Usage
1. **Job Description**: Enter the job description in the text area.
2. **Resume Upload**: Upload a PDF version of the resume.
3. **Analyze Resume**:
   - Click **Tell Me About the Resume** to get an evaluation of the resume based on job requirements.
   - Click **Percentage Match** to receive a match score along with suggestions for improvement.

## File Structure
- **app.py**: Main application code.
- **README.md**: Documentation for the app.
- **requirements.txt**: List of required Python libraries.
- **.env**: Environment file for API keys (not included in repository).

## Troubleshooting
1. **Poppler Installation**: Ensure Poppler is installed and accessible in your PATH if you encounter PDF processing errors.
2. **API Errors**: Check your Google API key and usage limits if there are issues with the AI model responses.


