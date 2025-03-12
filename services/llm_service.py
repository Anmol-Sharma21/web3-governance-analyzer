from langchain_groq import ChatGroq
from config import GROQ_API_KEY

# Initialize LLM Model
llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")

def generate_llm_content(prompt: str) -> str:
    """ Generate content using LLM """
    try:
        response = llm.invoke(prompt)
        return response.content if response else "No response from LLM."
    except Exception as e:
        print(f"Error generating content: {e}")
        return "Failed to generate content."
