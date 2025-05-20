# api/main.py
# Eden Protocol – FastAPI Entry Point

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import settings
from api.middleware import add_security_middleware
from api.routes import (
    auth,
    avatar,
    tree_of_life,
    quests,
    xp,
    dao,
    soulform,
    world_tree
)

app = FastAPI(
    title="Eden Protocol API",
    description="Symbolic and therapeutic backend for Eden Protocol",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# === CORS Middleware ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Custom Security Middleware ===
add_security_middleware(app)

# === Route Modules ===
app.include_router(auth.router)
app.include_router(avatar.router)
app.include_router(tree_of_life.router)
app.include_router(quests.router)
app.include_router(xp.router)
app.include_router(dao.router)
app.include_router(soulform.router)
app.include_router(world_tree.router)

# === Health Check ===
@app.get("/health", tags=["system"])
async def health_check():
    return {
        "success": True,
        "message": "Eden Protocol API is operational.",
        "timestamp": settings.now()
    }
