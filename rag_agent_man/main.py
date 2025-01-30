from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag_agent_man.graph import get_graph
from rag_agent_man.rag import RAG

app = FastAPI()

# CORS configuration (needed for frontend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instantiate RAG once and reuse it
rag = RAG()
graph = get_graph()

class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    final_state = graph.invoke({"question": request.question},
        config={"configurable": {"rag": rag}},
    )

    final_answer = final_state["answer"]
    return {"answer": final_answer}
