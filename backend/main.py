from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
    title="Adventure Story Game",
    description="Adventure Story Game"
)

app.add_middleware(CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app",host="0.0.0.0", port=8000,reload=True)
