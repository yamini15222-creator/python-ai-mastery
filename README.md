# Python AI Mastery

A structured Python project for learning and building reliable AI-focused applications through practical exercises, validation, testing, and professional development workflows.

## Problem

AI applications need more than model code. They also require reliable input validation, structured data handling, testing, documentation, and safe development practices.

This project focuses on building those software engineering foundations while developing AI-related functionality step by step.

## Solution

The project organizes Python learning and AI exercises into reusable modules and tests.

The Day 8–9 feature validates a learner's topic and AI settings before creating a structured request. It prevents empty topics and invalid token limits, making future AI features safer and more reliable.

## Architecture

```text
User Input
    ↓
Validation
    ↓
Structured Request
    ↓
AI Feature
    ↓
Result
    ↓
Tests & Evaluation
```

### Main Components

- `ai_core/` — Core AI-related modules
- `tests/` — Automated tests
- `lessons/` — Learning exercises
- `data/` — Project data
- `main.py` — Main application entry point
- `hello_ai.py` — Python/AI practice
- `pytest.ini` — Pytest configuration

## Validation

The project validates important inputs before processing them.

Examples include:

- Topic must not be empty.
- Token limits must be valid.
- Structured requests should contain the expected information.
- Invalid input should produce meaningful errors.

## Testing

Tests are implemented using `pytest`.

Run the test suite with:

```bash
pytest -q
```

## Code Quality

Ruff is used for Python linting and code-quality checks.

Run:

```bash
ruff check .
```

## Security

Sensitive files should not be committed to Git.

The `.gitignore` protects:

```text
.venv/
.env
__pycache__/
.ipynb_checkpoints/
data/private/
```

API keys, passwords, tokens, and private user information should never be stored directly in source code or committed to the repository.

## Limitations

AI systems can produce incorrect or incomplete results. This project does not assume that an AI model is always correct. Validation, testing, error handling, and human review remain important.

## Next Feature

The next feature can extend the validated request into an AI-powered workflow while preserving input validation, testing, and safe handling of sensitive information.

## Development Workflow

```text
Requirements
    ↓
Acceptance Criteria
    ↓
Technical Design
    ↓
Implementation
    ↓
Tests
    ↓
Documentation
    ↓
Code Review
    ↓
Release
```

## Author

Python AI Mastery Project