from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.core.config import settings


def get_vectorstore():
    embeddings = OpenAIEmbeddings(
        model=settings.OPENAI_EMBEDDING_MODEL
    )

    vectorstore = Chroma(
        persist_directory=settings.CHROMA_DIR,
        collection_name=settings.COLLECTION_NAME,
        embedding_function=embeddings
    )

    return vectorstore
