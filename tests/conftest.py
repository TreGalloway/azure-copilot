"""
Pytest configuration and fixtures for Azure Copilot tests.

This file provides reusable test fixtures that your tests can use.
Fixtures are like "setup helpers" that run before your tests.
"""

import os
from typing import Generator
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner


# ============================================================================
# Environment Fixtures - Manage test environment variables
# ============================================================================


@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Automatically sets fake environment variables for ALL tests.

    This prevents tests from accidentally using your real Azure credentials.
    'autouse=True' means this runs before every test automatically.

    TODO: Learn about monkeypatch.setenv() - it temporarily sets env vars
    https://docs.pytest.org/en/stable/how-to/monkeypatch.html
    """
    # Set a fake Azure subscription ID so tests don't use your real one
    monkeypatch.setenv("AZURE_SUBSCRIPTION_ID", "00000000-0000-0000-0000-000000000000")

    # TODO: Add more environment variables here as needed
    # monkeypatch.setenv("DEFAULT_LOCATION", "eastus")
    # monkeypatch.setenv("LOG_LEVEL", "DEBUG")


# ============================================================================
# CLI Testing Fixtures - Test Click commands
# ============================================================================


@pytest.fixture
def cli_runner() -> CliRunner:
    """
    Creates a Click CLI test runner.

    Use this in tests to run CLI commands without a real terminal.

    Example usage in a test:
        def test_help(cli_runner):
            result = cli_runner.invoke(cli, ["--help"])
            assert result.exit_code == 0

    TODO: Learn about Click's CliRunner
    https://click.palletsprojects.com/en/8.1.x/testing/
    """
    return CliRunner()


# ============================================================================
# Azure SDK Mock Fixtures - Fake Azure API clients
# ============================================================================


@pytest.fixture
def mock_credential() -> Generator[MagicMock, None, None]:
    """
    Mocks Azure DefaultAzureCredential so tests don't need real auth.

    This replaces the REAL credential with a fake one during tests.

    TODO: Learn about unittest.mock.patch and MagicMock
    https://docs.python.org/3/library/unittest.mock.html
    """
    with patch("azure.identity.DefaultAzureCredential") as mock:
        # Create a fake credential object
        mock_cred = MagicMock()
        mock.return_value = mock_cred
        yield mock_cred  # Provide the fake to tests


@pytest.fixture
def mock_resource_client() -> Generator[MagicMock, None, None]:
    """
    Mocks Azure ResourceManagementClient to prevent real API calls.

    This is the main fixture you'll use for testing Azure operations.

    TODO: Configure this mock to return fake resource groups
    Example:
        client.resource_groups.list.return_value = [fake_rg1, fake_rg2]
    """
    with patch("azure.mgmt.resource.ResourceManagementClient") as mock:
        # Create a fake Azure client
        client = MagicMock()

        # TODO: Configure the mock to return fake data
        # Example: client.resource_groups.list.return_value = [...]

        mock.return_value = client
        yield client


# ============================================================================
# Test Data Helpers - Create fake Azure objects for testing
# ============================================================================


def create_fake_resource_group(name: str, location: str) -> MagicMock:
    """
    Creates a fake Azure ResourceGroup object for testing.

    TODO: Make this return a MagicMock that has .name and .location properties

    Example:
        rg = MagicMock()
        rg.name = name
        rg.location = location
        return rg
    """
    # TODO: Implement this helper
    raise NotImplementedError("You need to implement this!")


@pytest.fixture
def sample_resource_groups() -> list[dict[str, str]]:
    """
    Provides sample resource group data for tests.

    TODO: Return a list of dictionaries representing resource groups
    Example: [{"name": "dev-rg", "location": "eastus"}, ...]
    """
    # TODO: Implement this - return a list of 2-3 fake resource groups
    return []
