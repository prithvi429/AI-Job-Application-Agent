# Assuming llama3_begin_template and llama3_end_template are already defined for Gemini models

llama3_begin_template = "<|begin_of_text|><|start_header_id|>system<|end_header_id|> "
llama3_end_template = " <|eot_id|> <|start_header_id>assistant<|end_header_id|>"

def get_generator_agent_prompt():
    """
    This function generates the prompt for the generator agent. It creates a personalized cover letter based
    on the user-uploaded CV and matching job listings.
    The generated cover letter should be based on the user's CV and the most relevant job.
    """
    GENERATOR_AGENT = llama3_begin_template + (
        "You are a Generator Agent. "
        "Your task is to generate a personalized cover letter for a user. "
        "The user has uploaded a CV, and based on the provided CV, you need to create a customized cover letter. "
        "The cover letter should reflect the skills, experience, and qualifications present in the CV, and tailor it for a matching job listing. "
        "Ensure the tone is professional and engaging, and make the letter suitable for a job application."
    ) + llama3_end_template

    return GENERATOR_AGENT
