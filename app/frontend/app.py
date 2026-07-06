import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

st.title("🤖 AI Document Assistant")
st.markdown("### Chat with your PDF using Gemini + ChromaDB")

# -----------------------------
# Sidebar - Upload PDF
# -----------------------------
st.sidebar.header("📄 Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.sidebar.button("Upload PDF"):

        with st.spinner("Uploading and indexing PDF..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

        if response.status_code == 200:

            data = response.json()

            st.sidebar.success("✅ PDF uploaded successfully!")

            st.sidebar.write(f"**File:** {data['filename']}")
            st.sidebar.write(f"**Chunks:** {data['chunks']}")

        else:
            st.sidebar.error("Upload failed!")
            st.sidebar.json(response.json())

# -----------------------------
# Chat Section
# -----------------------------
st.header("💬 Ask Questions")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "question": question
                }
            )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Answer")

            st.write(result["answer"])

            st.divider()

            st.subheader("📚 Source Documents")

            for source in result["sources"]:
                st.write(f"• {source}")

        else:

            st.error("Something went wrong!")

            st.json(response.json())