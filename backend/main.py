from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.settings import settings

app = FastAPI()

# Allow CORS access to frontend service
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FRONTEND_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# test endpoint
@app.get("/ping")
def ping():
    return {"message": "backend reachable"}