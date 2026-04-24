# PDF AI Agent

An end-to-end AI system that allows users to upload PDFs and interact with them using natural language. The application reads documents, understands their content, and provides accurate answers in a conversational format.

---

## Features

- Upload and process PDF documents  
- Chat-style interface for asking questions  
- Answers grounded in the uploaded document  
- Displays sources used to generate answers  
- Fast and responsive real-time responses  
- Modular and scalable system design  

---

## Tech Stack

- LangGraph (Agent orchestration)  
- Retrieval-Augmented Generation (RAG)  
- FAISS (Vector database for similarity search)  
- HuggingFace Embeddings  
- OpenAI LLM (for reasoning and answer generation)  
- FastAPI (Backend API)  
- Streamlit (Frontend UI)  
- Redis (Session memory layer)  
- LangSmith (Observability and tracing)  

---

## Architecture
Streamlit UI
↓
FastAPI Backend
↓
LangGraph Workflow
↓
Guardrails → Tool Layer → Retrieval
↓
Vector Database (FAISS)
↓
LLM Reasoning
↓
Response + Sources

---

## How It Works (Simple Workflow)

1. Upload a PDF  
   The user uploads any document such as a resume, report, or contract.

2. System reads the document  
   The application extracts all the text from the PDF.

3. Breaks it into smaller pieces  
   The document is split into smaller sections so it becomes easier to search.

4. Stores the information smartly  
   The system organizes these sections so it can quickly find relevant parts later.

5. User asks a question  
   The user types a question in the chat interface.

6. Finds the most relevant parts  
   The system searches the document and selects the sections that best match the question.

7. AI generates an answer  
   The AI reads those sections and generates a clear and accurate answer.

8. Shows answer with sources  
   The user receives:
   - A direct answer  
   - The exact parts of the document used to generate it  

---

## Run Locally

### Backend

```bash
uvicorn app.main:app --reload