import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
API_URL = "https://ai-document-assistant-4hq9.onrender.com"

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

if "chunks" not in st.session_state:
    st.session_state.chunks = 0

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("📄 Document Upload")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if st.button("Upload PDF", use_container_width=True):

        if uploaded_file is None:
            st.warning("Please choose a PDF.")
        else:

            with st.spinner("Uploading and indexing..."):

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

                st.session_state.uploaded_file = data["filename"]
                st.session_state.chunks = data["chunks"]

                st.success("✅ Document indexed successfully!")

            else:
                st.error("Upload failed.")

                st.write("Status Code:", response.status_code)
                st.write("Response Text:")
                st.text(response.text)

    st.divider()

    st.subheader("📑 Current Document")

    if st.session_state.uploaded_file:

        st.success(st.session_state.uploaded_file)

        st.write(
            f"**Chunks:** {st.session_state.chunks}"
        )

    else:
        st.info("No document uploaded.")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Main Page
# -----------------------------
st.title("🤖 AI Document Assistant")

st.caption(
    "Upload a PDF and ask questions using Gemini + LangChain + ChromaDB"
)

st.divider()

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
            and message["sources"]
        ):

            with st.expander("📚 Sources"):

                for source in message["sources"]:
                    st.write(f"• {source}")

# -----------------------------
# Chat Input
# -----------------------------
question = st.chat_input(
    "Ask a question about your document..."
)

if question:

    if st.session_state.uploaded_file is None:

        st.warning("Please upload a PDF first.")

    else:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = requests.post(
                    f"{API_URL}/chat",
                    json={
                        "question": question
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    answer = result["answer"]
                    sources = result["sources"]

                    st.markdown(answer)

                    if sources:

                        with st.expander("📚 Sources"):

                            for source in sources:
                                st.write(f"• {source}")

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "sources": sources
                        }
                    )

                else:

                    st.error("Something went wrong!")

                    st.write("Status Code:", response.status_code)
                    st.write("Response Text:")
                    st.text(response.text)