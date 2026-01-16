import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Configuration
# --------------------------------------------------
PDF_DIR = "data/raw_pdfs"
CHROMA_DIR = "data/chroma"
COLLECTION_NAME = "air_india_docs"

# --------------------------------------------------
# Step 1: Load PDF documents
# --------------------------------------------------
print("Loading PDF documents...")
loader = PyPDFDirectoryLoader(PDF_DIR)
documents = loader.load()
print(f"Loaded {len(documents)} documents")

# --------------------------------------------------
# Step 2: Split documents into chunks
# --------------------------------------------------
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} text chunks")

# --------------------------------------------------
# Step 3: Initialize OpenAI embeddings
# --------------------------------------------------
print("Initializing OpenAI embeddings...")
embeddings = OpenAIEmbeddings(
    model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
)

# --------------------------------------------------
# Step 4: Create Chroma vector store (auto-persisted)
# --------------------------------------------------
print("Creating Chroma vector store...")
Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_DIR,
    collection_name=COLLECTION_NAME
)

print("Ingestion complete. Vector store saved successfully.")
