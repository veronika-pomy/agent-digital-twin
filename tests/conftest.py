"""
Pytest configuration and shared fixtures.

This file is automatically loaded by pytest.
"""

import pytest


@pytest.fixture
def sample_career_evaluation():
    """Sample evaluation result for a career question."""
    from src.agent.evaluator import EvaluationResult
    return EvaluationResult(
        is_career_related=True,
        category="career_question",
        confidence="high",
        reasoning="Question about work experience"
    )


@pytest.fixture
def sample_off_topic_evaluation():
    """Sample evaluation result for an off-topic question."""
    from src.agent.evaluator import EvaluationResult
    return EvaluationResult(
        is_career_related=False,
        category="off_topic",
        confidence="high",
        reasoning="Not related to career"
    )


# Add more fixtures as needed
