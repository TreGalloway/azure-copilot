# Agent Guidelines for az-copilot

## Build/Lint/Test Commands
- **Run application**: `python3 cli.py "<command>"`
- **Activate venv**: `source venv/bin/activate` (Python 3.13)
- **No formal test suite**: Test manually with `python3 cli.py "list resources"`

## Code Style Guidelines
- **Python version**: 3.13
- **Imports**: Standard library first, then third-party (click, rich), then local
- **Formatting**: 4-space indentation, snake_case for functions/variables
- **Dependencies**: Uses `click` for CLI framework, `rich` for console output
- **Function style**: Simple, focused functions with docstrings
- **Error handling**: Use console.print() from rich.console.Console for user-facing messages
- **Naming**: Descriptive names (e.g., `list_resources()`, `show_help()`)
- **CLI pattern**: Use @click.command() and @click.argument() decorators
- **Console output**: Use `console.print()` with optional style parameter for colored output
- **Command parsing**: Simple string matching with .lower() for case-insensitive checks

## Project Context
- Early-stage Azure CLI assistant that translates natural language to Azure commands
- Core files: cli.py (entry point), azure_commands.py, config.py (currently empty)
- Focus on natural language processing for Azure resource management
