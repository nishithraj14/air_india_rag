"""
Air India Policy Assistant – Streamlit Demo

• Production-grade RAG demo
• Uses Chroma vector store
• Strictly grounded answers
• Designed for Streamlit Cloud
• No local secrets.toml required
"""

import os
import streamlit as st

from app.services.rag_service import RAGService

# ==================================================
# Secure OpenAI API Key Handling
# ==================================================
OPENAI_API_KEY = None

try:
    # Streamlit Cloud
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except Exception:
    # Local development (.env or system env)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error(
        "OPENAI_API_KEY not configured.\n\n"
        "• Local: set it in .env\n"
        "• Streamlit Cloud: set it in App Secrets"
    )
    st.stop()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="Air India Policy Assistant",
    page_icon="✈️",
    layout="wide"
)

# ==================================================
# Header / Branding
# ==================================================
st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            color: #8b0000;
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 18px;
            color: #cccccc;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">✈️ Air India Policy Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    'Document-grounded AI assistant for official Air India policies'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# Description
# ==================================================
st.markdown("""
🔒 **No hallucinations**  
📄 **Answers are grounded in official policy text**  
⚠️ **If information is unavailable, the assistant clearly states so**
""")

st.divider()

# ==================================================
# Sample Questions (VISIBLE ON ALL THEMES)
# ==================================================
st.markdown("### 💡 Try asking questions like:")

st.markdown(
    """
    <div style="
        background-color: #ffffff;
        color: #111111;
        padding: 18px;
        border-radius: 10px;
        border-left: 6px solid #8b0000;
        line-height: 1.8;
        font-size: 16px;
        max-width: 900px;
    ">
        • What is the baggage allowance for domestic flights?<br>
        • What is Air India’s cancellation policy?<br>
        • Are refunds allowed for non-refundable tickets?<br>
        • What documents are required for international travel?<br>
        • What are the check-in time rules?
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# Load RAG Service (Cached)
# ==================================================
@st.cache_resource
def load_rag():
    return RAGService()

rag = load_rag()

# ==================================================
# Chat Interface
# ==================================================
if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])

query = st.chat_input("Ask a question about Air India policies")

if query:
    st.chat_message("user").write(query)

    with st.spinner("Searching official Air India policy documents..."):
        answer = rag.ask(query)

    st.chat_message("assistant").write(answer)

    st.session_state.chat.append({"role": "user", "content": query})
    st.session_state.chat.append({"role": "assistant", "content": answer})

# ==================================================
# Footer
# ==================================================
st.divider()
st.markdown(
    """
    **Note:**  
    This demo uses document-grounded AI.  
    If the information is not present in the documents, the assistant will say so explicitly.
    """
)
