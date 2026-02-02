from langchain_openai import OpenAIEmbeddings
from app.core.config import settings


def get_embeddings():
    return OpenAIEmbeddings(
        model=settings.OPENAI_EMBEDDING_MODEL
    )
