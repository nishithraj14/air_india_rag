from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Air India RAG Assistant"
    APP_VERSION: str = "1.0.0"

    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-large"

    # Vector Store
    CHROMA_DIR: str = "data/chroma"
    COLLECTION_NAME: str = "air_india_docs"

    class Config:
        env_file = ".env"


settings = Settings()
