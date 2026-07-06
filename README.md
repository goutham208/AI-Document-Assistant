# 🤖 AI Document Assistant

An AI-powered Document Assistant built using **FastAPI**, **LangChain**, **Google Gemini**, **ChromaDB**, and **Streamlit**.

Upload PDF documents and ask questions in natural language. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant document chunks and generate accurate answers with source citations.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic text chunking
- 🧠 Gemini Embeddings
- 🗂️ Chroma Vector Database
- 🔍 Semantic Search
- 🤖 Gemini 2.5 Flash
- 💬 Interactive Chat Interface
- 📚 Source Citation
- 📝 Chat History
- 🗑️ Clear Chat

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- Google Gemini API
- ChromaDB
- PyPDF
- Requests

---

## 📂 Project Structure

```text
ai-document-assistant/
│
├── app/
│   ├── main.py
│   ├── rag.py
│   ├── chat.py
│   ├── embeddings.py
│   └── vector_store.py
│
├── frontend/
│   └── app.py
│
├── documents/
├── chroma_db/
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Document-Assistant.git
```

Navigate to the project:

```bash
cd AI-Document-Assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
.\venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

## ▶️ Run Streamlit

```bash
python -m streamlit run frontend/app.py
```

---

## 📸 Demo

Upload a PDF and ask questions like:

- When was Greenview founded?
- What is the pet policy?
- Who manages the property?

The application retrieves relevant chunks from the PDF and generates answers using Gemini.

---

## 🎯 Future Improvements

- Multiple PDF support
- Conversation memory
- Streaming responses
- Authentication
- Cloud deployment

---

## 👨‍💻 Author

**Goutham Kumar**

Built as part of my Generative AI Engineering portfolio.