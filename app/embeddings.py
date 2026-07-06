from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"

print("Looking for:", env_path)
print("File exists:", env_path.exists())

load_dotenv(dotenv_path=env_path)

print("API Key:", os.getenv("GOOGLE_API_KEY"))

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)