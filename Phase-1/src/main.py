#!/usr/bin/env python3
"""
Main entry point for the Todo In-Memory Python Console App.

This application provides command-line interface for task management
(add, view, update, delete, mark complete) with data stored only in memory
during the session, with no persistence to external databases or files.
"""

from cli import main as cli_main


def main():
    """Application entry point."""
    cli_main()


if __name__ == "__main__":
    main()