"""
Unit tests for storage functions in the Todo CLI application.

Tests all storage operations: create, read, update, delete tasks.
"""
import pytest
from datetime import datetime
from src.storage import StorageManager


class TestStorageManager:
    """Test cases for the StorageManager class."""

    def setup_method(self):
        """Set up a fresh StorageManager instance for each test."""
        self.storage = StorageManager()

    def test_create_task(self):
        """Test creating a new task."""
        title = "Test Task"
        description = "Test Description"

        task = self.storage.create_task(title, description)

        assert task["id"] == 1
        assert task["title"] == title
        assert task["description"] == description
        assert task["completed"] is False
        assert "created_at" in task

        # Verify datetime format
        datetime.fromisoformat(task["created_at"])

    def test_create_task_without_description(self):
        """Test creating a task without description."""
        title = "Test Task"

        task = self.storage.create_task(title)

        assert task["id"] == 1
        assert task["title"] == title
        assert task["description"] == ""
        assert task["completed"] is False

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when none exist."""
        tasks = self.storage.get_all_tasks()

        assert tasks == []

    def test_get_all_tasks_with_data(self):
        """Test getting all tasks when some exist."""
        self.storage.create_task("Task 1", "Description 1")
        self.storage.create_task("Task 2", "Description 2")

        tasks = self.storage.get_all_tasks()

        assert len(tasks) == 2
        assert tasks[0]["title"] == "Task 1"
        assert tasks[1]["title"] == "Task 2"

    def test_get_task_by_id_found(self):
        """Test getting a task by ID when it exists."""
        self.storage.create_task("Test Task", "Description")
        task_id = 1

        task = self.storage.get_task_by_id(task_id)

        assert task is not None
        assert task["id"] == task_id
        assert task["title"] == "Test Task"

    def test_get_task_by_id_not_found(self):
        """Test getting a task by ID when it doesn't exist."""
        task = self.storage.get_task_by_id(999)

        assert task is None

    def test_update_task_title(self):
        """Test updating a task's title."""
        self.storage.create_task("Old Title", "Description")
        task_id = 1
        new_title = "New Title"

        updated_task = self.storage.update_task(task_id, title=new_title)

        assert updated_task is not None
        assert updated_task["title"] == new_title
        assert updated_task["description"] == "Description"

    def test_update_task_description(self):
        """Test updating a task's description."""
        self.storage.create_task("Title", "Old Description")
        task_id = 1
        new_description = "New Description"

        updated_task = self.storage.update_task(task_id, description=new_description)

        assert updated_task is not None
        assert updated_task["title"] == "Title"
        assert updated_task["description"] == new_description

    def test_update_task_completed(self):
        """Test updating a task's completion status."""
        self.storage.create_task("Title", "Description")
        task_id = 1

        updated_task = self.storage.update_task(task_id, completed=True)

        assert updated_task is not None
        assert updated_task["completed"] is True

    def test_update_task_multiple_fields(self):
        """Test updating multiple fields of a task."""
        self.storage.create_task("Old Title", "Old Description")
        task_id = 1

        updated_task = self.storage.update_task(
            task_id,
            title="New Title",
            description="New Description",
            completed=True
        )

        assert updated_task is not None
        assert updated_task["title"] == "New Title"
        assert updated_task["description"] == "New Description"
        assert updated_task["completed"] is True

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist."""
        result = self.storage.update_task(999, title="New Title")

        assert result is None

    def test_delete_task_success(self):
        """Test deleting a task that exists."""
        self.storage.create_task("Test Task", "Description")
        task_id = 1

        result = self.storage.delete_task(task_id)

        assert result is True

        # Verify task is gone
        task = self.storage.get_task_by_id(task_id)
        assert task is None

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist."""
        result = self.storage.delete_task(999)

        assert result is False

    def test_auto_increment_id(self):
        """Test that task IDs are auto-incremented."""
        task1 = self.storage.create_task("Task 1")
        task2 = self.storage.create_task("Task 2")
        task3 = self.storage.create_task("Task 3")

        assert task1["id"] == 1
        assert task2["id"] == 2
        assert task3["id"] == 3

    def test_clear_all_tasks(self):
        """Test clearing all tasks."""
        self.storage.create_task("Task 1")
        self.storage.create_task("Task 2")

        self.storage.clear_all_tasks()

        tasks = self.storage.get_all_tasks()
        assert tasks == []