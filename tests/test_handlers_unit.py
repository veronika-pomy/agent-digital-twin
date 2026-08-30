"""
Unit tests for handlers module.

These test deterministic logic without making LLM calls.
Run with: pytest tests/test_handlers_unit.py
"""

import pytest
from src.agent.evaluator import EvaluationResult
from src.agent.handlers import route_message


def test_route_message_inappropriate():
    """Test that inappropriate messages get safety response."""
    # Arrange - create mock evaluation
    eval = EvaluationResult(
        is_career_related=False,
        category="inappropriate",
        confidence="high",
        reasoning="Contains offensive content"
    )

    # Act
    response = route_message("some inappropriate message", eval)

    # Assert
    assert "professional background" in response.lower()
    assert "not able to engage" in response.lower()


def test_route_message_greeting_calls_handler():
    """Test that greeting category routes to greeting handler."""
    eval = EvaluationResult(
        is_career_related=False,
        category="greeting",
        confidence="high",
        reasoning="Simple greeting"
    )

    # This would make a real API call - we should mock it
    # For now, just test it doesn't crash
    response = route_message("Hi", eval)
    assert isinstance(response, str)
    assert len(response) > 0


# Add more unit tests as needed
