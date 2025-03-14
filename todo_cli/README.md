# Todo List CLI

A simple command-line todo list manager built with Python and Click.

## Features

- Add new tasks
- List all tasks
- Mark tasks as complete
- Delete tasks
- Data persistence using JSON file

## Installation

Make sure you have Python installed on your system. Then install the required dependencies:

```bash
pip install click
```

## Usage

The following commands are available:

1. Add a new task:
```bash
python todo.py add "Your task description"
```

2. List all tasks:
```bash
python todo.py list
```

3. Mark a task as complete:
```bash
python todo.py complete TASK_ID
```

4. Delete a task:
```bash
python todo.py delete TASK_ID
```

## Examples

```bash
# Add a new task
python todo.py add "Buy groceries"

# List all tasks
python todo.py list

# Mark task #1 as complete
python todo.py complete 1

# Delete task #2
python todo.py delete 2
```
