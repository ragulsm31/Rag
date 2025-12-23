# 📄 Chat with RAG Application

## 🚀 What this project does

- Upload one or more PDF files
- Extract and chunk PDF text
- Convert text into embeddings using **Gemini embeddings**
- Store embeddings in **ChromaDB**
- Ask natural language questions
- Get accurate, context-based answers from the PDF

---

## 📁 Project Structure

```
pdf-chat-rag/
│
├── backend/
│   ├── main.py        # FastAPI backend routes
│   ├── rag.py         # RAG logic (Gemini + Chroma)
│   └── pdf_utils.py   # PDF text extraction
│
├── frontend/
│   └── app.py         # Streamlit UI (single-page)
│
├── chroma_db/         # Vector database (auto-created)
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

## 🔧 Tech Stack

- **Python 3.10**
- **Streamlit** – Frontend UI
- **FastAPI** – Backend APIs
- **LangChain (v0.2.x)** – RAG orchestration
- **Google Gemini** – LLM + embeddings
- **ChromaDB** – Vector database
- **Docker & Docker Compose**

---

## ⬇️ Download / Clone

### Clone from GitHub
```bash
git clone https://github.com/ragulsm31/Rag
cd Rag
```

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```


## 🐳 Run the Project (Recommended: Docker)

Make sure **Docker** and **Docker Compose** are installed.

```bash
docker-compose up --build
```


## 🧪 How to Use the App

1. Open the Streamlit UI
2. Upload one or more PDF files
3. Click **Process PDFs**
4. Ask a question related to the document
5. View the AI-generated answer

---

## 👤 Author & GitHub Credit

**Author:** Ragul SM  
**GitHub:** https://github.com/ragulsm31  

## 📜 License

This project is open-source and intended for **educational and learning purposes**.

---

⭐ If you find this project useful, please consider giving it a **star** on GitHub.
