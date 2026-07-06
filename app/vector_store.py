from langchain_chroma import Chroma
from app.embeddings import embeddings

DB_DIRECTORY = "chroma_db"

vector_store = Chroma(
    collection_name="ai_document_assistant",
    embedding_function=embeddings,
    persist_directory=DB_DIRECTORY,
)