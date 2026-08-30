import json
import os
from pathlib import Path
import requests
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent.parent  # Go up to project root
load_dotenv(ROOT_DIR / ".env", override=True)

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

pushover_url = "https://api.pushover.net/1/messages.json"


def push(text):
    """Send notification via Pushover. Fails gracefully if Pushover is unavailable."""
    try:
        requests.post(
            pushover_url,
            data={
                "token": pushover_token,
                "user": pushover_user,
                "message": text,
            },
            timeout=5,  # Don't hang forever
        )
        print(f"[PUSHOVER] Notification sent: {text[:50]}...")
    except Exception as e:
        # Log error 
        print(f"[PUSHOVER] Failed to send notification: {type(e).__name__}: {e}")


def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"Recording interest from {name} with email {email} and notes {notes}")
    return "OK"


def record_unknown_question(question):
    push(f"Recording {question} asked that I couldn't answer")
    return "OK"


def log_evaluation(user_message, category, confidence, reasoning, was_blocked=False):
    """
    Log evaluation metrics to Pushover for monitoring.

    Args:
        user_message: The user's message
        category: The classification category
        confidence: The confidence level
        reasoning: The reasoning for the classification
        was_blocked: Whether the message was blocked (not processed normally)
    """
    if was_blocked:
        # Log blocked messages (off-topic, inappropriate)
        push(
            f"🚫 BLOCKED: {category}\n"
            f"Message: {user_message[:100]}\n"
            f"Confidence: {confidence}\n"
            f"Reason: {reasoning}"
        )
    elif confidence == "low":
        # Log edge cases with low confidence (might need review)
        push(
            f"⚠️ LOW CONFIDENCE: {category}\n"
            f"Message: {user_message[:100]}\n"
            f"Reason: {reasoning}"
        )


record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "The email address of this user"},
            "name": {"type": "string", "description": "The user's name, if they provided it"},
            "notes": {
                "type": "string",
                "description": "Any additional info about the conversation that's worth recording to give context",
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "The question that couldn't be answered"},
        },
        "required": ["question"],
        "additionalProperties": False,
    },
}

tools = [
    {"type": "function", "function": record_user_details_json},
    {"type": "function", "function": record_unknown_question_json},
]

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
}


def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)
        tool = tool_map.get(tool_name)
        result = tool(**arguments) if tool else "Unknown tool: " + tool_name
        results.append(
            {"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id}
        )
    return results
