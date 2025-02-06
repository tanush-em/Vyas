from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.on_event("startup")
async def startup_event():
    # Initialize your components here
    from vector_store import create_vector_store
    from document_processor import process_document
    
    chunks = process_document("mahabharata.txt")
    app.state.vector_store = create_vector_store(chunks)
    app.state.qa_chain = create_vyas_qa_chain(app.state.vector_store)

@app.post("/ask")
async def ask_vyas(request: QueryRequest):
    try:
        result = app.state.qa_chain({"query": request.question})
        return {"answer": result["result"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))