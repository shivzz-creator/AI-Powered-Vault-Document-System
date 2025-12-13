from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.chat.context_builder import build_context
from app.llm.groq_client import generate_answer

router = APIRouter()

# Request model
class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5  # number of chunks to retrieve

# Response model
class AnswerResponse(BaseModel):
    answer: str
    sources: list[dict]

@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    # 1️⃣ Build RAG context
    context, sources = build_context(request.question, top_k=request.top_k)

    # 2️⃣ Generate LLM answer
    answer = generate_answer(context, request.question)

    return AnswerResponse(answer=answer, sources=sources)
