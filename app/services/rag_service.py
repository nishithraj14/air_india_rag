from typing import List

from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

from app.services.vectorstore import get_vectorstore
from app.core.config import settings


class RAGService:
    """
    Core Retrieval-Augmented Generation (RAG) service.

    Responsibilities:
    - Retrieve relevant Air India policy documents
    - Construct a grounded prompt
    - Generate a factual, document-constrained answer
    """

    def __init__(self):
        # Initialize vector store (Chroma)
        self.vectorstore = get_vectorstore()

        # Initialize LLM
        self.llm = ChatOpenAI(
            model=settings.OPENAI_CHAT_MODEL,
            temperature=0,
        )

    def retrieve_context(self, query: str, k: int = 4) -> List[Document]:
        """
        Retrieve top-k most relevant documents from the vector store.
        """
        return self.vectorstore.similarity_search(query, k=k)

    def build_prompt(self, context_docs: List[Document], question: str) -> str:
        """
        Build a strictly grounded prompt using retrieved documents.
        """
        context_text = "\n\n".join(doc.page_content for doc in context_docs)

        return f"""
You are an official Air India policy assistant.

Answer the user's question using ONLY the information provided
in the context below.

Rules:
- Do NOT use prior knowledge
- Do NOT guess or hallucinate
- If the answer is not explicitly present, reply exactly:
  "Information not available in Air India policy documents."

Context:
{context_text}

Question:
{question}

Answer:
""".strip()

    def ask(self, question: str) -> str:
        """
        Main RAG pipeline:
        1. Retrieve context
        2. Build grounded prompt
        3. Generate answer
        """
        context_docs = self.retrieve_context(question)

        if not context_docs:
            return "Information not available in Air India policy documents."

        prompt = self.build_prompt(context_docs, question)

        response = self.llm.invoke(prompt)

        return response.content.strip()
