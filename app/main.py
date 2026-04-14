from fastapi import FastAPI
from app.api.router import router
from app.core.rag_initializer import initialize_rag_pipeline

app = FastAPI()


@app.on_event("startup")
def startup_event():
    initialize_rag_pipeline()


@app.get("/")
def read_root():
    return {"message": "Clinical RAG AI is running"}


app.include_router(router)