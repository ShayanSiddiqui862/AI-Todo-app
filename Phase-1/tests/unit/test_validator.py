"""
Unit tests for validation functions in the Todo CLI application.

Tests all validation functions: task title, description, ID validation.
"""
import pytest
from src.validator import validate_task_title, validate_task_description, validate_task_id, is_valid_command


class TestValidateTaskTitle:
    """Test cases for validate_task_title function."""

    def test_valid_title(self):
        """Test validating a valid title."""
        title = "Valid Task Title"
        result = validate_task_title(title)
        assert result == "Valid Task Title"

    def test_title_with_whitespace(self):
        """Test validating a title with leading/trailing whitespace."""
        title = "  Task Title with Whitespace  "
        result = validate_task_title(title)
        assert result == "Task Title with Whitespace"

    def test_empty_title(self):
        """Test validating an empty title."""
        with pytest.raises(ValueError, match="Task title is required and cannot be empty"):
            validate_task_title("")

    def test_whitespace_only_title(self):
        """Test validating a title with only whitespace."""
        with pytest.raises(ValueError, match="Task title is required and cannot be empty"):
            validate_task_title("   ")

    def test_title_too_long(self):
        """Test validating a title that exceeds 200 characters."""
        long_title = "A" * 201
        with pytest.raises(ValueError, match="Task title exceeds maximum length of 200 characters"):
            validate_task_title(long_title)

    def test_minimal_valid_title(self):
        """Test validating the shortest valid title."""
        title = "A"
        result = validate_task_title(title)
        assert result == "A"


class TestValidateTaskDescription:
    """Test cases for validate_task_description function."""

    def test_valid_description(self):
        """Test validating a valid description."""
        description = "Valid Task Description"
        result = validate_task_description(description)
        assert result == "Valid Task Description"

    def test_description_with_whitespace(self):
        """Test validating a description with leading/trailing whitespace."""
        description = "  Task Description with Whitespace  "
        result = validate_task_description(description)
        assert result == "Task Description with Whitespace"

    def test_empty_description(self):
        """Test validating an empty description."""
        result = validate_task_description("")
        assert result == ""

    def test_none_description(self):
        """Test validating a None description."""
        result = validate_task_description(None)
        assert result == ""

    def test_description_too_long(self):
        """Test validating a description that exceeds 1000 characters."""
        long_description = "A" * 1001
        with pytest.raises(ValueError, match="Task description exceeds maximum length of 1000 characters"):
            validate_task_description(long_description)

    def test_max_length_description(self):
        """Test validating a description at the maximum length."""
        max_description = "A" * 1000
        result = validate_task_description(max_description)
        assert result == max_description


class TestValidateTaskId:
    """Test cases for validate_task_id function."""

    def test_valid_positive_integer_string(self):
        """Test validating a valid positive integer string."""
        result = validate_task_id("123")
        assert result == 123

    def test_valid_positive_integer_with_whitespace(self):
        """Test validating a positive integer string with whitespace."""
        result = validate_task_id("  456  ")
        assert result == 456

    def test_invalid_empty_string(self):
        """Test validating an empty string."""
        with pytest.raises(ValueError, match="Task ID is required and cannot be empty"):
            validate_task_id("")

    def test_invalid_whitespace_only(self):
        """Test validating a string with only whitespace."""
        with pytest.raises(ValueError, match="Task ID is required and cannot be empty"):
            validate_task_id("   ")

    def test_invalid_non_numeric_string(self):
        """Test validating a non-numeric string."""
        with pytest.raises(ValueError, match="Task ID must be a valid integer"):
            validate_task_id("abc")

    def test_invalid_negative_number(self):
        """Test validating a negative number."""
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            validate_task_id("-5")

    def test_invalid_zero(self):
        """Test validating zero."""
        with pytest.raises(ValueError, match="Task ID must be a positive integer"):
            validate_task_id("0")

    def test_valid_with_max_id_within_range(self):
        """Test validating a valid ID within the max range."""
        result = validate_task_id("5", max_id=10)
        assert result == 5

    def test_invalid_with_max_id_exceeded(self):
        """Test validating an ID that exceeds the max range."""
        with pytest.raises(ValueError, match="Task ID 15 exceeds maximum allowed ID of 10"):
            validate_task_id("15", max_id=10)


class TestIsValidCommand:
    """Test cases for is_valid_command function."""

    def test_valid_commands(self):
        """Test validating all valid commands."""
        valid_commands = ["add", "list", "update", "delete", "complete", "help", "exit"]
        for cmd in valid_commands:
            assert is_valid_command(cmd) is True
            assert is_valid_command(cmd.upper()) is True  # Test case insensitivity

    def test_invalid_command(self):
        """Test validating an invalid command."""
        assert is_valid_command("invalid") is False

    def test_command_with_whitespace(self):
        """Test validating a command with whitespace."""
        assert is_valid_command(" add ") is True

    def test_empty_command(self):
        """Test validating an empty command."""
        assert is_valid_command("") is False

    def test_partial_command(self):
        """Test validating a partial command."""
        assert is_valid_command("ad") is False  # Should be "add"