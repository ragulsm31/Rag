import streamlit as st
import requests

API_URL = "http://backend:8000"

st.set_page_config(page_title="Chat with PDF")
st.header("📄 Chat with PDF (Gemini RAG)")

question = st.text_input("Ask a question")
if question:
    res = requests.get(f"{API_URL}/ask", params={"q": question})
    st.write("Answer:", res.json()["answer"])

with st.sidebar:
    st.subheader("Upload PDFs")
    files = st.file_uploader("Upload PDF files", accept_multiple_files=True)

    if st.button("Process PDFs"):
        if not files:
            st.warning("Upload at least one PDF")
        else:
            payload = [("files", (f.name, f, "application/pdf")) for f in files]
            requests.post(f"{API_URL}/upload", files=payload)
            st.success("PDFs indexed successfully")
