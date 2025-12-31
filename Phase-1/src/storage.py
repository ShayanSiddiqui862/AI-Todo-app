"""
In-memory task storage manager.

Handles all in-memory data operations for the Todo CLI application.
Uses a list of dictionaries to store tasks during the session.
"""

from datetime import datetime
from typing import List, Dict, Optional


class StorageManager:
    """Manages in-memory task storage using a list of dictionaries."""

    def __init__(self):
        """Initialize empty task list."""
        self._tasks: List[Dict] = []
        self._next_id: int = 1

    def create_task(self, title: str, description: str = "") -> Dict:
        """
        Create a new task with auto-generated ID and timestamp.

        Args:
            title: Task title (1-200 characters)
            description: Optional task description (max 1000 characters)

        Returns:
            Dictionary representing the created task
        """
        task = {
            "id": self._next_id,
            "title": title.strip(),
            "description": description.strip() if description else "",
            "completed": False,
            "created_at": datetime.now().isoformat()
        }

        self._tasks.append(task)
        self._next_id += 1

        return task

    def get_all_tasks(self) -> List[Dict]:
        """
        Return all tasks in the current session.

        Returns:
            List of all task dictionaries
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Dict]:
        """
        Retrieve a specific task by ID.

        Args:
            task_id: Unique identifier of the task

        Returns:
            Task dictionary if found, None otherwise
        """
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None, completed: bool = None) -> Optional[Dict]:
        """
        Update task properties.

        Args:
            task_id: Unique identifier of the task to update
            title: New title (optional)
            description: New description (optional)
            completed: New completion status (optional)

        Returns:
            Updated task dictionary if found, None otherwise
        """
        for task in self._tasks:
            if task["id"] == task_id:
                if title is not None:
                    task["title"] = title.strip()
                if description is not None:
                    task["description"] = description.strip()
                if completed is not None:
                    task["completed"] = completed
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task by ID.

        Args:
            task_id: Unique identifier of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        for i, task in enumerate(self._tasks):
            if task["id"] == task_id:
                del self._tasks[i]
                return True
        return False

    def clear_all_tasks(self) -> None:
        """Clear all tasks from memory."""
        self._tasks.clear()
        self._next_id = 1


# Global storage instance for the session
storage_manager = StorageManager()