# PDF AI Agent

An end-to-end AI-powered document intelligence system that allows users to upload PDF documents and interact with them using natural language.

The application processes uploaded documents, understands contextual information, retrieves relevant knowledge using semantic search, and generates grounded conversational responses with source attribution.

The system is designed using a modular, scalable, and production-oriented architecture inspired by modern AI engineering workflows.

---

# Features

- Upload and process PDF documents
- Conversational chat interface for document interaction
- Retrieval-Augmented Generation (RAG) pipeline
- Context-aware semantic search
- AI-generated responses grounded in uploaded documents
- Source citation and retrieved context visibility
- Session-aware conversational memory
- Modular LangGraph-based agent orchestration
- Scalable API-driven backend architecture
- Real-time response generation

---

# Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | Streamlit |
| Backend API | FastAPI |
| Agent Orchestration | LangGraph |
| LLM Reasoning | OpenAI |
| Embeddings | HuggingFace Embeddings |
| Vector Database | FAISS |
| Session Memory | Redis |
| Observability | LangSmith |
| AI Architecture | Retrieval-Augmented Generation (RAG) |

---

# System Architecture

```text
                    ┌──────────────────────┐
                    │     Streamlit UI     │
                    │  Chat + PDF Upload   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    │  Request Handling    │
                    └──────────┬───────────┘
                               │
                               ▼
                ┌────────────────────────────┐
                │     LangGraph Workflow     │
                │ Agent Orchestration Layer  │
                └──────────┬─────────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
┌──────────────────┐              ┌────────────────────┐
│ Guardrails Layer │              │ Session Memory     │
│ Validation/Rules │              │ Redis-backed State │
└─────────┬────────┘              └────────────────────┘
          │
          ▼
┌───────────────────────────────┐
│ Retrieval Pipeline (RAG)      │
│ Query Understanding + Search  │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Vector Database (FAISS)       │
│ Semantic Similarity Search    │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ OpenAI LLM Reasoning Engine   │
│ Contextual Answer Generation  │
└──────────────┬────────────────┘
               ▼
┌───────────────────────────────┐
│ Final Response + Citations    │
└───────────────────────────────┘

Workflow Overview

1. Document Ingestion

The user uploads a PDF document through the Streamlit interface.

The backend extracts raw textual content from the uploaded file using a document parsing pipeline.

⸻

2. Chunking & Preprocessing

The extracted document is segmented into smaller semantic chunks to improve retrieval accuracy and contextual relevance during search.

Each chunk is cleaned, normalized, and prepared for embedding generation.

⸻

3. Embedding Generation

The system converts each document chunk into dense vector embeddings using HuggingFace embedding models.

These embeddings capture semantic meaning rather than simple keyword matching.

⸻

4. Vector Storage

Generated embeddings are stored inside a FAISS vector index for high-speed similarity retrieval.

This enables efficient semantic search across large documents.

⸻

5. User Query Processing

When the user submits a question:

* The query is embedded
* Semantic similarity search is performed
* The most relevant document chunks are retrieved

⸻

6. Retrieval-Augmented Generation (RAG)

Retrieved context is injected into the LLM prompt.

The OpenAI model generates grounded responses using only the relevant document context.

This minimizes hallucinations and improves answer accuracy.

⸻

7. Conversational Response

The system returns:

* A context-aware answer
* Supporting document sources
* Retrieved passages used during reasoning

⸻

Engineering Highlights

* Retrieval-Augmented Generation (RAG)
* Agent-based orchestration with LangGraph
* Semantic vector similarity search using FAISS
* Session-aware conversational memory with Redis
* Modular service-oriented backend architecture
* Real-time conversational document interaction
* Scalable FastAPI-based backend design
* Source-grounded AI reasoning pipeline
* Observability and tracing with LangSmith


pdf-ai-agent/
│
├── app/
│   ├── api/                 # FastAPI routes
│   ├── graph/               # LangGraph workflows
│   ├── services/            # Business logic
│   ├── tools/               # Tool layer
│   ├── vectorstore/         # FAISS operations
│   ├── memory/              # Redis session memory
│   ├── models/              # Pydantic schemas
│   └── core/                # Config + logging
│
├── ui/                      # Streamlit frontend
│
├── data/                    # Uploaded PDFs
├── requirements.txt
└── README.md

Running the Project Locally

1. Clone the repository

git clone <repository-url>
cd pdf-ai-agent

2. Create a virtual environment

python -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
REDIS_URL=redis://localhost:6379

5. Start Redis
docker run -p 6379:6379 redis

6. Start the FastAPI backend
uvicorn app.main:app --reload

Backend will run at:
http://127.0.0.1:8000

7. Start the Streamlit frontend
streamlit run ui/app.py

Frontend will run at:
http://localhost:8501


Example Use Cases

* Resume analysis
* Contract understanding
* Research paper Q&A
* Technical documentation assistant
* Financial report analysis
* Policy and compliance document review
* Academic learning assistant

⸻

Future Enhancements

* Multi-document retrieval support
* Hybrid retrieval (semantic + keyword)
* Streaming token responses
* Distributed vector databases
* Persistent conversation memory
* Multi-agent workflows
* Kubernetes deployment
* Async ingestion pipelines
* Advanced document citation rendering

⸻

Observability

The system integrates LangSmith for:

* Workflow tracing
* Agent execution monitoring
* Prompt debugging
* Retrieval inspection
* Performance analysis

⸻

Key Learning Outcomes

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* AI agent orchestration
* Semantic vector search
* Conversational AI systems
* LLM grounding techniques
* Production-oriented AI architecture
* FastAPI backend engineering
* Session-aware AI memory systems