import logging
from app.core.config import LOG_DIR

LOG_FILE = LOG_DIR / "agent.log"

def setup_logger(name: str = "doc_intelligence_agent") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# What it does?
"""
The code creates a Notebook for your AI to record everything it does.

What it does:
Time-stamps: It marks exactly when something happened.

Prints to Screen: Shows you what’s happening in the VS Code terminal right now.

Saves to File: Writes a permanent copy in agent.log so you can check it later.

Filters: It ignores tiny details but records important actions and errors.

Avoids Clutter: It makes sure the notebook only starts once so it doesn't repeat the same line 5 times.
"""