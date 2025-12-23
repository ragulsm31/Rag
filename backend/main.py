from fastapi import FastAPI, UploadFile, File
from backend.pdf_utils import extract_text
from backend.rag import split_text, create_vector_store, answer_question

app = FastAPI(title="PDF RAG API")

@app.post("/upload")
async def upload_pdfs(files: list[UploadFile] = File(...)):
    text = extract_text(files)
    chunks = split_text(text)
    create_vector_store(chunks)
    return {"status": "PDFs processed successfully"}

@app.get("/ask")
async def ask(q: str):
    return {"answer": answer_question(q)}
