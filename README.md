# claude-learning

A learning project for building LLM applications with the Claude API.

## Requirements

- Python >= 3.9
- An [Anthropic API key](https://console.anthropic.com/)

## Setup

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install the package with dev dependencies
pip install -e ".[dev]"

# Configure your API key
cp .env.example .env
# then edit .env and set ANTHROPIC_API_KEY
```

## Project layout

```
src/claude_learning/   # package source
  __init__.py
  api.py               # Claude API client code
tests/                 # pytest test suite
```

## Development

```bash
pytest          # run tests
black .         # format code
ruff check .    # lint
mypy src        # type check
```

## Status

Early scaffold — package structure and tooling are set up; API client code is still being written.
