# Digital Twin Agent - Implementation Roadmap

## Vision
Build a production-ready digital twin agent that gracefully handles career-related questions while filtering off-topic requests, with progressively sophisticated agentic patterns for scalability.

---

## Phase 1: Pre-flight Evaluation & Logging
**Goal:** Add message evaluation BEFORE generating response, with structured outputs and monitoring.

**Objectives:**
- Evaluate user input before main LLM call (cost/latency optimization)
- Use structured outputs for reliable evaluation (no text parsing)
- Gracefully handle off-topic questions
- Log all evaluations for monitoring and improvement

**Deliverables:**
- [x] Create `evaluator.py` - Evaluation logic with structured outputs
- [x] Create `handlers.py` - Separate handlers for on-topic vs off-topic flow
- [x] Update `app.py` - Integrate pre-flight evaluation into main chat loop
- [x] Extend Pushover logging - Track evaluation metrics (blocked questions, edge cases)
- [x] Add evaluation tests - Verify evaluator works on sample inputs

**Testing (Phase 1):**
- [x] Create `test_evaluator.py` - Standalone evaluation script with 13 test cases
- [x] Create `conftest.py` - Pytest fixtures for test data
- [x] Create `pytest.ini` - Pytest configuration with markers
- [x] Add example unit tests - `test_handlers_unit.py` with 2 basic tests

**Success Criteria:**
- Off-topic questions blocked before expensive LLM call
- Graceful refusal messages for off-topic requests
- All evaluation decisions logged to Pushover
- No false positives (legitimate career questions blocked)

---

## Phase 2: Enhanced Routing & Classification
**Goal:** Sophisticated question classification with nuanced handling.

**Objectives:**
- Classify questions into multiple categories (not just on/off-topic)
- Handle edge cases (greetings, clarifications, borderline questions)
- Different response strategies per category
- Track classification metrics

**Deliverables:**
- [ ] Create `router.py` - Question classification system
- [ ] Define question categories (career, greeting, clarification, off-topic, inappropriate)
- [ ] Implement category-specific handlers
- [ ] Add routing decision logging
- [ ] Create classification confidence scoring

**Testing (Phase 2):**
- [ ] Add unit tests with pytest markers (`@pytest.mark.unit`)
- [ ] Mock LLM calls in unit tests (using `pytest-mock`)
- [ ] Create integration tests for routing (`@pytest.mark.integration`)
- [ ] Add tests for confidence scoring logic
- [ ] Expand evaluation script with new categories
- [ ] Build golden dataset (20-30 sample questions with expected outcomes)

**Categories to Handle:**
- Career question → Full digital twin response
- Greeting/small talk → Brief friendly response
- Clarification needed → Ask follow-up
- Off-topic but salvageable → Redirect gracefully
- Completely off-topic → Polite refusal
- Inappropriate content → Safety response

---

## Phase 3: Telegram Integration
**Goal:** Deploy agent as a real-world Telegram bot for practical testing and usage.

**Objectives:**
- Create Telegram bot interface
- Integrate with existing evaluation and routing logic
- Test agent in real conversational context
- Enable broader access for friends/colleagues to interact with digital twin
- Gather real-world usage data

**Deliverables:**
- [ ] Create `telegram_bot.py` - Telegram bot implementation
- [ ] Set up Telegram Bot API integration
- [ ] Adapt chat interface for Telegram (message handling, formatting)
- [ ] Add Telegram-specific features:
  - [ ] Start command and welcome message
  - [ ] Help command
  - [ ] Conversation reset
  - [ ] Rich message formatting (Markdown/HTML)
- [ ] Deploy bot (local or cloud hosting)
- [ ] Test with real users
- [ ] Add Telegram-specific logging (track usage, popular questions)

**Benefits:**
- Real-world testing environment
- Async messaging (users can return to conversation)
- Rich formatting support
- Easy to share with others
- Natural conversational context
- Data collection for improvements

**Technical Considerations:**
- Use `python-telegram-bot` or similar library
- Handle async messaging
- Session management across conversations
- Rate limiting
- Error handling for network issues
- Graceful handling of media/files users might send

**Testing (Phase 3):**
- [ ] Add integration tests for Telegram bot (`test_telegram_integration.py`)
- [ ] Test message handling (text, commands, formatting)
- [ ] Test session management across conversations
- [ ] Test error handling and rate limiting
- [ ] Manual testing with real Telegram users (gather feedback)
- [ ] Track metrics: response time, error rate, user satisfaction

---

## Phase 4: Memory & Context Management
**Goal:** Add conversation memory and user journey tracking.

**Objectives:**
- Track conversation history per user
- Remember frequently asked topics
- Learn from edge cases (borderline questions)
- Personalize responses based on history
- Track user journey (first-time vs returning)

**Deliverables:**
- [ ] Create `memory.py` - Conversation state management
- [ ] Implement session tracking
- [ ] Add topic frequency analytics
- [ ] Build edge case learning system
- [ ] Create user journey tracking
- [ ] Add conversation summarization for long sessions

**Patterns to Explore:**
- Short-term memory (current session)
- Long-term memory (across sessions)
- Semantic memory (learned patterns)
- Episodic memory (specific conversations)

**Testing (Phase 4):**
- [ ] Add unit tests for memory storage/retrieval logic
- [ ] Test session tracking across multiple conversations
- [ ] Test memory persistence and cleanup
- [ ] Create evaluation tests for personalization quality
- [ ] Test edge case learning (does it improve over time?)
- [ ] Benchmark memory lookup performance

---

## Phase 5: Multi-Agent Coordinator Pattern
**Goal:** Implement sophisticated multi-agent architecture.

**Objectives:**
- Separate concerns into specialized agents
- Implement agent coordination logic
- Add agent-to-agent communication
- Optimize agent selection/routing

**Deliverables:**
- [ ] Create `coordinator.py` - Main agent coordinator
- [ ] Create specialized agents:
  - [ ] `evaluator_agent.py` - Question evaluation
  - [ ] `twin_agent.py` - Career question answering
  - [ ] `clarification_agent.py` - Handle ambiguous questions
  - [ ] `tools_agent.py` - Tool execution coordination
- [ ] Implement agent communication protocol
- [ ] Add agent performance monitoring
- [ ] Create agent selection strategy

**Architecture:**
```
User Input → Coordinator Agent
              ├─> Evaluator Agent (is this career-related?)
              ├─> Digital Twin Agent (answer career questions)
              ├─> Clarification Agent (handle ambiguous questions)
              └─> Tools Agent (email recording, question logging)
```

**Testing (Phase 5):**
- [ ] Add unit tests for coordinator logic
- [ ] Test agent communication protocol
- [ ] Test agent selection strategy (right agent for the job)
- [ ] Integration tests for full multi-agent flow
- [ ] Performance tests (latency, parallel execution)
- [ ] Test fallback behavior when agents fail
- [ ] Monitor and log agent performance metrics

---

## Phase 6: Guardrails & Validation
**Goal:** Add comprehensive safety, quality, and validation layers.

**Objectives:**
- Input validation (detect attacks, inappropriate content)
- Output validation (quality checks, fact verification)
- Safety guardrails (PII handling, professional tone)
- Evaluate alternative logging solutions

**Deliverables:**
- [ ] Create `guardrails.py` - Input/output validation
- [ ] Implement jailbreak detection
- [ ] Add PII detection/redaction
- [ ] Build output quality validator
- [ ] Add fact-checking against context
- [ ] Professional tone verification
- [ ] Research and evaluate logging alternatives:
  - [ ] Structured logging (JSON logs)
  - [ ] Application Performance Monitoring (APM) tools
  - [ ] Analytics platforms
  - [ ] Self-hosted solutions
- [ ] Implement chosen logging solution

**Safety Checks:**
- Prompt injection attempts
- Inappropriate content
- PII in user input
- PII in agent output
- Off-brand tone
- Factual accuracy

**Testing (Phase 6):**
- [ ] Add adversarial tests (jailbreak attempts, prompt injection)
- [ ] Test PII detection accuracy (unit tests with sample data)
- [ ] Test output quality validation
- [ ] Test fact-checking against LinkedIn profile
- [ ] Create security test suite (`test_security.py`)
- [ ] Build attack dataset for guardrail testing
- [ ] Measure false positive/negative rates for safety checks

---

## Phase 7: Production Scalability
**Goal:** Optimize for production deployment with advanced patterns.

**Objectives:**
- Performance optimization (caching, async)
- Enhanced retrieval (RAG, vector search)
- Model optimization (fine-tuning)
- A/B testing and experimentation
- Observability dashboard

**Deliverables:**
- [ ] Implement evaluation caching
- [ ] Add async processing for parallel operations
- [ ] Build RAG pipeline for career history
- [ ] Create vector search over LinkedIn/resume
- [ ] Set up prompt versioning system
- [ ] Implement A/B testing framework
- [ ] Build analytics dashboard
- [ ] Collect training data for fine-tuning
- [ ] Fine-tune custom evaluator model

**Optimization Areas:**
- Response latency
- Cost per interaction
- Evaluation accuracy
- User satisfaction
- Scalability (concurrent users)

**Testing (Phase 7):**
- [ ] Performance benchmarking suite
- [ ] Load testing (concurrent users, stress tests)
- [ ] Cache hit/miss rate testing
- [ ] A/B test framework validation
- [ ] RAG accuracy evaluation (retrieval quality)
- [ ] Regression testing suite (prevent quality degradation)
- [ ] End-to-end production simulation tests
- [ ] Set up CI/CD pipeline with automated testing

---

## Future Considerations
- Multi-modal support (resume uploads, voice)
- Integration with calendar/scheduling tools
- Real-time LinkedIn profile updates
- Multi-language support
- Additional messaging platforms (WhatsApp, Discord, Slack)
- API for integration with website
- Mobile app version
- Desktop widget/app

---

## Success Metrics (Across All Phases)

### Quality Metrics (Tested Throughout)
- **Accuracy:** % of questions correctly classified (measured in evaluation tests)
- **Precision:** % of blocked questions that were truly off-topic (minimize false positives)
- **Recall:** % of off-topic questions successfully blocked (minimize false negatives)
- **Confidence Distribution:** Track low/medium/high confidence classifications

### Performance Metrics (Tracked & Tested)
- **Latency:** Average response time (benchmarked in tests)
- **Cost:** Cost per interaction (tracked per phase)
- **Test Coverage:** % of code covered by tests
- **Test Pass Rate:** % of tests passing on each commit

### User Experience Metrics (Measured in Production)
- **User Satisfaction:** Feedback ratings from real users
- **Engagement:** Conversation length, return rate
- **Error Rate:** % of conversations with errors
- **Edge Cases Discovered:** Low-confidence or misclassified messages

---

## Notes

### Development Philosophy
- This is a Work In Progress - phases will evolve based on learnings
- Each phase builds on the previous, but can be adjusted as needed
- Focus on production-ready patterns that showcase agentic architecture
- Balance sophistication with maintainability

### Testing Philosophy
- **Test as you build:** Testing tasks are integrated into each phase
- Tests are written alongside features, not after
- Each phase adds tests for its own functionality
- Unit tests for logic, integration tests for flows, evaluation tests for quality
- Goal: Keep testing and app development in sync
- See [TESTING.md](TESTING.md) for detailed testing strategy
- See [TESTS_STATUS.md](TESTS_STATUS.md) for current test implementation status
