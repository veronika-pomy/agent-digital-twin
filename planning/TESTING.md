# Testing Strategy

This document explains the testing approach for the Digital Twin Agent project.

## Quick Start

```bash
# Install test dependencies
pip install pytest pytest-mock pytest-cov

# Run all tests
pytest

# Run only unit tests (fast, no API calls)
pytest -m unit

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_handlers_unit.py

# Run evaluation tests (slow, costs money)
python tests/test_evaluator.py
```

## Testing Philosophy for AI Agents

AI/agent testing is different from traditional software because:

1. **LLM outputs are non-deterministic** - same input can produce different outputs
2. **We need evaluation metrics, not just assertions** - "good enough" vs exact match
3. **Tests cost money** - every LLM call costs API credits
4. **Human review is essential** - edge cases need manual verification

## Test Types

### 1. Unit Tests (Fast, No API Calls)

**What:** Test deterministic logic without external dependencies  
**When:** Test utility functions, routing logic, data validation  
**Tools:** pytest, pytest-mock  
**Cost:** Free, fast  

**Example:**
```python
def test_should_process_normally(sample_career_evaluation):
    assert should_process_normally(sample_career_evaluation) == True
```

**Location:** `tests/test_*_unit.py`  
**Run with:** `pytest -m unit`

---

### 2. Integration Tests (Moderate Speed, Real APIs)

**What:** Test how components work together with real API calls  
**When:** Test the full evaluation pipeline  
**Tools:** pytest with real API keys  
**Cost:** $$ (API costs)

**Example:**
```python
@pytest.mark.integration
def test_evaluate_career_question():
    result = evaluate_message("What technologies do you work with?")
    assert result.category == "career_question"
    assert result.is_career_related == True
```

**Location:** `tests/test_*_integration.py`  
**Run with:** `pytest -m integration`

---

### 3. Evaluation Tests (Slow, Expensive, Fuzzy)

**What:** Test LLM behavior with sample inputs, grade quality  
**When:** Test response quality, classification accuracy  
**Tools:** Custom scripts, LLM-as-judge  
**Cost:** $$$ (multiple API calls per test)

**Example:**
```python
@pytest.mark.evaluation
def test_evaluator_accuracy():
    # Test with 50 sample messages
    # Check if accuracy > 90%
    # Report edge cases
```

**Current implementation:** `tests/test_evaluator.py` (standalone script)

**Location:** `tests/test_*_evaluation.py` or standalone scripts  
**Run with:** `pytest -m evaluation` or `python tests/test_evaluator.py`

---

### 4. Human-in-the-Loop (Continuous)

**What:** Manual review of edge cases and production behavior  
**When:** Low confidence classifications, blocked messages  
**Tools:** Pushover notifications (Phase 1), analytics dashboards (later)  
**Cost:** Time (human review)

**Current implementation:** 
- Pushover logging in `tools.py`
- Notifications for blocked messages
- Notifications for low confidence classifications

---

## Test Organization

```
tests/
├── __init__.py
├── conftest.py              # Pytest fixtures (shared test data)
├── pytest.ini               # Pytest configuration (moved to root)
│
├── test_*_unit.py           # Unit tests (fast, no API)
├── test_*_integration.py    # Integration tests (real API)
├── test_*_evaluation.py     # Evaluation tests (LLM grading)
│
├── fixtures/                # Test data
│   ├── sample_messages.json
│   └── golden_dataset.json
│
└── test_evaluator.py        # Legacy evaluation script
```

## Running Tests

### Development Workflow

```bash
# 1. Quick unit tests (every save)
pytest -m unit --tb=short

# 2. Integration tests (before commit)
pytest -m integration

# 3. Full suite (before push)
pytest

# 4. Evaluation tests (before deploy, manual)
python tests/test_evaluator.py
```

### CI/CD Strategy (Future)

```yaml
# .github/workflows/test.yml
on: [push, pull_request]

jobs:
  unit-tests:
    - pytest -m unit  # Run on every push
  
  integration-tests:
    - pytest -m integration  # Run on PR
  
  evaluation-tests:
    - pytest -m evaluation  # Run on main branch only
```

## Success/Failure Criteria

### Unit Tests
- **Pass:** Assertion passes
- **Fail:** Assertion fails, exception raised
- **Standard pytest behavior**

### Integration Tests
- **Pass:** Response matches expected category/type
- **Fail:** Wrong category, timeout, API error
- **Some tolerance for confidence levels**

### Evaluation Tests
- **Pass:** Accuracy > threshold (e.g., 90%)
- **Fail:** Accuracy < threshold, too many edge cases
- **Report confidence distribution**
- **Manual review of failures**

## What's Missing (Future Work)

1. **Mocking LLM calls** - Use `pytest-mock` to test without API costs
2. **Golden dataset** - Build dataset of expected behaviors
3. **LLM-as-judge** - Use GPT to grade responses
4. **Coverage tracking** - What questions/scenarios are tested?
5. **Performance benchmarks** - Track latency, cost per interaction
6. **Regression tests** - Prevent quality degradation
7. **A/B testing framework** - Test different prompts

## Recommended Next Steps

1. **Phase 1 (Now):**
   - Keep `test_evaluator.py` as-is for quick manual testing
   - Add basic pytest unit tests for deterministic logic

2. **Phase 2:**
   - Add pytest markers (unit, integration, evaluation)
   - Mock LLM calls in unit tests
   - Build golden dataset

3. **Phase 3:**
   - Implement LLM-as-judge evaluation
   - Add CI/CD integration
   - Track accuracy over time

4. **Phase 4+:**
   - A/B testing framework
   - Performance benchmarks
   - Automated regression detection

## Resources

- **pytest docs:** https://docs.pytest.org/
- **OpenAI Evals:** https://github.com/openai/evals
- **LangSmith:** https://docs.smith.langchain.com/
- **Testing LLM apps:** https://www.anthropic.com/index/evaluating-ai
