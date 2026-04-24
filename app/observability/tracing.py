import os
from langsmith import Client
from app.core.logging import setup_logger

logger = setup_logger(__name__)

client = None

def init_tracing():
    global client
    
    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        try:
            client = Client()
            logger.info("LangSmith tracing initialized")
        except Exception as e:
            logger.warning(f"LangSmith init failed: {e}")
        else:
            logger.info("LangSmith tracing disabled")
            
# What this file does?
"""
this initialized tracing.
if enabled -> connect to LangSmith
if not -> skip safely
"""