def generate_cover_letter(cv_text, job_posting):
    """
    Generate a personalized cover letter based on the CV and job posting.
    :param cv_text: Text from the uploaded CV
    :param job_posting: The selected job posting to generate the letter for
    :return: A personalized cover letter
    """
    cover_letter = f"Dear Hiring Manager,\n\nI am writing to apply for the position of {job_posting['job_title']} at {job_posting['company_name']} in {job_posting['location']}. Based on my experience and skills, I believe I would be a strong fit for this role.\n\nSincerely,\n[Your Name]"
    return cover_letter
