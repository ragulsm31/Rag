from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

DB_DIR = "chroma_db"

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=300)
    return splitter.split_text(text)

def create_vector_store(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    Chroma.from_texts(texts=chunks, embedding=embeddings, persist_directory=DB_DIR).persist()

def answer_question(question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    docs = db.similarity_search(question, k=4)

    prompt = PromptTemplate(
        template="""
Answer the question using only the provided context.
If the answer is not present, say:
"Answer is not available in the provided context."

Context:
{context}

Question:
{question}

Answer:
""",
        input_variables=["context", "question"],
    )

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)

    result = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
    return result["output_text"]
