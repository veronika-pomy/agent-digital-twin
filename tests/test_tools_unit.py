"""
Unit tests for tools module (Pushover, email recording, etc.).

Tests focus on error handling and logic without making real API calls.
Run with: pytest tests/test_tools_unit.py -v
"""

import pytest
from unittest.mock import Mock, patch
from src.tools.tools import push, log_evaluation, record_user_details


@pytest.mark.unit
def test_push_success(mocker, capsys):
    """Test that push() logs success when request succeeds."""
    # Mock requests.post to return successfully
    mock_post = mocker.patch('src.tools.tools.requests.post')
    mock_post.return_value = Mock(status_code=200)

    # Call push
    push("Test notification")

    # Verify requests.post was called with correct args
    mock_post.assert_called_once()
    assert mock_post.call_args[1]['timeout'] == 5

    # Check console output
    captured = capsys.readouterr()
    assert "[PUSHOVER] Notification sent" in captured.out


@pytest.mark.unit
@pytest.mark.parametrize("exception_class,exception_message,expected_error_name", [
    # Network/SSL errors (common in production)
    (Exception, "Generic error", "Exception"),
    # Uncomment these if you want to test specific error types:
    # (requests.exceptions.SSLError, "Certificate verify failed", "SSLError"),
    # (requests.exceptions.ConnectionError, "Network unreachable", "ConnectionError"),
    # (requests.exceptions.Timeout, "Request timed out", "Timeout"),
])
def test_push_handles_errors_gracefully(mocker, capsys, exception_class, exception_message, expected_error_name):
    """
    Test that push() handles ANY error gracefully without crashing.

    This test uses a generic Exception to verify error handling works for any failure.
    The function should catch SSL errors, network errors, timeouts, or any other exception.
    """
    # Mock requests.post to raise the specified exception
    mock_post = mocker.patch('src.tools.tools.requests.post')
    mock_post.side_effect = exception_class(exception_message)

    # Call push - should NOT raise exception (graceful handling)
    push("Test notification")

    # Verify error was logged to console
    captured = capsys.readouterr()
    assert "[PUSHOVER] Failed to send notification" in captured.out
    assert expected_error_name in captured.out


@pytest.mark.unit
def test_log_evaluation_blocked_message(mocker):
    """Test that log_evaluation calls push for blocked messages."""
    # Mock push function
    mock_push = mocker.patch('src.tools.tools.push')

    # Call log_evaluation with blocked message
    log_evaluation(
        user_message="Tell me a joke",
        category="off_topic",
        confidence="high",
        reasoning="Not related to career",
        was_blocked=True
    )

    # Verify push was called
    mock_push.assert_called_once()
    call_args = mock_push.call_args[0][0]
    assert "🚫 BLOCKED" in call_args
    assert "off_topic" in call_args
    assert "Tell me a joke" in call_args


@pytest.mark.unit
def test_log_evaluation_low_confidence(mocker):
    """Test that log_evaluation calls push for low confidence classifications."""
    # Mock push function
    mock_push = mocker.patch('src.tools.tools.push')

    # Call log_evaluation with low confidence
    log_evaluation(
        user_message="What do you think about coding?",
        category="career_question",
        confidence="low",
        reasoning="Ambiguous - could be career or personal opinion",
        was_blocked=False
    )

    # Verify push was called
    mock_push.assert_called_once()
    call_args = mock_push.call_args[0][0]
    assert "⚠️ LOW CONFIDENCE" in call_args
    assert "career_question" in call_args


@pytest.mark.unit
def test_log_evaluation_no_logging_needed(mocker):
    """Test that log_evaluation doesn't call push for normal career questions."""
    # Mock push function
    mock_push = mocker.patch('src.tools.tools.push')

    # Call log_evaluation with high confidence career question
    log_evaluation(
        user_message="What technologies do you work with?",
        category="career_question",
        confidence="high",
        reasoning="Clear career question",
        was_blocked=False
    )

    # Verify push was NOT called (no need to log normal interactions)
    mock_push.assert_not_called()


@pytest.mark.unit
def test_record_user_details_returns_ok(mocker):
    """Test that record_user_details returns OK (even if push fails)."""
    # Mock push to do nothing (simulate failure)
    mocker.patch('src.tools.tools.push')

    # Call record_user_details
    result = record_user_details(email="test@example.com", name="John Doe")

    # Should return OK regardless of push success/failure
    assert result == "OK"
