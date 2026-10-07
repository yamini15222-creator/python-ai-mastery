# Python AI Mastery

A hands-on Python and AI engineering learning project.

## Current Project

Modular AI Learning Request Builder.

The application validates learner input and model settings, then creates a
structured LLM request. It does not call a real LLM yet.

## Features

- Validates topic and learner level
- Validates temperature and token limits
- Builds structured AI request dictionaries
- Uses modular project architecture
- Includes pytest tests
- Uses Ruff for code-quality checks

## Architecture

```text
ai_core/
├── config.py           # Model configuration validation
├── prompt_builder.py   # Prompt construction
├── request_service.py  # Request orchestration
├── agent_state.py      # Agent memory/state
└── conversation_store.py # JSON persistence