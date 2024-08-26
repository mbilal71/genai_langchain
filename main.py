from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Create LangChain LLM instance
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=os.environ["GOOGLE_API_KEY"])

# Invoke the LLM
response = llm.invoke(input="What I Can Help You !")

print(response.content)