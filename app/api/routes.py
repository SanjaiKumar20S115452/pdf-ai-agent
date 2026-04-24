from fastapi import APIRouter, HTTPException
from app.api.schemas import AskRequest, AskResponse, SourceChunk
from app.graph.workflow import agent_workflow
from app.core.logging import setup_logger
from fastapi import APIRouter, HTTPException, UploadFile, File
import shutil
from app.services.pdf_service import save_uploaded_pdf, convert_pdf_to_text_file
from app.core.config import VECTOR_STORE_DIR

logger = setup_logger(__name__)
router = APIRouter()

@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    try:
        from app.memory.redis_memory import save_message, get_history

        save_message(
            session_id=request.session_id,
            role="user",
            content=request.question
        )

        history = get_history(request.session_id)

        result = agent_workflow.invoke({
            "question": request.question,
            "retrieved_docs": [],
            "answer": ""
        })

        save_message(
            session_id=request.session_id,
            role="assistant",
            content=result["answer"]
        )

        sources = [
            SourceChunk(
                source=doc.metadata.get("source", "unknown"),
                content=doc.page_content
            )
            for doc in result["retrieved_docs"]
        ]

        logger.info(f"API request completed successfully. History length: {len(history)}")

        return AskResponse(
            question=request.question,
            answer=result["answer"],
            sources=sources
        )

    except Exception as e:
        logger.error(f"API request failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

        file_bytes = await file.read()

        pdf_path = save_uploaded_pdf(
            file_bytes=file_bytes,
            filename=file.filename
        )

        txt_path = convert_pdf_to_text_file(pdf_path)

        # Reset vector store so new PDF content gets indexed
        if VECTOR_STORE_DIR.exists():
            shutil.rmtree(VECTOR_STORE_DIR)

        logger.info("Vector store reset after PDF upload")

        return {
            "message": "PDF uploaded and processed successfully",
            "pdf_file": file.filename,
            "text_file": txt_path.name
        }

    except Exception as e:
        logger.error(f"PDF upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))