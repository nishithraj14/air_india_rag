import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

CHROMA_DIR = "data/chroma"
COLLECTION_NAME = "air_india_docs"


def get_vectorstore():
    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
    )

    vectorstore = Chroma(
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings
    )

    return vectorstore
