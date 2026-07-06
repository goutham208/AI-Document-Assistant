from app.vector_store import vector_store
from app.chat import llm


def ask_question(question: str):

    results = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        doc.page_content for doc in results
    )

    sources = list(
        set(
            doc.metadata.get("source", "Unknown")
            for doc in results
        )
    )

    prompt = f"""
You are an AI Document Assistant.

Answer ONLY using the context below.

If the answer is not in the context, say:

"I couldn't find that information in the uploaded document."

Context:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    return {
        "question": question,
        "answer": response.content,
        "sources": sources
    }