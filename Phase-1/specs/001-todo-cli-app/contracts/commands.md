# Command Contracts: Todo In-Memory Python Console App

## Overview

This document defines the command-line interface contracts for the Todo CLI application. These contracts specify the expected input format, output format, and behavior for each command.

## Command Structure

All commands follow the format: `[command] [arguments]` where arguments are space-separated.

## Command Definitions

### 1. ADD Command

**Command**: `add`

**Description**: Adds a new task to the in-memory list

**Input Format**:
```
add "task title" ["optional description"]
```

**Parameters**:
- `task title`: Required string (1-200 characters)
- `optional description`: Optional string (max 1000 characters)

**Output Format**:
```
Task added successfully!
ID: {id}
Title: {title}
Description: {description}
Status: Incomplete
Created: {timestamp}
```

**Success Response**:
- Status: Success
- Code: 200
- Message: Task created with assigned ID

**Error Responses**:
- Empty title: "Error: Task title is required (1-200 characters)"
- Title too long: "Error: Task title exceeds 200 character limit"
- Description too long: "Error: Task description exceeds 1000 character limit"

### 2. LIST Command

**Command**: `list`

**Description**: Lists all tasks in the current session

**Input Format**:
```
list
```

**Parameters**: None

**Output Format**:
```
Current Tasks:
┌────┬────────────────────┬─────────────┬─────────────┐
│ ID │ Title              │ Description │ Status      │
├────┼────────────────────┼─────────────┼─────────────┤
│ 1  │ Sample Task        │ Description │ Incomplete  │
│ 2  │ Another Task       │ Details     │ Complete    │
└────┴────────────────────┴─────────────┴─────────────┘
```

**Success Response**:
- Status: Success
- Code: 200
- Message: List of all tasks formatted in table

**Error Responses**:
- No tasks: "No tasks found. Add tasks using 'add' command."

### 3. UPDATE Command

**Command**: `update`

**Description**: Updates an existing task

**Input Format**:
```
update {id} ["new title"] ["new description"]
```

**Parameters**:
- `id`: Required integer (task identifier)
- `new title`: Optional string (1-200 characters)
- `new description`: Optional string (max 1000 characters)

**Output Format**:
```
Task updated successfully!
ID: {id}
Title: {updated_title}
Description: {updated_description}
```

**Success Response**:
- Status: Success
- Code: 200
- Message: Task updated successfully

**Error Responses**:
- Invalid ID: "Error: Task ID must be a valid integer"
- ID not found: "Error: Task ID {id} not found"
- Title too long: "Error: Task title exceeds 200 character limit"
- Description too long: "Error: Task description exceeds 1000 character limit"

### 4. DELETE Command

**Command**: `delete`

**Description**: Deletes a task from the in-memory list

**Input Format**:
```
delete {id}
```

**Parameters**:
- `id`: Required integer (task identifier)

**Output Format**:
```
Task deleted successfully!
ID: {id}
Title: {title}
```

**Success Response**:
- Status: Success
- Code: 200
- Message: Task deleted successfully

**Error Responses**:
- Invalid ID: "Error: Task ID must be a valid integer"
- ID not found: "Error: Task ID {id} not found"

### 5. COMPLETE Command

**Command**: `complete`

**Description**: Marks a task as complete or incomplete

**Input Format**:
```
complete {id} [status]
```

**Parameters**:
- `id`: Required integer (task identifier)
- `status`: Optional boolean ("true"/"false" or "complete"/"incomplete")

**Output Format**:
```
Task status updated!
ID: {id}
Title: {title}
Status: {Complete/Incomplete}
```

**Success Response**:
- Status: Success
- Code: 200
- Message: Task status updated successfully

**Error Responses**:
- Invalid ID: "Error: Task ID must be a valid integer"
- ID not found: "Error: Task ID {id} not found"
- Invalid status: "Error: Status must be 'true', 'false', 'complete', or 'incomplete'"

### 6. HELP Command

**Command**: `help`

**Description**: Displays available commands and their usage

**Input Format**:
```
help
```

**Parameters**: None

**Output Format**:
```
Todo CLI Application - Available Commands:

add "title" ["description"]     - Add a new task
list                           - List all tasks
update {id} ["title"] ["desc"] - Update a task
delete {id}                    - Delete a task
complete {id} ["status"]       - Mark task complete/incomplete
help                           - Show this help message
exit                           - Exit the application

Examples:
  add "Buy groceries" "Milk, bread, eggs"
  list
  update 1 "Updated title"
  delete 1
  complete 1 true
```

**Success Response**:
- Status: Success
- Code: 200
- Message: Help text displayed

### 7. EXIT Command

**Command**: `exit`

**Description**: Exits the application and clears all in-memory data

**Input Format**:
```
exit
```

**Parameters**: None

**Output Format**:
```
Exiting Todo CLI Application...
All tasks have been cleared from memory.
Goodbye!
```

**Success Response**:
- Status: Success
- Code: 200
- Message: Application terminated successfully

## Error Contract

### Standard Error Format
```
Error: {detailed error message}
```

### Error Codes
- 400: Bad Request (invalid input format)
- 404: Not Found (task ID does not exist)
- 422: Unprocessable Entity (validation failed)
- 500: Internal Server Error (application error)

## Session Contract

### Session Lifecycle
1. Application starts with empty task list
2. All operations affect only in-memory data
3. Data persists only for the duration of the session
4. All data is cleared when application exits
5. No data persists between sessions

### Memory Management
- Application must handle up to 1000 tasks in memory
- Performance should remain under 1 second per operation
- Memory usage should not exceed 100MB for typical usage