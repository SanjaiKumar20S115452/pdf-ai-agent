import json
import redis
from app.core.config import REDIS_URL
from app.core.logging import setup_logger

logger = setup_logger(__name__)

redis_client = redis.from_url(REDIS_URL, decode_responses=True)


def save_message(session_id: str, role: str, content: str) -> None:
    """
    Save one message into Redis conversation history.
    """
    key = f"session:{session_id}:messages"

    message = {
        "role": role,
        "content": content
    }

    redis_client.rpush(key, json.dumps(message))
    redis_client.expire(key, 60 * 60 * 24)

    logger.info(f"Saved {role} message to Redis session {session_id}")


def get_history(session_id: str) -> list[dict]:
    """
    Retrieve conversation history from Redis.
    """
    key = f"session:{session_id}:messages"

    messages = redis_client.lrange(key, 0, -1)

    return [json.loads(message) for message in messages]


def clear_history(session_id: str) -> None:
    """
    Clear a Redis conversation session.
    """
    key = f"session:{session_id}:messages"

    redis_client.delete(key)

    logger.info(f"Cleared Redis session {session_id}")


"""
save_message() → store user/assistant messages
get_history() → retrieve previous conversation
clear_history() → delete session memory

With redis, agent can remember:
1. session history
2. previous questions
3. cached answers
4. temporary state

ARCHITECTURE

User Question
   ↓
FastAPI
   ↓
Redis Memory Check
   ↓
LangGraph Agent
   ↓
Store Conversation in Redis
   ↓
Final Answer
"""
