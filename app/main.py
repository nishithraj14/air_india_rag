from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.core.logging import setup_logging
from app.core.config import settings

# --------------------------------------------------
# Logging
# --------------------------------------------------
setup_logging()

# --------------------------------------------------
# App
# --------------------------------------------------
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Retrieval-Augmented Generation assistant for Air India documents",
)

# --------------------------------------------------
# CORS
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# API routes
# --------------------------------------------------
app.include_router(health_router, prefix="/api")
app.include_router(chat_router, prefix="/api")

# --------------------------------------------------
# Static files
# --------------------------------------------------
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def serve_ui():
    return FileResponse("app/static/index.html")
