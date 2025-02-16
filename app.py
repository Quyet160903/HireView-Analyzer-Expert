import streamlit as st
from utils import HireView

def main():
    # Page configuration
    st.set_page_config(
        page_title="HireView Analyzer Expert", 
        page_icon="📄",
        layout="wide")

    # Page title with professional description   
    st.title("📄 HireView Analyzer Expert")
    st.markdown("""
        This application leverages advanced AI models to streamline and enhance the resume screening process.
        Upload your resume, choose the AI models and paste job description to:
        1. Recieve insightful analyses on your resume.
        2. See the percentage match of your resume with the job requirements.
        3. Get suggestions on how to improve.
        4. Save valuable time and effort in the job application process.
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        # Upload resume file
        uploaded_file = st.file_uploader(
            "Upload PDF resume", 
            type=["pdf"],
            help="Please ensure upload in PDF format")
        
        if uploaded_file:
            st.success("Resume uploaded successfully!")


    with col2:
        # Job description input
        job_description = st.text_area(
            "Paste job description here",
            height=200,
            placeholder="Please paste the job description here...")
    
    if uploaded_file and job_description:
        # Select AI model
        model_type = st.selectbox(
            "Select AI model",
            ["GPT-4o", "Gemini-2.0-flash"],
            help="Choose the AI model to analyze your resume")
        
        mapping = {
            "GPT-4o": "openai",
            "Gemini-2.0-flash": "gemini"
        }

        model_type = mapping[model_type]
        
        if st.button("Analyze Resume"):
            pdf_text = HireView.extract_pdf_text(uploaded_file)

            prefix = """
                Analyze the following resume and compare it with the given job description. Follow these steps:

                Extract Key Information: Identify the candidate’s skills, experience, education, and relevant achievements from the resume.
                Compare with Job Requirements: Match the extracted details with the job description, highlighting strengths and gaps.
                Provide Insights & Recommendations: Offer constructive feedback on areas where the resume could be improved to better align with the role.
                Calculate Match Percentage: Based on the alignment of skills, experience, and keywords, provide a match percentage indicating how well the resume fits the job description.
                Input:

                Resume: [Insert Resume Text]
                Job Description: [Insert Job Description]
                Output:

                Key strengths and missing skills.
                Specific suggestions for improvement.
                Final match percentage (0-100%).
                Begin the analysis and conclude with the match percentage.

                Format the response with clear headings and professional language.
            """

            response = HireView.get_model_response(model_type, prefix, pdf_text, job_description)

            if response:
                st.markdown("### Analysis Results")
                st.markdown(response)

                # Add export option
                st.download_button(
                    label="📥 Export Analysis",
                    data=response,
                    file_name="resume_analysis.txt",
                    mime="text/plain"
                )
    else:
        st.info("👆 Please upload your resume and provide the job description to begin the analysis.")

    # Footer
    st.markdown("---")
    st.markdown(
        "This tool uses AI to analyze resumes but should be used as one of many factors in your job application process."
    )

if __name__ == "__main__":
    main()