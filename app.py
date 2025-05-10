import streamlit as st
import os
from data_loader import load_cv, write_to_docx
from job_searcher import search_jobs
from cv_analyzer import analyze_cv_and_jobs
from cover_letter_generator import generate_cover_letter
from agent_router import routing_prompt

# Function to handle the job search and CV analysis, followed by cover letter generation
def process_cv_and_generate_cover_letter(uploaded_cv_file, job_keywords, location_name):
    # Step 1: Load CV
    cv_text = load_cv(uploaded_cv_file)

    # Step 2: Search for jobs based on user input
    job_listings = search_jobs(job_keywords, location_name)

    # Step 3: Analyze the CV and match it to the best job
    best_match_job = analyze_cv_and_jobs(cv_text, job_listings)

    # Step 4: Generate the cover letter for the best matching job
    cover_letter_text = generate_cover_letter(cv_text, best_match_job)

    # Step 5: Write the cover letter to a docx file
    cover_letter_file_path = write_to_docx(cover_letter_text)

    return cover_letter_file_path, cover_letter_text


# Streamlit User Interface
st.title("Cover Letter Generator with CV Analysis")

# Upload CV (PDF)
uploaded_file = st.file_uploader("Upload Your CV (PDF)", type="pdf")
if uploaded_file is not None:
    st.write("CV uploaded successfully!")
    
    # User input for job search (keywords and location)
    job_keywords = st.text_input("Enter job keywords (e.g., 'data scientist')", "data scientist")
    location_name = st.text_input("Enter job location (e.g., 'Berlin')", "Berlin")

    if st.button("Generate Cover Letter"):
        if uploaded_file and job_keywords and location_name:
            # Process the CV, search for jobs, analyze the CV, and generate the cover letter
            cover_letter_file_path, cover_letter_text = process_cv_and_generate_cover_letter(
                uploaded_file, job_keywords, location_name
            )

            # Display success message
            st.success("Cover letter generated successfully!")

            # Display the cover letter
            st.subheader("Generated Cover Letter")
            st.text(cover_letter_text)

            # Provide download button for the cover letter docx file
            with open(cover_letter_file_path, "rb") as file:
                st.download_button(
                    label="Download Cover Letter",
                    data=file,
                    file_name="cover_letter.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

        else:
            st.error("Please fill in all the required fields!")
