from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.rag_chain import create_rag_chain

# 1️⃣ Create app FIRST
app = FastAPI()

# 2️⃣ Add CORS AFTER app is defined
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ Create RAG chain
rag_chain = create_rag_chain()


class QueryRequest(BaseModel):
    question: str


@app.post("/chat")
async def chat(request: QueryRequest):
    response = rag_chain.invoke(request.question)
    return {"answer": response}