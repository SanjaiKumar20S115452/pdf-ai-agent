from fastapi import FastAPI
from app.api.routes import router
from app.observability.tracing import init_tracing

app = FastAPI(
    title="Private Enterprise Knowledge Agent",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():
    init_tracing()


@app.get("/")
def health_check():
    return {"status": "running"}


app.include_router(router)



# from fastapi import FastAPI
# from pydantic import BaseModel

# from app.graph import agent

# app = FastAPI()

# class Request(BaseModel):
#     question: str
    

# @app.get("/")
# def home():
#     return {"status": "running"}

# @app.post("/ask")
# def ask(req: Request):
#     result = agent.invoke({
#         "question": req.question,
#         "context": [],
#         "answer": ""
#     })
    
#     return {
#         "question": req.question,
#         "answer": result["answer"]
#     }

# from fastapi import FastAPI

# from app.api.routes import router

# app = FastAPI(
#     title="Private Enterprise Knowledge Agent",
#     description="Production-grade document intelligence agent using LangGraph, RAG, and LLM reasoning",
#     version = "1.0.0"
# )

# @app.get("/")
# def health_check():
#     return {
#         "status": "running",
#         "service": "Private Enterprise Knowledge Agent"
#     }
    
# app.include_router(router)