"""
Test suite for the evaluator module.

Prerequisites:
1. Ensure you have all dependencies installed:
   pip install openai python-dotenv pydantic

2. Ensure your .env file has OPENAI_API_KEY set

Run with: python test_evaluator.py
"""

from evaluator import evaluate_message, should_process_normally

# Test cases covering different message categories
TEST_CASES = [
    # Career questions - should process normally
    {
        "message": "What technologies do you work with?",
        "expected_category": "career_question",
        "should_process": True,
    },
    {
        "message": "Tell me about your experience at Penguin Random House",
        "expected_category": "career_question",
        "should_process": True,
    },
    {
        "message": "What programming languages do you know?",
        "expected_category": "career_question",
        "should_process": True,
    },
    {
        "message": "Can you describe your background?",
        "expected_category": "career_question",
        "should_process": True,
    },
    # Greetings - brief response, don't process normally
    {
        "message": "Hi there!",
        "expected_category": "greeting",
        "should_process": False,
    },
    {
        "message": "Hello, how are you?",
        "expected_category": "greeting",
        "should_process": False,
    },
    {
        "message": "Good morning!",
        "expected_category": "greeting",
        "should_process": False,
    },
    # Off-topic questions - should refuse
    {
        "message": "What's the weather like today?",
        "expected_category": "off_topic",
        "should_process": False,
    },
    {
        "message": "Do you like pizza?",
        "expected_category": "off_topic",
        "should_process": False,
    },
    {
        "message": "What's the capital of France?",
        "expected_category": "off_topic",
        "should_process": False,
    },
    {
        "message": "Tell me a joke",
        "expected_category": "off_topic",
        "should_process": False,
    },
    # Edge cases
    {
        "message": "What do you do in your free time?",
        "expected_category": "off_topic",  # Unless hobbies are in profile
        "should_process": False,
    },
]


def run_tests():
    """Run all test cases and report results."""
    print("=" * 70)
    print("EVALUATOR TEST SUITE")
    print("=" * 70)

    passed = 0
    failed = 0
    edge_cases = []

    for i, test_case in enumerate(TEST_CASES, 1):
        message = test_case["message"]
        expected_category = test_case["expected_category"]
        expected_process = test_case["should_process"]

        print(f"\n[Test {i}] Message: {message}")

        # Run evaluation
        result = evaluate_message(message)
        actual_process = should_process_normally(result)

        # Check results
        category_match = result.category == expected_category
        process_match = actual_process == expected_process

        print(f"  Expected: {expected_category} | Process: {expected_process}")
        print(f"  Actual:   {result.category} | Process: {actual_process}")
        print(f"  Confidence: {result.confidence}")
        print(f"  Reasoning: {result.reasoning}")

        if category_match and process_match:
            print("  ✅ PASSED")
            passed += 1
        else:
            print("  ❌ FAILED")
            if not category_match:
                print(f"     Category mismatch: expected {expected_category}, got {result.category}")
            if not process_match:
                print(f"     Processing mismatch: expected {expected_process}, got {actual_process}")
            failed += 1

        # Track edge cases (low confidence)
        if result.confidence == "low":
            edge_cases.append((message, result))

    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total tests: {len(TEST_CASES)}")
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    print(f"Edge cases (low confidence): {len(edge_cases)} ⚠️")

    if edge_cases:
        print("\nEDGE CASES (Review these):")
        for msg, result in edge_cases:
            print(f"  - {msg}")
            print(f"    Category: {result.category}, Reasoning: {result.reasoning}")

    print("\n" + "=" * 70)

    return passed, failed, edge_cases


if __name__ == "__main__":
    run_tests()
