"""
Tests for the config.py module.

These tests verify that configuration loading works correctly.

TODO: Learn about pytest basics before implementing these tests
https://docs.pytest.org/en/stable/getting-started.html
"""

import os
import pytest
from config import Config, reload_config


# ============================================================================
# Basic Configuration Tests
# ============================================================================


def test_config_loads_subscription_id(mock_env_vars):
    """
    Test that Config loads AZURE_SUBSCRIPTION_ID from environment.

    The 'mock_env_vars' fixture automatically sets this env var.

    TODO:
    1. Create a Config instance
    2. Assert that config.subscription_id equals the mocked value

    Learn: assert statements - https://docs.pytest.org/en/stable/how-to/assert.html
    """
    # TODO: Implement this test
    # config = Config()
    # assert config.subscription_id == "expected-value"
    pass


def test_config_loads_default_location(mock_env_vars, monkeypatch):
    """
    Test that Config loads DEFAULT_LOCATION from environment.

    TODO:
    1. Use monkeypatch.setenv() to set DEFAULT_LOCATION
    2. Create a Config instance
    3. Assert the location was loaded correctly

    Learn: monkeypatch - https://docs.pytest.org/en/stable/how-to/monkeypatch.html
    """
    # TODO: Implement this test
    # monkeypatch.setenv("DEFAULT_LOCATION", "westus")
    # config = Config()
    # assert config.default_location == "westus"
    pass


# ============================================================================
# Validation Tests
# ============================================================================


def test_config_raises_error_without_subscription_id(monkeypatch):
    """
    Test that Config raises ValueError if AZURE_SUBSCRIPTION_ID is missing.

    TODO:
    1. Remove the AZURE_SUBSCRIPTION_ID env var using monkeypatch.delenv()
    2. Use pytest.raises() to check that Config() raises ValueError

    Learn: pytest.raises - https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions
    """
    # TODO: Implement this test
    # monkeypatch.delenv("AZURE_SUBSCRIPTION_ID", raising=False)
    # with pytest.raises(ValueError):
    #     Config()
    pass


def test_config_validates_log_level(monkeypatch):
    """
    Test that Config validates LOG_LEVEL is a valid option.

    TODO:
    1. Set an invalid LOG_LEVEL (e.g., "INVALID")
    2. Check that Config() raises ValueError
    """
    # TODO: Implement this test
    pass


# ============================================================================
# Helper Method Tests
# ============================================================================


def test_is_service_principal_configured_returns_false_by_default(mock_env_vars):
    """
    Test that is_service_principal_configured() returns False without SP credentials.

    TODO:
    1. Create a Config instance
    2. Call config.is_service_principal_configured()
    3. Assert it returns False
    """
    # TODO: Implement this test
    pass


def test_is_service_principal_configured_returns_true_with_credentials(monkeypatch):
    """
    Test that is_service_principal_configured() returns True when all SP vars are set.

    TODO:
    1. Use monkeypatch to set AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID
    2. Create Config instance
    3. Assert is_service_principal_configured() returns True
    """
    # TODO: Implement this test
    pass


def test_get_authentication_method(mock_env_vars):
    """
    Test that get_authentication_method() returns correct auth type.

    TODO:
    1. Create Config instance (should default to azure_cli)
    2. Assert get_authentication_method() returns "azure_cli"
    """
    # TODO: Implement this test
    pass


# ============================================================================
# Edge Cases and Error Handling
# ============================================================================


def test_config_repr_masks_sensitive_data(mock_env_vars):
    """
    Test that __repr__ doesn't expose full subscription ID.

    TODO:
    1. Create Config instance
    2. Call repr(config) or str(config)
    3. Assert that the full subscription ID is NOT in the string
    4. Assert that only last 4 chars are shown (e.g., "***0000")
    """
    # TODO: Implement this test
    pass


# ============================================================================
# BONUS: Advanced Tests (Optional)
# ============================================================================


def test_reload_config_picks_up_new_values(monkeypatch):
    """
    BONUS: Test that reload_config() loads new environment variable values.

    This is an advanced test - skip if you're just getting started.
    """
    # TODO (Optional): Implement this test
    pass
