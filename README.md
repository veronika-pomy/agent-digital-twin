# Digital Twin Agent

An AI-powered digital twin that answers questions about your professional career, background, and experience.

## Features (Phase 1 Complete)

- 🤖 **Pre-flight message evaluation** - Classifies messages before expensive LLM calls
- 📧 **Email collection** - Records interested users for follow-ups
- 📱 **Pushover monitoring** - Notifications for blocked/edge-case messages
- 🎨 **Gradio web interface** - Clean, accessible chat interface
- 🧪 **Evaluation testing** - 13 test cases for classification accuracy

## Quick Start

### 1. Setup

```bash
# Run setup script (creates venv, installs dependencies)
./scripts/setup.sh

# Or manually:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your keys:
# - OPENAI_API_KEY
# - PUSHOVER_USER
# - PUSHOVER_TOKEN
```

### 3. Add Your Profile

Replace these files with your own:
- `data/linkedin.pdf` - Export your LinkedIn profile
- `data/summary.txt` - Write a brief personal summary

### 4. Run

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the app
python app.py
```

Open http://localhost:7860 in your browser.

## Project Structure

```
agent-digital-twin/
├── src/                    # Source code
│   ├── agent/             # Core agent logic (evaluator, handlers)
│   ├── tools/             # Agent tools (email, logging)
│   ├── context/           # System prompts and data loading
│   └── ui/                # Gradio interface and styling
├── tests/                 # Test suite
├── data/                  # Profile data (LinkedIn, summary)
├── planning/              # Roadmap and documentation
├── scripts/               # Setup and utility scripts
└── app.py                 # Main entry point
```

See [planning/STRUCTURE.md](planning/STRUCTURE.md) for detailed structure documentation.

## Development

### Testing

**Currently Available:**

```bash
# Run evaluation script (13 test cases - makes real API calls)
python tests/test_evaluator.py

# Run example pytest tests (2 simple tests)
pytest tests/test_handlers_unit.py
```

**Full Test Suite (Coming in Phase 2+):**
- Unit tests with mocks
- Integration tests  
- Pytest markers for filtering
- Code coverage reporting

See [planning/TESTING.md](planning/TESTING.md) for complete testing strategy and [planning/TESTS_STATUS.md](planning/TESTS_STATUS.md) for current implementation status.

### Virtual Environment

```bash
# Activate (you'll need to do this every time you open a new terminal)
source .venv/bin/activate

# Deactivate
deactivate

# Update dependencies
pip install -r requirements.txt
```

## Roadmap

See [planning/ROADMAP.md](planning/ROADMAP.md) for the complete implementation plan:

- ✅ **Phase 1**: Pre-flight evaluation & logging
- 🔄 **Phase 2**: Enhanced routing & classification
- 📋 **Phase 3**: Telegram integration
- 📋 **Phase 4**: Memory & context management
- 📋 **Phase 5**: Multi-agent coordinator
- 📋 **Phase 6**: Guardrails & validation
- 📋 **Phase 7**: Production scalability

## Architecture Highlights

- **Pre-flight evaluation**: Messages are evaluated BEFORE expensive LLM calls
- **Structured outputs**: Uses Pydantic models for reliable classification
- **Separation of concerns**: Clean module organization
- **Monitoring**: Pushover notifications for edge cases and blocked content
- **Scalable**: Enterprise-ready structure for future growth

## License

MIT
