from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls, log_evaluation
from styles import CSS, JS, EXAMPLES
from evaluator import evaluate_message, should_process_normally
from handlers import route_message
from dotenv import load_dotenv
import os
from pathlib import Path
import gradio as gr

ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR / ".env", override=True)

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5.4-mini")

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    # Pre-flight evaluation: check if message is career-related BEFORE expensive LLM call
    evaluation = evaluate_message(message)

    # Console logging for debugging
    print(f"[EVAL] Category: {evaluation.category}, Confidence: {evaluation.confidence}")
    print(f"[EVAL] Reasoning: {evaluation.reasoning}")

    # If message needs special handling (greeting, off-topic, inappropriate)
    if not should_process_normally(evaluation):
        # Log blocked/special-handled messages to Pushover
        was_blocked = evaluation.category in ["off_topic", "inappropriate"]
        log_evaluation(
            message,
            evaluation.category,
            evaluation.confidence,
            evaluation.reasoning,
            was_blocked=was_blocked,
        )
        response = route_message(message, evaluation)
        return response

    # Log edge cases (low confidence on career questions)
    if evaluation.confidence == "low":
        log_evaluation(
            message,
            evaluation.category,
            evaluation.confidence,
            evaluation.reasoning,
            was_blocked=False,
        )

    # Normal processing for career-related questions
    messages = system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())
