"""
Tests for the cli.py module.

These tests verify that CLI commands work correctly.

TODO: Learn about Click testing before implementing
https://click.palletsprojects.com/en/8.1.x/testing/
"""

import pytest
from click.testing import CliRunner
from cli import cli, list_resources, show_help


# ============================================================================
# Basic CLI Command Tests
# ============================================================================


def test_cli_accepts_command_argument(cli_runner):
    """
    Test that the CLI accepts a command string as an argument.

    The cli_runner fixture is provided by conftest.py

    TODO:
    1. Use cli_runner.invoke() to run the CLI with a test command
    2. Check that result.exit_code == 0 (success)

    Learn: CliRunner.invoke() returns a Result object with:
        - exit_code: 0 for success, non-zero for errors
        - output: What was printed to the terminal
        - exception: Any exception that was raised

    Example:
        result = cli_runner.invoke(cli, ["help"])
        assert result.exit_code == 0
    """
    # TODO: Implement this test
    pass


def test_cli_shows_command_in_output(cli_runner):
    """
    Test that CLI echoes back the command you typed.

    Looking at cli.py, it prints "You said: {command}"

    TODO:
    1. Invoke the CLI with a test command like "test command"
    2. Assert that result.output contains "You said: test command"

    Learn: Use 'in' operator to check if string is in output
        assert "expected text" in result.output
    """
    # TODO: Implement this test
    pass


# ============================================================================
# Help Command Tests
# ============================================================================


def test_help_command_recognized(cli_runner):
    """
    Test that typing "help" triggers the help function.

    TODO:
    1. Invoke CLI with "help" command
    2. Check that result.output contains "Available commands"
    """
    # TODO: Implement this test
    pass


def test_help_shows_available_commands(cli_runner):
    """
    Test that help output lists available commands.

    TODO:
    1. Invoke CLI with "help"
    2. Assert that output mentions "list resources"
    """
    # TODO: Implement this test
    pass


# ============================================================================
# List Resources Command Tests
# ============================================================================


def test_list_resources_command_recognized(cli_runner):
    """
    Test that "list resources" is recognized as a valid command.

    TODO:
    1. Invoke CLI with "list resources"
    2. Check that it doesn't say "Command not recognized"
    3. Check that it says "Listing your resources"
    """
    # TODO: Implement this test
    pass


def test_list_command_variations(cli_runner):
    """
    Test that different variations of list command work.

    The CLI checks for "list" AND "resource" in the command.

    TODO: Test these variations all work:
    - "list resources"
    - "list my resources"
    - "show me resource list"

    Hint: Use a loop or multiple assertions
    """
    # TODO: Implement this test
    pass


# ============================================================================
# Unrecognized Command Tests
# ============================================================================


def test_unknown_command_shows_error(cli_runner):
    """
    Test that unrecognized commands show an error message.

    TODO:
    1. Invoke CLI with an invalid command like "foobar"
    2. Assert output contains "Command not recognized"
    """
    # TODO: Implement this test
    pass


# ============================================================================
# Edge Cases
# ============================================================================


def test_empty_command(cli_runner):
    """
    Test what happens with an empty command.

    TODO:
    1. Try invoking with empty string ""
    2. Decide what the expected behavior should be
    3. Test for that behavior
    """
    # TODO: Implement this test
    pass


def test_case_insensitive_commands(cli_runner):
    """
    Test that commands work regardless of case.

    Looking at cli.py, it uses .lower() so "HELP" should work.

    TODO:
    1. Test "HELP", "Help", "hElP" all work
    2. Assert they all trigger the help function
    """
    # TODO: Implement this test
    pass


# ============================================================================
# BONUS: Function Unit Tests (Optional)
# ============================================================================


def test_list_resources_function_directly():
    """
    BONUS: Test the list_resources() function directly (not through CLI).

    This tests the function in isolation.

    TODO:
    1. Call list_resources() directly
    2. Check it doesn't raise exceptions

    Note: This will print to console since it uses Rich Console
    """
    # TODO (Optional): Implement this test
    pass


def test_show_help_function_directly():
    """
    BONUS: Test the show_help() function directly.

    TODO:
    1. Call show_help() directly
    2. Verify it doesn't crash
    """
    # TODO (Optional): Implement this test
    pass
