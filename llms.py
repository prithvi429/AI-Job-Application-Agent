import os
from langchain_google_genai import ChatGoogleGenerativeAI

def load_llm(llm_name: str):
    if llm_name == "gemini-pro":
        return ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.7,
            convert_system_message_to_human=True
        )
    raise ValueError(f"LLM '{llm_name}' is not supported.")
