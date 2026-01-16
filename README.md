✈️ Air India RAG Assistant

A Retrieval-Augmented Generation (RAG) based knowledge assistant for Air India documents, built using FastAPI, OpenAI embeddings, and a persistent vector database, with a professional airline-grade UI.

This system allows users to ask natural-language questions and receive grounded, factual answers strictly based on internal Air India documents (PDFs).

🔍 What This Project Does

Ingests Air India PDFs (HR regulations, routes, fact sheets, history)

Converts documents into vector embeddings (OpenAI)

Stores embeddings in a persistent vector database (ChromaDB)

Retrieves relevant context at query time

Uses an LLM to generate context-grounded answers

Prevents hallucination by refusing to answer when information is missing

Exposes functionality via a FastAPI backend

Provides a clean, professional Air India–style web UI

Architecture

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/feeff4a0-ef1c-480c-8f48-8b085b60c52a" />



UI

<img width="1881" height="917" alt="image" src="https://github.com/user-attachments/assets/c484af04-c5a4-4e63-9b91-308a0e665e19" />

🧰 Tech Stack
Layer	Technology
Backend	FastAPI
LLM	OpenAI (Chat models)
Embeddings	OpenAI Embeddings
Vector DB	ChromaDB (persistent)
Document Parsing	PyPDF
Frontend	HTML + CSS + JavaScript
Config	Pydantic Settings
Logging	Python logging
Server	Uvicorn


project structure 
AirIndia_Rag_Chatbot/
│
├── app/
│   ├── api/            # FastAPI routes
│   ├── core/           # config & logging
│   ├── schemas/        # request/response models
│   ├── services/       # RAG, vector store logic
│   ├── static/         # UI (HTML, CSS, JS, images)
│   └── main.py         # FastAPI entry point
│
├── data/
│   ├── raw_pdfs/       # Air India PDFs
│   └── chroma/         # Vector database (auto-generated)
│
├── scripts/
│   ├── ingest_documents.py
│   └── test_rag.py
│
├── .env
├── requirements.txt
├── README.md
└── venv/

🚀 How to Run the Project (Step-by-Step)
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/air-india-rag-assistant.git
cd air-india-rag-assistant

2️⃣ Create & Activate Virtual Environment
python -m venv venv


Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in project root:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx


(Optional)

OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-large

5️⃣ Ingest Documents (ONE-TIME)

Run this once, or whenever PDFs change:

python scripts/ingest_documents.py


This will:

Load PDFs

Split text into chunks

Generate embeddings

Persist ChromaDB to disk

6️⃣ Start the Backend Server
uvicorn app.main:app --reload


You should see:

Uvicorn running on http://127.0.0.1:8000

7️⃣ Access the Application

UI → http://127.0.0.1:8000

Health Check → http://127.0.0.1:8000/api/health

Swagger Docs → http://127.0.0.1:8000/docs

🧪 Sample Questions to Try
General

Who is the CEO of Air India?

What is Vihaan.AI and which phase is Air India in?

Operations

How many domestic destinations does Air India serve?

Does Air India operate flights to North America?

HR & Policy

Can an employee opt for voluntary retirement?

Are employees allowed to work outside India?

What is the probation period for Air India employees?

Safety & History

What was the deadliest Air India accident?

What happened during Air India Flight 182?

If an answer is not present in documents, the system will correctly respond:

“I do not have enough information.”

✅ Key Features Demonstrated

Retrieval-Augmented Generation (RAG)

Hallucination control

Persistent vector database

Clean API design

Professional UI

Enterprise-ready architecture
