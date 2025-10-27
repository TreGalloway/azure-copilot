"""
Configuration management for Azure Copilot.

This module loads and validates configuration from environment variables,
providing a clean API for accessing settings throughout the application.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Load .env file from the project root
load_dotenv()


@dataclass
class Config:
    """
    Application configuration loaded from environment variables.

    All settings are loaded from .env file or environment variables.
    See .env.example for available configuration options.
    """

    # =========================================================================
    # Azure Authentication (Required)
    # =========================================================================
    subscription_id: str = field(default_factory=lambda: os.getenv("AZURE_SUBSCRIPTION_ID", ""))

    # Optional authentication for Service Principal
    client_id: Optional[str] = field(default_factory=lambda: os.getenv("AZURE_CLIENT_ID", None))
    client_secret: Optional[str] = field(
        default_factory=lambda: os.getenv("AZURE_CLIENT_SECRET", None)
    )
    tenant_id: Optional[str] = field(default_factory=lambda: os.getenv("AZURE_TENANT_ID", None))

    # =========================================================================
    # Azure Defaults
    # =========================================================================
    default_location: str = field(default_factory=lambda: os.getenv("DEFAULT_LOCATION", "eastus"))
    default_resource_group: str = field(
        default_factory=lambda: os.getenv("DEFAULT_RESOURCE_GROUP", "")
    )

    # =========================================================================
    # Azure OpenAI (Week 3+ - Optional)
    # =========================================================================
    openai_endpoint: Optional[str] = field(
        default_factory=lambda: os.getenv("AZURE_OPENAI_ENDPOINT", None)
    )
    openai_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("AZURE_OPENAI_API_KEY", None)
    )
    openai_deployment: str = field(
        default_factory=lambda: os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4-turbo")
    )
    openai_api_version: str = field(
        default_factory=lambda: os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    )

    # =========================================================================
    # Application Settings
    # =========================================================================
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    debug: bool = field(default_factory=lambda: os.getenv("DEBUG", "false").lower() == "true")
    default_dry_run: bool = field(
        default_factory=lambda: os.getenv("DEFAULT_DRY_RUN", "false").lower() == "true"
    )
    skip_confirmations: bool = field(
        default_factory=lambda: os.getenv("SKIP_CONFIRMATIONS", "false").lower() == "true"
    )
    track_token_usage: bool = field(
        default_factory=lambda: os.getenv("TRACK_TOKEN_USAGE", "true").lower() == "true"
    )

    # =========================================================================
    # Vector Database (Week 5+ - Optional)
    # =========================================================================
    chroma_persist_directory: Path = field(
        default_factory=lambda: Path(os.getenv("CHROMA_PERSIST_DIRECTORY", "./data/chroma"))
    )
    embedding_model: str = field(
        default_factory=lambda: os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
    )

    def __post_init__(self) -> None:
        """Validate required configuration after initialization."""
        self._validate_required_settings()
        self._validate_log_level()

    def _validate_required_settings(self) -> None:
        """
        Validate that all required settings are present.

        Raises:
            ValueError: If required settings are missing.
        """
        if not self.subscription_id:
            raise ValueError(
                "AZURE_SUBSCRIPTION_ID is required. "
                "Please set it in your .env file or environment variables.\n"
                "Run 'az account show --query id -o tsv' to get your subscription ID."
            )

    def _validate_log_level(self) -> None:
        """
        Validate that log level is valid.

        Raises:
            ValueError: If log level is invalid.
        """
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if self.log_level.upper() not in valid_levels:
            raise ValueError(
                f"Invalid LOG_LEVEL: {self.log_level}. Must be one of: {', '.join(valid_levels)}"
            )
        # Normalize to uppercase
        self.log_level = self.log_level.upper()

    def is_service_principal_configured(self) -> bool:
        """
        Check if service principal authentication is configured.

        Returns:
            True if all service principal settings are present, False otherwise.
        """
        return bool(self.client_id and self.client_secret and self.tenant_id)

    def is_openai_configured(self) -> bool:
        """
        Check if Azure OpenAI is configured (Week 3+ feature).

        Returns:
            True if OpenAI endpoint and API key are set, False otherwise.
        """
        return bool(self.openai_endpoint and self.openai_api_key)

    def get_authentication_method(self) -> str:
        """
        Determine which authentication method is configured.

        Returns:
            String describing the authentication method:
            - "service_principal" if SP credentials are set
            - "azure_cli" if using DefaultAzureCredential fallback
        """
        if self.is_service_principal_configured():
            return "service_principal"
        return "azure_cli"

    def __repr__(self) -> str:
        """
        String representation with sensitive data masked.

        Returns:
            Safe string representation of the configuration.
        """
        return (
            f"Config("
            f"subscription_id={'***' + self.subscription_id[-4:] if self.subscription_id else 'NOT SET'}, "
            f"auth_method={self.get_authentication_method()}, "
            f"default_location={self.default_location}, "
            f"log_level={self.log_level})"
        )


# ============================================================================
# Singleton Instance
# ============================================================================
# Create a single global config instance that can be imported anywhere
try:
    config = Config()
except ValueError as e:
    # If configuration fails, print helpful error and re-raise
    print(f"\n❌ Configuration Error: {e}\n")
    print("💡 Quick Setup:")
    print("   1. Copy .env.example to .env:  cp .env.example .env")
    print("   2. Run: az login")
    print("   3. Run: az account show --query id -o tsv")
    print("   4. Add the subscription ID to your .env file\n")
    raise


# ============================================================================
# Helper Functions
# ============================================================================
def reload_config() -> Config:
    """
    Reload configuration from environment variables.

    Useful for testing or when environment variables change at runtime.

    Returns:
        New Config instance with reloaded values.
    """
    load_dotenv(override=True)
    return Config()


def print_config(safe: bool = True) -> None:
    """
    Print current configuration to console.

    Args:
        safe: If True, mask sensitive values. If False, show all values.
              WARNING: Only use safe=False in secure debugging environments!
    """
    if safe:
        print(config)
    else:
        print("⚠️  WARNING: Displaying sensitive configuration values!")
        print(f"Subscription ID: {config.subscription_id}")
        print(f"Tenant ID: {config.tenant_id}")
        print(f"Client ID: {config.client_id}")
        print(f"Default Location: {config.default_location}")
        print(f"Log Level: {config.log_level}")
        print(f"OpenAI Configured: {config.is_openai_configured()}")
