from app.core.config import MAX_QUESTION_LENGTH


BLOCKED_PHRASES = [
    "ignore previous instructions",
    "reveal system prompt",
    "delete all files",
    "run shell command",
]


def validate_question(question: str) -> str:
    question = question.strip()

    if not question:
        raise ValueError("Question cannot be empty.")

    if len(question) > MAX_QUESTION_LENGTH:
        raise ValueError(f"Question is too long. Max length is {MAX_QUESTION_LENGTH} characters.")

    lowered = question.lower()

    for phrase in BLOCKED_PHRASES:
        if phrase in lowered:
            raise ValueError("Question contains unsafe instruction patterns.")

    return question