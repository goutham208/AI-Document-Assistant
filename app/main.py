from fastapi import FastAPI, UploadFile, File, Body
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

from app.vector_store import vector_store
from app.rag import ask_question

import os
import shutil

app = FastAPI(
    title="AI Document Assistant",
    description="RAG-powered PDF Question Answering API",
    version="2.0"
)

UPLOAD_FOLDER = "documents"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Document Assistant 🚀"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    documents = [
        Document(
            page_content=chunk,
            metadata={
                "source": file.filename
            }
        )
        for chunk in chunks
    ]

    vector_store.add_documents(documents)

    return {
        "message": "Document indexed successfully!",
        "filename": file.filename,
        "chunks": len(chunks)
    }


@app.post("/chat")
async def chat(question: str = Body(..., embed=True)):

    response = ask_question(question)

    return response