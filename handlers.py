"""
Response handlers for different message categories.

This module provides specialized handlers for different types of user messages
based on the evaluation results from evaluator.py.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from evaluator import EvaluationResult

ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR / ".env", override=True)

# Use a fast model for simple responses
HANDLER_MODEL = os.getenv("EVAL_MODEL_NAME", "gpt-4o-mini")

openai = OpenAI()


def handle_greeting(user_message: str) -> str:
    """
    Generate a brief, friendly greeting response.

    Args:
        user_message: The greeting message from the user

    Returns:
        A brief, warm greeting that introduces the digital twin
    """
    system_prompt = """You are a digital twin representing Veronika Pomyateeva.

The user just greeted you. Respond with a brief (1-2 sentences), warm, professional
greeting that:
- Acknowledges their greeting
- Introduces yourself as Veronika's AI digital twin
- Invites them to ask about Veronika's career, background, or experience

Keep it natural and friendly, not robotic."""

    response = openai.chat.completions.create(
        model=HANDLER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


def handle_off_topic(user_message: str, evaluation: EvaluationResult) -> str:
    """
    Generate a graceful refusal for off-topic questions.

    Args:
        user_message: The off-topic message from the user
        evaluation: The evaluation result with reasoning

    Returns:
        A polite refusal that redirects to career topics
    """
    system_prompt = """You are a digital twin representing Veronika Pomyateeva.

A visitor asked something outside your scope - you only discuss Veronika's career,
background, skills, and professional experience.

Write a short (2-3 sentences), warm, professional reply that:
- Briefly acknowledges what they asked (be specific, not generic)
- Explains you can only help with career-related questions
- Offers to help with professional topics instead

Be friendly but firm. Don't apologize excessively. Stay in character as Veronika's twin."""

    response = openai.chat.completions.create(
        model=HANDLER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"User asked: {user_message}\n\nWhy it's off-topic: {evaluation.reasoning}",
            },
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


def handle_inappropriate(user_message: str) -> str:
    """
    Generate a firm but professional response to inappropriate content.

    Args:
        user_message: The inappropriate message from the user

    Returns:
        A brief, professional boundary-setting response
    """
    return (
        "I'm here to provide information about Veronika's professional background "
        "and career. I'm not able to engage with that type of content. "
        "If you have questions about her work experience, skills, or projects, "
        "I'd be happy to help with those."
    )


def route_message(user_message: str, evaluation: EvaluationResult) -> str:
    """
    Route a message to the appropriate handler based on evaluation.

    This is called for messages that DON'T need full agent processing
    (greetings, off-topic, inappropriate).

    Args:
        user_message: The user's message
        evaluation: The evaluation result

    Returns:
        An appropriate response for the message category
    """
    if evaluation.category == "greeting":
        return handle_greeting(user_message)
    elif evaluation.category == "off_topic":
        return handle_off_topic(user_message, evaluation)
    elif evaluation.category == "inappropriate":
        return handle_inappropriate(user_message)
    else:
        # Fallback - shouldn't normally reach here
        return (
            "I'm Veronika's AI digital twin, here to answer questions about her "
            "career, background, and professional experience. How can I help you?"
        )
