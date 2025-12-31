"""
CLI controller and command processor for the Todo application.

Manages the main application loop and command routing to handle user input
and execute appropriate functions for task management operations.
"""

from storage import storage_manager
from validator import validate_task_title, validate_task_description, validate_task_id, is_valid_command
from renderer import render_task_list, render_task_detail, render_menu, render_success_message, render_error_message


def display_menu() -> None:
    """Show available commands to the user."""
    print(render_menu())


def process_command(command: str) -> bool:
    """
    Process user input and execute appropriate functions.

    Args:
        command: Command string from user input

    Returns:
        True to continue running, False to exit
    """
    cmd_parts = command.strip().split()
    if not cmd_parts:
        print(render_error_message("Please enter a command. Type 'help' for available options."))
        return True

    cmd = cmd_parts[0].lower()

    if not is_valid_command(cmd):
        print(render_error_message(f"Unknown command: {cmd}. Type 'help' for available options."))
        return True

    if cmd == "add":
        handle_add_task()
    elif cmd == "list":
        handle_list_tasks()
    elif cmd == "update":
        handle_update_task()
    elif cmd == "delete":
        handle_delete_task()
    elif cmd == "complete":
        handle_mark_complete()
    elif cmd == "help":
        display_menu()
    elif cmd == "exit":
        return False

    return True


def handle_add_task() -> None:
    """Handle adding new tasks."""
    try:
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional): ").strip()

        validated_title = validate_task_title(title)
        validated_description = validate_task_description(description)

        task = storage_manager.create_task(validated_title, validated_description)
        print(render_success_message(f"Task '{task['title']}' added successfully with ID {task['id']}"))
    except ValueError as e:
        print(render_error_message(str(e)))
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


def handle_list_tasks() -> None:
    """Handle displaying all tasks."""
    tasks = storage_manager.get_all_tasks()
    print(render_task_list(tasks))


def handle_update_task() -> None:
    """Handle updating existing tasks."""
    try:
        task_id_str = input("Enter task ID to update: ").strip()
        tasks = storage_manager.get_all_tasks()
        max_id = max([task['id'] for task in tasks]) if tasks else 0

        task_id = validate_task_id(task_id_str, max_id)
        task = storage_manager.get_task_by_id(task_id)

        if not task:
            print(render_error_message(f"Task with ID {task_id} not found."))
            return

        print(f"Current task: {task['title']}")
        new_title = input(f"Enter new title (current: '{task['title']}'): ").strip()
        new_description = input(f"Enter new description (current: '{task['description']}'): ").strip()

        # Use current values if no new input is provided
        title = new_title if new_title else task['title']
        description = new_description if new_description else task['description']

        # Validate inputs if they are provided
        if new_title:
            title = validate_task_title(title)
        if new_description:
            description = validate_task_description(description)

        updated_task = storage_manager.update_task(task_id, title=title, description=description)
        if updated_task:
            print(render_success_message(f"Task {task_id} updated successfully"))
        else:
            print(render_error_message(f"Failed to update task {task_id}"))

    except ValueError as e:
        print(render_error_message(str(e)))
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


def handle_delete_task() -> None:
    """Handle deleting tasks."""
    try:
        task_id_str = input("Enter task ID to delete: ").strip()
        tasks = storage_manager.get_all_tasks()
        max_id = max([task['id'] for task in tasks]) if tasks else 0

        task_id = validate_task_id(task_id_str, max_id)
        task = storage_manager.get_task_by_id(task_id)

        if not task:
            print(render_error_message(f"Task with ID {task_id} not found."))
            return

        print(f"Are you sure you want to delete task '{task['title']}'? (y/N): ", end="")
        confirmation = input().strip().lower()

        if confirmation in ['y', 'yes']:
            success = storage_manager.delete_task(task_id)
            if success:
                print(render_success_message(f"Task {task_id} deleted successfully"))
            else:
                print(render_error_message(f"Failed to delete task {task_id}"))
        else:
            print(render_success_message("Task deletion cancelled"))

    except ValueError as e:
        print(render_error_message(str(e)))
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


def handle_mark_complete() -> None:
    """Handle marking tasks as complete/incomplete."""
    try:
        task_id_str = input("Enter task ID to toggle completion status: ").strip()
        tasks = storage_manager.get_all_tasks()
        max_id = max([task['id'] for task in tasks]) if tasks else 0

        task_id = validate_task_id(task_id_str, max_id)
        task = storage_manager.get_task_by_id(task_id)

        if not task:
            print(render_error_message(f"Task with ID {task_id} not found."))
            return

        current_status = task['completed']
        new_status = not current_status
        updated_task = storage_manager.update_task(task_id, completed=new_status)

        status_text = "completed" if new_status else "incomplete"
        if updated_task:
            print(render_success_message(f"Task {task_id} marked as {status_text}"))
        else:
            print(render_error_message(f"Failed to update task {task_id}"))

    except ValueError as e:
        print(render_error_message(str(e)))
    except KeyboardInterrupt:
        print("\nOperation cancelled.")


def main() -> None:
    """Main application entry point that initializes the app and starts the command loop."""
    print("Welcome to the Todo In-Memory Python Console App!")
    print("Type 'help' to see available commands or 'exit' to quit.")

    running = True
    while running:
        try:
            command = input("\n> ").strip()
            if command:
                running = process_command(command)
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            break
        except EOFError:
            print("\n\nExiting application...")
            break

    print("Thank you for using the Todo In-Memory Python Console App!")