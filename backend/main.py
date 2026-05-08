
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from routes.chat import router as chat_router

app = FastAPI()

app.include_router(
    chat_router,
    prefix="/chat"
)


@app.get("/")

def home():

    return {
        "message":
        "Mental Health AI Backend Running"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

