from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="API REST pour géolocaliser les lieux gratuits à Paris",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Bienvenue sur l'API Paris Gratuit",
        "version": settings.version,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.version,
    }