from app.services.rag_service import RAGService

rag = RAGService()

answer = rag.ask("What is the current status of Air India?")
print(answer)
