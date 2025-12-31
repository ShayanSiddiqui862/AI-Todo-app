# Data Model: Todo In-Memory Python Console App

## Entity: Task

### Schema Definition

```python
{
    "id": int,              # Auto-incrementing unique identifier (required)
    "title": str,           # 1-200 characters task title (required)
    "description": str,     # Optional, max 1000 characters additional details (optional, default: "")
    "completed": bool,      # Boolean flag for completion status (required, default: False)
    "created_at": str       # ISO 8601 datetime string (required)
}
```

### Field Specifications

| Field | Type | Required | Constraints | Default | Description |
|-------|------|----------|-------------|---------|-------------|
| id | int | Yes | Positive integer, auto-incremented | N/A | Unique identifier for the task |
| title | str | Yes | 1-200 characters, trimmed | N/A | Brief description/title of the task |
| description | str | No | Max 1000 characters | "" | Detailed description of the task |
| completed | bool | Yes | Boolean value | False | Completion status of the task |
| created_at | str | Yes | ISO 8601 format | N/A | Timestamp when task was created |

### Validation Rules

1. **id**:
   - Must be a positive integer
   - Auto-incremented from the highest existing ID in the system
   - Cannot be modified after creation

2. **title**:
   - Required field with 1-200 character limit
   - Trimmed of leading/trailing whitespace
   - Cannot be empty or contain only whitespace

3. **description**:
   - Optional field with max 1000 character limit
   - If provided, trimmed of leading/trailing whitespace
   - Default to empty string if not provided

4. **completed**:
   - Boolean value representing task completion status
   - Default to False when creating new tasks
   - Can be updated to True or False

5. **created_at**:
   - ISO 8601 formatted datetime string (e.g., "2025-12-30T10:30:00")
   - Set automatically at task creation time
   - Cannot be modified after creation

### Example Task Object

```python
{
    "id": 1,
    "title": "Implement user authentication",
    "description": "Create login and registration functionality with password hashing",
    "completed": False,
    "created_at": "2025-12-30T10:30:00"
}
```

## Entity: CLI Session

### Schema Definition

```python
{
    "session_id": str,          # Unique session identifier (UUID)
    "start_time": str,          # ISO 8601 datetime when session started
    "tasks": list,              # List of Task objects in current session
    "active": bool              # Boolean indicating if session is active
}
```

### Field Specifications

| Field | Type | Required | Constraints | Default | Description |
|-------|------|----------|-------------|---------|-------------|
| session_id | str | Yes | UUID format | N/A | Unique identifier for the session |
| start_time | str | Yes | ISO 8601 format | N/A | Timestamp when session started |
| tasks | list | Yes | List of Task objects | [] | Collection of tasks in current session |
| active | bool | Yes | Boolean value | True | Session active status |

### Validation Rules

1. **session_id**:
   - Must be a valid UUID string
   - Generated automatically when session starts

2. **start_time**:
   - ISO 8601 formatted datetime string
   - Set automatically when session starts

3. **tasks**:
   - Must be a list containing valid Task objects
   - Initially empty when session starts

4. **active**:
   - Boolean value indicating session status
   - True when session is active, False when terminated

## State Transitions

### Task State Transitions

```
CREATED (completed: False)
    ↓
MARKED_COMPLETE (completed: True)
    ↓
MARKED_INCOMPLETE (completed: False)
```

### Session State Transitions

```
STARTED (active: True)
    ↓
ACTIVE (active: True)
    ↓
TERMINATED (active: False)
```

## Relationships

### Task to Session
- Each Task belongs to exactly one CLI Session
- Tasks exist only within the context of their session
- When session terminates, all tasks are cleared from memory

## Constraints

1. **In-Memory Only**: All data exists only during the current session and is cleared when the application exits
2. **No External Persistence**: Tasks cannot be saved to files, databases, or external storage
3. **Session Isolation**: Tasks from different sessions do not persist or interact
4. **Character Limits**: Title (1-200 chars), Description (max 1000 chars)
5. **ID Uniqueness**: Each task ID must be unique within the current session