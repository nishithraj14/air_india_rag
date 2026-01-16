from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

from app.services.vectorstore import get_vectorstore
from app.core.config import settings


class RAGService:
    def __init__(self):
        self.vectorstore = get_vectorstore()
        self.llm = ChatOpenAI(
            model=settings.OPENAI_CHAT_MODEL,
            temperature=0
        )

    def retrieve_context(self, query: str, k: int = 4) -> list[Document]:
        return self.vectorstore.similarity_search(query, k=k)

    def build_prompt(self, context_docs: list[Document], question: str) -> str:
        context_text = "\n\n".join(doc.page_content for doc in context_docs)

        prompt = f"""
You are an Air India official assistant.
Answer the user's question using ONLY the information provided in the context.
If the answer is not present in the context, say you do not have enough information.

Context:
{context_text}

Question:
{question}

Answer:
"""
        return prompt.strip()

    def ask(self, question: str) -> str:
        context_docs = self.retrieve_context(question)
        prompt = self.build_prompt(context_docs, question)
        response = self.llm.invoke(prompt)
        return response.content
