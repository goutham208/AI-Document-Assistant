from langchain_core.documents import Document
from app.vector_store import vector_store

docs = [
    Document(
        page_content="Hello World",
        metadata={"source": "test"}
    )
]

vector_store.add_documents(docs)

print("SUCCESS")