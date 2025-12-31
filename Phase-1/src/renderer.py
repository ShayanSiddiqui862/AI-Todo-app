"""
Console output formatter for the Todo CLI application.

Handles formatting and display of tasks, menus, and feedback messages
to provide a consistent user interface in the terminal.
"""

from typing import List, Dict
from datetime import datetime


def render_task_list(tasks: List[Dict]) -> str:
    """
    Format and display all tasks in a table format.

    Args:
        tasks: List of task dictionaries to display

    Returns:
        Formatted string representation of tasks
    """
    if not tasks:
        return "No tasks found. Add a task using 'add' command."

    # Calculate column widths
    max_id_len = max(len(str(task["id"])) for task in tasks)
    max_id_len = max(max_id_len, len("ID"))

    # Create header
    header = f"{'ID':>{max_id_len}} | Status | Title"
    separator = f"{'-' * max_id_len}-|--------|------"

    lines = [header, separator]

    for task in tasks:
        status = "✓" if task["completed"] else "○"
        title = task["title"]
        line = f"{task['id']:>{max_id_len}} | {status:6} | {title}"
        lines.append(line)

    return "\n".join(lines)


def render_task_detail(task: Dict) -> str:
    """
    Display detailed information for a single task.

    Args:
        task: Task dictionary to display

    Returns:
        Formatted string representation of a single task
    """
    status = "Completed" if task["completed"] else "Pending"
    created_at = task["created_at"]

    # Parse the datetime string to make it more readable
    try:
        dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        formatted_date = created_at

    detail = f"""
Task Details:
ID:          {task['id']}
Title:       {task['title']}
Description: {task['description'] if task['description'] else '[No description]'}
Status:      {status}
Created:     {formatted_date}
    """.strip()

    return detail


def render_menu() -> str:
    """
    Display the available commands menu.

    Returns:
        Formatted string representation of available commands
    """
    menu = """
Available Commands:
  add      - Add a new task
  list     - List all tasks
  update   - Update an existing task
  delete   - Delete a task
  complete - Mark a task as complete/incomplete
  help     - Show this menu
  exit     - Exit the application
    """.strip()

    return menu


def render_success_message(message: str) -> str:
    """
    Format success feedback messages.

    Args:
        message: Success message to format

    Returns:
        Formatted success message
    """
    return f"✓ {message}"


def render_error_message(message: str) -> str:
    """
    Format error feedback messages.

    Args:
        message: Error message to format

    Returns:
        Formatted error message
    """
    return f"✗ Error: {message}"