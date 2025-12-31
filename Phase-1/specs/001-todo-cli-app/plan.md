# Implementation Plan: Todo In-Memory Python Console App

**Branch**: `001-todo-cli-app` | **Date**: 2025-12-30 | **Spec**: [specs/001-todo-cli-app/spec.md](/mnt/d/github/user1/AI-Todo-app/Phase-1/specs/001-todo-cli-app/spec.md)
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

## Summary

Implementation of a high-performance, in-memory CLI tool for personal task management using Python 3.13+ with UV as package manager. The application will provide command-line interface for task management (add, view, update, delete, mark complete) with data stored only in memory during the session, with no persistence to external databases or files.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard library only (datetime, sys, os, etc.)
**Storage**: In-memory using Python list of dictionaries
**Testing**: pytest for unit and integration tests
**Target Platform**: Cross-platform (Linux, macOS, Windows)
**Project Type**: Single CLI application
**Performance Goals**: <1 second response time per operation, handle up to 1000 tasks in memory
**Constraints**: <100MB memory usage, no external persistence, CLI-only interface
**Scale/Scope**: Single-user, session-based, up to 1000 tasks per session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Uses Python 3.13+ as required by constitution
- ✅ Uses in-memory storage (Python list/dict) with no external persistence
- ✅ Uses UV as package manager as required
- ✅ Source code will reside in /src folder as required
- ✅ Will implement graceful handling for invalid IDs and empty inputs
- ✅ Will follow PEP 8 standards and use type hinting
- ✅ No database connectors, web frameworks, or external persistence mechanisms

## Architecture Overview

The application will follow a modular, procedural approach with clear separation of concerns:

1. **Storage Manager**: Handles in-memory task storage using a list of dictionaries
2. **CLI Controller**: Main loop to capture user input and route commands
3. **Input Validator**: Utility functions to sanitize strings and validate task IDs
4. **View Renderer**: Component to format console output for task display

The architecture will be entirely in-memory using native Python data structures (list of dictionaries) as specified in the constitution, with no external dependencies beyond the Python standard library.

## Data Modeling

### Task Entity Schema

The Task entity will be represented as a dictionary with the following structure:

```python
{
    "id": int,              # Auto-incrementing unique identifier
    "title": str,          # 1-200 characters task title/description
    "description": str,    # Optional, max 1000 characters additional details
    "completed": bool,     # Boolean flag for completion status (default: False)
    "created_at": str      # ISO 8601 datetime string (e.g., "2025-12-30T10:30:00")
}
```

### Validation Rules

- `id`: Must be a positive integer, auto-incremented from the highest existing ID
- `title`: Required string between 1-200 characters, trimmed of leading/trailing whitespace
- `description`: Optional string, max 1000 characters if provided
- `completed`: Boolean value, defaults to False when creating new tasks
- `created_at`: ISO 8601 formatted datetime string, set at task creation time

## Component Breakdown

### 1. Storage Manager (`src/storage.py`)

Responsible for all in-memory data operations:
- `create_task(title: str, description: str = "") -> dict`: Creates a new task with auto-generated ID and timestamp
- `get_all_tasks() -> list`: Returns all tasks in the current session
- `get_task_by_id(task_id: int) -> dict`: Retrieves a specific task by ID
- `update_task(task_id: int, title: str = None, description: str = None, completed: bool = None) -> dict`: Updates task properties
- `delete_task(task_id: int) -> bool`: Removes a task by ID
- `clear_all_tasks() -> None`: Clears all tasks (used internally)

### 2. CLI Controller (`src/cli.py`)

Manages the main application loop and command routing:
- `main() -> None`: Entry point that initializes the app and starts the command loop
- `display_menu() -> None`: Shows available commands to the user
- `process_command(command: str) -> bool`: Processes user input and executes appropriate functions
- `handle_add_task() -> None`: Handles adding new tasks
- `handle_list_tasks() -> None`: Handles displaying all tasks
- `handle_update_task() -> None`: Handles updating existing tasks
- `handle_delete_task() -> None`: Handles deleting tasks
- `handle_mark_complete() -> None`: Handles marking tasks as complete/incomplete

### 3. Input Validator (`src/validator.py`)

Provides input sanitization and validation:
- `validate_task_title(title: str) -> str`: Validates and sanitizes task title (1-200 chars)
- `validate_task_description(description: str) -> str`: Validates task description (max 1000 chars)
- `validate_task_id(task_id: str, max_id: int) -> int`: Validates task ID is a positive integer within range
- `is_valid_command(command: str) -> bool`: Validates if the command is recognized

### 4. View Renderer (`src/renderer.py`)

Handles console output formatting:
- `render_task_list(tasks: list) -> str`: Formats and displays all tasks in a table format
- `render_task_detail(task: dict) -> str`: Displays detailed information for a single task
- `render_menu() -> str`: Displays the available commands menu
- `render_success_message(message: str) -> str`: Formats success feedback messages
- `render_error_message(message: str) -> str`: Formats error feedback messages

## Execution Flow

### CLI Session Lifecycle

1. **Initialization**:
   - Import necessary modules and initialize empty task list in memory
   - Display welcome message and available commands menu

2. **Command Processing Loop**:
   - Prompt user for input
   - Parse and validate the command
   - Route to appropriate handler function
   - Execute storage operation based on command
   - Display feedback/updated task list to user

3. **Command Handling**:
   - `add` - Prompt for title/description, validate, create task
   - `list` - Retrieve all tasks, format and display
   - `update` - Prompt for task ID and new values, validate and update
   - `delete` - Prompt for task ID, validate and delete
   - `complete` - Prompt for task ID, toggle completion status
   - `help` - Display available commands
   - `exit` - Break loop and terminate application

4. **Termination**:
   - Exit the while loop
   - Clear memory (Python garbage collection handles this)
   - Display exit message

## Error Handling Strategy

### Edge Cases from Specification

1. **Non-existent ID**:
   - Validate task ID exists before operations
   - Return "Error: Task ID not found." message

2. **Empty Input**:
   - Require title for 'Add Task' operations
   - Return "Error: Task title is required." message

3. **Non-Integer IDs**:
   - Validate input types before processing
   - Return "Error: Task ID must be a valid integer." message

### Additional Error Scenarios

4. **Invalid Commands**:
   - Validate command exists in the command registry
   - Return "Error: Unknown command. Type 'help' for available options." message

5. **Malformed Input**:
   - Validate input format before processing
   - Return specific error messages based on validation failures

6. **Boundary Conditions**:
   - Handle maximum character limits for titles/descriptions
   - Return appropriate error messages when limits are exceeded

## Implementation Strategy

### Python Standard Library Modules

- `datetime`: For creating ISO 8601 timestamps
- `sys`: For handling exit operations
- `os`: For environment-related operations if needed
- `re`: For input validation and pattern matching
- `typing`: For type hints (List, Dict, Optional, etc.)

### Project Structure

```text
src/
├── __init__.py
├── main.py              # Entry point, imports and runs CLI controller
├── storage.py           # In-memory storage manager
├── cli.py               # Main CLI controller and command router
├── validator.py         # Input validation functions
└── renderer.py          # Console output formatting
```

### Environment Management

- Use UV as package manager as required by constitution
- Create virtual environment with `uv venv`
- Install dependencies with `uv pip install` (though for this project, only standard library will be used)

### Development Approach

1. Start with data models and storage layer
2. Implement validation functions
3. Build CLI controller with command routing
4. Add view rendering functions
5. Integrate all components
6. Add comprehensive error handling
7. Test with various edge cases

## Project Structure

### Documentation (this feature)
```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
src/
├── main.py              # Application entry point
├── storage.py           # In-memory task storage manager
├── cli.py               # CLI controller and command processor
├── validator.py         # Input validation functions
└── renderer.py          # Console output formatter

tests/
├── unit/
│   ├── test_storage.py  # Unit tests for storage functions
│   ├── test_validator.py # Unit tests for validation functions
│   └── test_renderer.py # Unit tests for rendering functions
└── integration/
    └── test_cli_flow.py # Integration tests for CLI flow
```

**Structure Decision**: Single project structure selected as this is a CLI application with clear separation of concerns between storage, CLI interface, validation, and rendering components.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |