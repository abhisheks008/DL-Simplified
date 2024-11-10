import streamlit as st
import requests

# Flask API endpoint for the Resume Analyzer
FLASK_API_URL = "http://localhost:5000/analyze_resume"

st.title("Resume Analyzer")
st.write("Upload a resume PDF and view insights by selecting from different analysis options.")

# File uploader for the PDF resume
uploaded_resume = st.file_uploader("Choose a Resume PDF file", type="pdf")

# Check if the analysis has been done (if results are in session state)
if "response_data" in st.session_state:
    response_data = st.session_state.response_data
else:
    response_data = None

# Submit button to analyze the resume
if st.button("Analyze Resume"):
    if uploaded_resume:
        files = {"fileUploaded": uploaded_resume}

        # Send the resume file to the Flask API
        response = requests.post(FLASK_API_URL, files=files)

        if response.status_code == 200:
            response_data = response.json()
            # Save the response data in session state
            st.session_state.response_data = response_data
            st.success("Resume analyzed successfully!")
        else:
            st.error("Error: Could not retrieve the response from the server.")
    else:
        st.warning("Please upload a resume PDF.")

# Only show analysis options if the response is available
if response_data:
    # Radio button for selecting analysis type
    selected_analysis = st.radio(
        "Select an Analysis to View",
        ["Summary", "Strengths", "Weaknesses", "Suggested Job Titles"]
    )

    # Display analysis based on the selected option
    if selected_analysis == "Summary":
        st.subheader("Summary")
        st.write(response_data.get("summary", "No summary available."))

    elif selected_analysis == "Strengths":
        st.subheader("Strengths")
        st.write(response_data.get("strengths", "No strengths detected."))

    elif selected_analysis == "Weaknesses":
        st.subheader("Weaknesses")
        st.write(response_data.get("weaknesses", "No weaknesses detected."))

    elif selected_analysis == "Suggested Job Titles":
        st.subheader("Suggested Job Titles")
        st.write(response_data.get("job_titles", "No job title suggestions available."))
else:
    st.info("Please upload and analyze a resume first.")
