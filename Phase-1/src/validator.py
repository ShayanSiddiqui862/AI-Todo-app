"""
Input validation functions for the Todo CLI application.

Provides input sanitization and validation for task titles, descriptions,
and task IDs to ensure data integrity and prevent errors.
"""

import re
from typing import Union


def validate_task_title(title: str) -> str:
    """
    Validate and sanitize task title (1-200 characters).

    Args:
        title: Task title to validate

    Returns:
        Sanitized title string

    Raises:
        ValueError: If title doesn't meet requirements
    """
    if not title or not title.strip():
        raise ValueError("Task title is required and cannot be empty")

    sanitized_title = title.strip()

    if len(sanitized_title) < 1:
        raise ValueError("Task title is required and cannot be empty")

    if len(sanitized_title) > 200:
        raise ValueError(f"Task title exceeds maximum length of 200 characters. Current length: {len(sanitized_title)}")

    return sanitized_title


def validate_task_description(description: str) -> str:
    """
    Validate task description (max 1000 characters).

    Args:
        description: Task description to validate

    Returns:
        Sanitized description string

    Raises:
        ValueError: If description doesn't meet requirements
    """
    if not description:
        return ""

    sanitized_description = description.strip()

    if len(sanitized_description) > 1000:
        raise ValueError(f"Task description exceeds maximum length of 1000 characters. Current length: {len(sanitized_description)}")

    return sanitized_description


def validate_task_id(task_id_str: str, max_id: int = None) -> int:
    """
    Validate task ID is a positive integer within range.

    Args:
        task_id_str: String representation of task ID
        max_id: Maximum allowed ID (optional)

    Returns:
        Validated integer task ID

    Raises:
        ValueError: If task ID is invalid
    """
    if not task_id_str or not task_id_str.strip():
        raise ValueError("Task ID is required and cannot be empty")

    try:
        task_id = int(task_id_str.strip())
    except ValueError:
        raise ValueError(f"Task ID must be a valid integer. Provided: {task_id_str}")

    if task_id <= 0:
        raise ValueError(f"Task ID must be a positive integer. Provided: {task_id}")

    if max_id is not None and task_id > max_id:
        raise ValueError(f"Task ID {task_id} exceeds maximum allowed ID of {max_id}")

    return task_id


def is_valid_command(command: str) -> bool:
    """
    Validate if the command is recognized.

    Args:
        command: Command string to validate

    Returns:
        True if command is valid, False otherwise
    """
    valid_commands = {"add", "list", "update", "delete", "complete", "help", "exit"}
    return command.strip().lower() in valid_commands