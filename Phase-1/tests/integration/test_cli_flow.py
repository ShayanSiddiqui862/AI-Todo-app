"""
Integration tests for CLI flow in the Todo CLI application.

Tests the end-to-end CLI command processing flow.
"""
import pytest
from unittest.mock import patch, MagicMock
from src.cli import process_command, handle_add_task, handle_list_tasks, handle_update_task, handle_delete_task, handle_mark_complete, display_menu
from src.storage import storage_manager


class TestCLIIntegration:
    """Test cases for CLI flow integration."""

    def setup_method(self):
        """Set up for each test method."""
        # Clear all tasks to start with a clean state
        storage_manager.clear_all_tasks()

    def test_add_task_integration(self):
        """Test adding a task through the CLI flow."""
        with patch('builtins.input', side_effect=['Test Task Title', 'Test Description']):
            with patch('builtins.print') as mock_print:
                handle_add_task()

        # Verify task was added to storage
        tasks = storage_manager.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0]['title'] == 'Test Task Title'
        assert tasks[0]['description'] == 'Test Description'
        assert tasks[0]['completed'] is False

    def test_list_tasks_integration(self):
        """Test listing tasks through the CLI flow."""
        # Add a test task
        storage_manager.create_task('Test Task', 'Test Description')

        with patch('builtins.print') as mock_print:
            handle_list_tasks()

        # Verify print was called (at least once for the task list)
        assert mock_print.called

    def test_update_task_integration(self):
        """Test updating a task through the CLI flow."""
        # Add a test task first
        storage_manager.create_task('Old Title', 'Old Description')

        with patch('builtins.input', side_effect=['1', 'New Title', 'New Description']):
            with patch('builtins.print') as mock_print:
                handle_update_task()

        # Verify task was updated in storage
        task = storage_manager.get_task_by_id(1)
        assert task['title'] == 'New Title'
        assert task['description'] == 'New Description'

    def test_delete_task_integration(self):
        """Test deleting a task through the CLI flow."""
        # Add a test task first
        storage_manager.create_task('Test Task', 'Test Description')

        with patch('builtins.input', side_effect=['1', 'y']):  # Confirm deletion
            with patch('builtins.print') as mock_print:
                handle_delete_task()

        # Verify task was deleted from storage
        tasks = storage_manager.get_all_tasks()
        assert len(tasks) == 0

    def test_mark_complete_integration(self):
        """Test marking a task as complete through the CLI flow."""
        # Add a test task first
        storage_manager.create_task('Test Task', 'Test Description')

        with patch('builtins.input', side_effect=['1']):
            with patch('builtins.print') as mock_print:
                handle_mark_complete()

        # Verify task completion status was updated
        task = storage_manager.get_task_by_id(1)
        assert task['completed'] is True

    def test_command_routing_add(self):
        """Test command routing for 'add' command."""
        with patch('src.cli.handle_add_task') as mock_handle:
            process_command('add')
            mock_handle.assert_called_once()

    def test_command_routing_list(self):
        """Test command routing for 'list' command."""
        with patch('src.cli.handle_list_tasks') as mock_handle:
            process_command('list')
            mock_handle.assert_called_once()

    def test_command_routing_update(self):
        """Test command routing for 'update' command."""
        with patch('src.cli.handle_update_task') as mock_handle:
            process_command('update')
            mock_handle.assert_called_once()

    def test_command_routing_delete(self):
        """Test command routing for 'delete' command."""
        with patch('src.cli.handle_delete_task') as mock_handle:
            process_command('delete')
            mock_handle.assert_called_once()

    def test_command_routing_complete(self):
        """Test command routing for 'complete' command."""
        with patch('src.cli.handle_mark_complete') as mock_handle:
            process_command('complete')
            mock_handle.assert_called_once()

    def test_command_routing_help(self):
        """Test command routing for 'help' command."""
        with patch('src.cli.display_menu') as mock_display:
            process_command('help')
            mock_display.assert_called_once()

    def test_command_routing_exit(self):
        """Test command routing for 'exit' command."""
        result = process_command('exit')
        assert result is False  # Should return False to exit

    def test_invalid_command_routing(self):
        """Test command routing for invalid command."""
        with patch('builtins.print') as mock_print:
            result = process_command('invalid_command')
            assert result is True  # Should continue running
            # Verify error message was printed
            mock_print.assert_called()

    def test_empty_command(self):
        """Test processing an empty command."""
        with patch('builtins.print') as mock_print:
            result = process_command('')
            assert result is True  # Should continue running
            # Verify error message was printed
            mock_print.assert_called()

    def test_command_with_extra_args(self):
        """Test command with additional arguments."""
        # This should still route to the appropriate handler
        with patch('src.cli.handle_add_task') as mock_handle:
            process_command('add extra args')
            mock_handle.assert_called_once()

    def test_menu_display(self):
        """Test that menu display works correctly."""
        with patch('builtins.print') as mock_print:
            display_menu()
            # Verify print was called
            assert mock_print.called