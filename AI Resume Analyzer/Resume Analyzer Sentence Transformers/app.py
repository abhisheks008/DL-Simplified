

import streamlit as st
from resume_analyzer import ResumeAnalyzer
import os

def main():
    st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")
    st.title("Smart Resume Analyzer")

    job_description = st.text_area("Enter the Job Description", height=200)
    st.write("Upload resumes as PDF files:")
    uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True, type="pdf")

    if st.button("Analyze Resumes") and uploaded_files:
        resume_files = []
        for uploaded_file in uploaded_files:
            file_path = os.path.join("/tmp", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            resume_files.append(file_path)

        analyzer = ResumeAnalyzer()
        analysis_results = analyzer.analyze_resumes(resume_files, job_description)

        for result in analysis_results:
            st.write(f"**Resume Name**: {result['Resume Name']}")
            st.write(f"**Job Titles**: {result['Job Titles']}")
            st.write(f"**Primary Skills**: {result['Primary Skills']}")
            st.write(f"**Secondary Skills**: {result['Secondary Skills']}")
            st.write(f"**Total Experience (Years)**: {result['Total Experience (Years)']}")
            st.write(f"**Relevant Experience Duration (Years)**: {result['Relevant Experience Duration (Years)']:.2f}")
            st.write(f"**Average Experience Relevance**: {result['Average Experience Relevance']:.2f}")
            st.write(f"**Relevant Projects**: {result['Relevant Projects']}")
            st.write(f"**Average Project Relevance**: {result['Average Project Relevance']:.2f}")
            st.write(f"**Score**: {result['Score']:.2f}")
            st.write("-" * 50)

        report_path = analyzer.generate_ranking_report(analysis_results)
        with open(report_path, "rb") as report_file:
            st.download_button(
                label="Download Analysis Report as PDF",
                data=report_file,
                file_name="resume_analysis_report.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
