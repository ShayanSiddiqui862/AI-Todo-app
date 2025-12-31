# Todo In-Memory Python Console App

A command-line interface application for managing personal tasks in memory. The application provides basic task management functionality with no external persistence - all data is stored only in memory during the session.

## Features

- Add new tasks with titles and descriptions
- List all tasks with visual indicators for completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Help command for available options
- Input validation and error handling

## Commands

- `add` - Add a new task
- `list` - List all tasks
- `update` - Update an existing task
- `delete` - Delete a task
- `complete` - Mark a task as complete/incomplete
- `help` - Show available commands
- `exit` - Exit the application

## Project Structure

```
src/
├── main.py              # Application entry point
├── storage.py           # In-memory task storage manager
├── cli.py               # CLI controller and command processor
├── validator.py         # Input validation functions
├── renderer.py          # Console output formatter
└── __init__.py          # Package initialization

tests/
├── unit/
│   ├── test_storage.py  # Unit tests for storage functions
│   ├── test_validator.py # Unit tests for validation functions
│   └── test_renderer.py # Unit tests for rendering functions
└── integration/
    └── test_cli_flow.py # Integration tests for CLI flow
```

## Running the Application

```bash
python3 -m src.main
```

## Running Tests

```bash
python3 -m pytest tests/ -v
```

## Architecture

The application follows a modular, procedural approach with clear separation of concerns:

1. **Storage Manager**: Handles in-memory task storage using a list of dictionaries
2. **CLI Controller**: Main loop to capture user input and route commands
3. **Input Validator**: Utility functions to sanitize strings and validate task IDs
4. **View Renderer**: Component to format console output for task display