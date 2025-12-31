"""
Unit tests for rendering functions in the Todo CLI application.

Tests all rendering functions: task list, task detail, menu, success/error messages.
"""
from src.renderer import render_task_list, render_task_detail, render_menu, render_success_message, render_error_message


class TestRenderTaskList:
    """Test cases for render_task_list function."""

    def test_empty_task_list(self):
        """Test rendering an empty task list."""
        result = render_task_list([])
        assert result == "No tasks found. Add a task using 'add' command."

    def test_single_task_list(self):
        """Test rendering a list with a single task."""
        tasks = [
            {
                "id": 1,
                "title": "Test Task",
                "description": "Test Description",
                "completed": False,
                "created_at": "2025-12-30T10:30:00"
            }
        ]
        result = render_task_list(tasks)

        lines = result.split('\n')
        assert "ID | Status | Title" in result
        assert "---|--------|------" in result
        assert "1 | ○      | Test Task" in result

    def test_multiple_tasks_list(self):
        """Test rendering a list with multiple tasks."""
        tasks = [
            {
                "id": 1,
                "title": "Task 1",
                "description": "Description 1",
                "completed": False,
                "created_at": "2025-12-30T10:30:00"
            },
            {
                "id": 2,
                "title": "Task 2",
                "description": "Description 2",
                "completed": True,
                "created_at": "2025-12-30T10:31:00"
            }
        ]
        result = render_task_list(tasks)

        assert "ID | Status | Title" in result
        assert "---|--------|------" in result
        assert "1 | ○      | Task 1" in result
        assert "2 | ✓      | Task 2" in result

    def test_completed_task_indicator(self):
        """Test that completed tasks show ✓ indicator."""
        tasks = [
            {
                "id": 1,
                "title": "Completed Task",
                "description": "Test Description",
                "completed": True,
                "created_at": "2025-12-30T10:30:00"
            }
        ]
        result = render_task_list(tasks)
        assert "✓" in result

    def test_pending_task_indicator(self):
        """Test that pending tasks show ○ indicator."""
        tasks = [
            {
                "id": 1,
                "title": "Pending Task",
                "description": "Test Description",
                "completed": False,
                "created_at": "2025-12-30T10:30:00"
            }
        ]
        result = render_task_list(tasks)
        assert "○" in result


class TestRenderTaskDetail:
    """Test cases for render_task_detail function."""

    def test_render_task_detail_completed(self):
        """Test rendering a completed task detail."""
        task = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": True,
            "created_at": "2025-12-30T10:30:00"
        }
        result = render_task_detail(task)

        assert "ID:          1" in result
        assert "Title:       Test Task" in result
        assert "Description: Test Description" in result
        assert "Status:      Completed" in result

    def test_render_task_detail_pending(self):
        """Test rendering a pending task detail."""
        task = {
            "id": 2,
            "title": "Pending Task",
            "description": "Test Description",
            "completed": False,
            "created_at": "2025-12-30T10:30:00"
        }
        result = render_task_detail(task)

        assert "ID:          2" in result
        assert "Title:       Pending Task" in result
        assert "Description: Test Description" in result
        assert "Status:      Pending" in result

    def test_task_without_description(self):
        """Test rendering a task with no description."""
        task = {
            "id": 1,
            "title": "Test Task",
            "description": "",
            "completed": False,
            "created_at": "2025-12-30T10:30:00"
        }
        result = render_task_detail(task)

        assert "Description: [No description]" in result

    def test_task_with_iso_datetime(self):
        """Test rendering a task with ISO datetime format."""
        task = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": False,
            "created_at": "2025-12-30T10:30:00"
        }
        result = render_task_detail(task)

        assert "Created:" in result


class TestRenderMenu:
    """Test cases for render_menu function."""

    def test_render_menu(self):
        """Test rendering the menu."""
        result = render_menu()

        assert "Available Commands:" in result
        assert "add      - Add a new task" in result
        assert "list     - List all tasks" in result
        assert "update   - Update an existing task" in result
        assert "delete   - Delete a task" in result
        assert "complete - Mark a task as complete/incomplete" in result
        assert "help     - Show this menu" in result
        assert "exit     - Exit the application" in result


class TestRenderSuccessMessage:
    """Test cases for render_success_message function."""

    def test_render_success_message(self):
        """Test rendering a success message."""
        message = "Task created successfully"
        result = render_success_message(message)

        assert result == f"✓ {message}"

    def test_render_success_message_empty(self):
        """Test rendering an empty success message."""
        result = render_success_message("")

        assert result == "✓ "


class TestRenderErrorMessage:
    """Test cases for render_error_message function."""

    def test_render_error_message(self):
        """Test rendering an error message."""
        message = "Task not found"
        result = render_error_message(message)

        assert result == f"✗ Error: {message}"

    def test_render_error_message_empty(self):
        """Test rendering an empty error message."""
        result = render_error_message("")

        assert result == "✗ Error: "