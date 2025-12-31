# Quickstart Guide: Todo In-Memory Python Console App

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Navigate to the project directory:
   ```bash
   cd /mnt/d/github/user1/AI-Todo-app/Phase-1
   ```

3. Create a virtual environment using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

## Running the Application

1. Make sure you're in the project root directory:
   ```bash
   cd /mnt/d/github/user1/AI-Todo-app/Phase-1
   ```

2. Run the application:
   ```bash
   python src/main.py
   ```

## Basic Usage

Once the application starts, you'll see the main menu with available commands:

### Adding a Task
```
add "My new task" "Optional description here"
```

### Listing All Tasks
```
list
```

### Updating a Task
```
update 1 "Updated title" "Updated description"
```

### Deleting a Task
```
delete 1
```

### Marking a Task as Complete
```
complete 1 true
```

### Getting Help
```
help
```

### Exiting the Application
```
exit
```

## Important Notes

- All data is stored only in memory and will be lost when you exit the application
- Task IDs are auto-generated and unique within the current session
- Maximum 200 characters for task titles
- Maximum 1000 characters for task descriptions
- The application can handle up to 1000 tasks in memory simultaneously

## Troubleshooting

If you encounter any issues:
1. Verify Python 3.13+ is installed: `python --version`
2. Ensure UV is installed: `uv --version`
3. Check that you're running the application from the correct directory