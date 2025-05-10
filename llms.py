import os
from langchain_google_genai import ChatGoogleGenerativeAI

def load_llm(llm_name: str):
    """
    Load the specified LLM model and validate API key.
    :param llm_name: Name of the LLM to load
    :return: LLM instance
    """
    api_key = os.getenv("GOOGLE_GENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("API key for Google Generative AI is missing. Set 'GOOGLE_GENAI_API_KEY' in the environment.")

    if llm_name == "gemini-pro":
        return ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.7,
            convert_system_message_to_human=True,
            api_key=api_key
        )
    
    raise ValueError(f"LLM '{llm_name}' is not supported.")
