# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Azure CLI Assistant** is a Python-based CLI tool that translates natural language commands into Azure CLI operations. The project uses Click for CLI framework and Rich for terminal output formatting.

**Target Python Version**: 3.13
**Status**: Early-stage development (Week 1 phase)
**Core Value**: Eliminate the need to memorize complex Azure CLI syntax by enabling cloud resource management through plain English commands.

## Current Project Structure

```
azure-copilot/
├── cli.py                 # Main CLI entry point (Click-based)
├── azure_commands.py      # Placeholder for Azure SDK wrappers (empty)
├── config.py             # Placeholder for configuration (empty)
├── __init__.py           # Package initialization (empty)
├── README.md             # User-facing documentation
├── CLAUDE.md             # This file - AI assistant guidance
├── roadmap.md            # Detailed 12-week implementation plan
└── AGENTS.md             # Agent-related documentation
```

**Missing Components** (to be created):
- No dependency management (no `requirements.txt`, `pyproject.toml`, or `setup.py`)
- No tests directory or test files
- No `.env` or configuration files
- No CI/CD pipeline
- No Docker configuration

## Architecture (Current Implementation)

### cli.py (Main Entry Point)
- **Framework**: Click with `@click.command()` decorator
- **Argument**: Single string argument for natural language input
- **Output**: Rich Console for formatted terminal output
- **Routing**: Basic keyword matching (`"list"`, `"resource"`, `"help"`)
- **Current Functions**:
  - `list_resources()` - Placeholder for listing Azure resources
  - `show_help()` - Shows basic help text

### Current Limitations
- No actual Azure SDK integration yet
- No authentication mechanism
- No LLM/NLP processing (just string matching)
- No error handling or validation
- No configuration management
- No safety checks or dry-run mode

## Development Setup

### Install Dependencies (Manual)
```bash
pip install click rich
```

### Run the CLI
```bash
python cli.py "your natural language command"

# Examples:
python cli.py "list resources"
python cli.py "help"
```

### Current Working Commands
- `"list resources"` - Triggers list_resources() function
- `"help"` - Shows available commands
- Any other input - Shows "Command not recognized"

## 12-Week Roadmap Summary

The project follows an aggressive 3-month sprint to MVP. See `roadmap.md` for full details.

### Month 1: Foundation + LLM Integration (Weeks 1-4)
**Week 1** (CURRENT): Project setup, Click CLI, Azure authentication, config management
**Week 2**: Azure SDK wrappers, safety features, error handling
**Week 3**: Azure OpenAI integration, intent classification, entity extraction
**Week 4**: Context management, command history, multi-turn conversations

### Month 2: RAG + Production Basics (Weeks 5-8)
- Knowledge base and embeddings
- RAG pipeline for grounded responses
- Security and secrets management (Key Vault)
- Monitoring and observability (App Insights)

### Month 3: Production Polish (Weeks 9-12)
- Testing and evaluation (80%+ coverage)
- Performance optimization
- Packaging and CI/CD
- Launch preparation

## Implementation Priorities

### Week 1 Immediate Tasks (In Priority Order)
1. **Create `pyproject.toml`** or `requirements.txt` for dependency management
2. **Set up tests directory** with pytest
3. **Implement Azure authentication** using `azure-identity`
4. **Create config.py** with basic configuration (Azure credentials, defaults)
5. **Add `--version`, `--help`, `--dry-run` flags** to CLI
6. **Create `.env.example`** template for environment variables

### First 5 Commands to Build
1. `copilot auth` - Authenticate with Azure (using DefaultAzureCredential)
2. `copilot "list my resource groups"` - List resource groups via Azure SDK
3. `copilot "create a resource group called test-rg in eastus"` - Create RG with confirmation
4. `copilot "show me all VMs"` - List virtual machines
5. `copilot help` - Show comprehensive help

## Technology Stack

### Current Dependencies
- **click** (8.1+) - CLI framework
- **rich** (13.0+) - Terminal formatting

### Required Dependencies (Week 1)
- **azure-identity** - Azure authentication
- **azure-mgmt-resource** - Resource management
- **azure-mgmt-compute** - VM management
- **azure-mgmt-storage** - Storage account management
- **python-dotenv** - Environment variable management

### Future Dependencies (Week 3+)
- **openai** - Azure OpenAI integration
- **pytest**, **pytest-asyncio**, **pytest-cov** - Testing
- **ruff**, **black**, **mypy** - Code quality

## Code Quality Guidelines

### Python Standards
- **Type hints**: Use everywhere (leverage Python 3.13 features)
- **Docstrings**: Google-style for all public functions/classes
- **Function length**: Keep under 50 lines
- **Error handling**: Always provide user-friendly messages
- **Async/await**: Use for I/O operations (Azure SDK calls)

### Example Function Structure
```python
async def list_resource_groups(subscription_id: str) -> list[dict[str, str]]:
    """
    List all resource groups in the specified subscription.

    Args:
        subscription_id: Azure subscription ID

    Returns:
        List of resource group dictionaries with name and location

    Raises:
        AzureAuthError: If authentication fails
        AzureAPIError: If API call fails
    """
    try:
        # Implementation
        pass
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise
```

### Testing Requirements
- Write tests alongside features (not after)
- Aim for 80%+ code coverage from Week 1
- Use pytest fixtures for Azure SDK mocks
- Test both success and error paths

## Safety and Security Guidelines

### Critical Safety Rules
1. **Destructive operations MUST have confirmation prompts**
   - Delete, stop, restart operations require user input
   - Implement `--force` flag to bypass (use with caution)

2. **Dry-run mode is mandatory**
   - Add `--dry-run` flag that shows what would happen
   - Show Azure CLI equivalent command before execution

3. **No hardcoded credentials**
   - Use Azure Key Vault or environment variables only
   - Never commit `.env` files

4. **Input validation**
   - Sanitize all user inputs
   - Validate resource names against Azure naming rules
   - Check for prompt injection attempts (when LLM added)

### Example Safety Pattern
```python
@click.option('--dry-run', is_flag=True, help='Show what would happen without executing')
@click.option('--force', is_flag=True, help='Skip confirmation prompts')
def delete_resource_group(name: str, dry_run: bool, force: bool):
    if dry_run:
        console.print(f"[yellow]Would delete resource group: {name}[/yellow]")
        return

    if not force:
        confirm = click.confirm(f"Delete resource group '{name}'? This cannot be undone.")
        if not confirm:
            console.print("[blue]Operation cancelled[/blue]")
            return

    # Execute deletion
    delete_rg(name)
```

## Common Development Patterns

### Azure SDK Usage Pattern
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)

# List resource groups
for rg in client.resource_groups.list():
    console.print(f"- {rg.name} ({rg.location})")
```

### Rich Console Formatting
```python
from rich.console import Console
from rich.table import Table

console = Console()

# Success message
console.print("[green]✓[/green] Operation completed")

# Error message
console.print("[red]✗[/red] Operation failed", style="bold")

# Table output
table = Table(title="Resource Groups")
table.add_column("Name", style="cyan")
table.add_column("Location", style="magenta")
table.add_row("my-rg", "eastus")
console.print(table)
```

## Development Workflow

### Daily Workflow
1. **Pull latest changes**: `git pull origin main`
2. **Create feature branch**: `git checkout -b feat/feature-name`
3. **Write tests first** (TDD approach when possible)
4. **Implement feature** with type hints and docstrings
5. **Run tests**: `pytest tests/`
6. **Format code**: `black . && ruff check .` (when tools added)
7. **Commit with clear message**: `git commit -m "feat: add resource group listing"`
8. **Push and create PR**: `git push origin feat/feature-name`

### Commit Message Format
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions/changes
- `refactor:` - Code refactoring
- `chore:` - Tooling, dependencies

## Key Implementation Principles

### 🎯 Core Philosophy
- **Ship fast, iterate faster** - Working code beats perfect code
- **Safety first** - Prevent destructive mistakes at all costs
- **User feedback drives development** - Build what users need, not what's elegant
- **Test everything** - Bugs in production are 10x more expensive

### Week-by-Week Focus
- **Weeks 1-4**: Get something working that users can try
- **Weeks 5-8**: Make it reliable, secure, and production-ready
- **Weeks 9-12**: Make it fast, polished, and shippable

### Common Pitfalls to Avoid
❌ **Don't** build complex features before validating basic value
❌ **Don't** skip dry-run mode for destructive operations
❌ **Don't** optimize prematurely (performance work is Week 10)
❌ **Don't** ignore costs (track LLM token usage from day 1)
❌ **Don't** skip tests (they save debugging time later)

✅ **Do** implement safety checks immediately
✅ **Do** write tests alongside features
✅ **Do** keep functions small and focused
✅ **Do** use type hints everywhere
✅ **Do** provide helpful error messages

## Success Metrics

### Week 1 Success Criteria
- [ ] CLI runs with `--version` and `--help` flags
- [ ] Can authenticate with Azure using DefaultAzureCredential
- [ ] Can list resource groups in default subscription
- [ ] Basic config file loads environment variables
- [ ] At least 3 tests written and passing
- [ ] Dependencies documented in `pyproject.toml` or `requirements.txt`

### MVP Success Criteria (Week 12)
- Command interpretation accuracy > 90%
- Average response time < 3 seconds
- Zero unintended destructive operations in testing
- 80%+ test coverage
- 50+ test cases passing
- pip-installable package
- 5+ early users providing feedback

## Quick Reference Commands

### Project Setup (Week 1)
```bash
# Create virtual environment
python3.13 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies (after creating requirements file)
pip install -r requirements.txt

# Run CLI
python cli.py "list my resources"

# Run tests (after setup)
pytest tests/ -v --cov=. --cov-report=html
```

### Azure Authentication Setup
```bash
# Login to Azure CLI (easiest method)
az login

# Or set environment variables
export AZURE_SUBSCRIPTION_ID="your-subscription-id"
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
```

## File Templates

### pyproject.toml Template (Week 1)
```toml
[project]
name = "azure-copilot"
version = "0.1.0"
description = "Natural language interface for Azure CLI"
requires-python = ">=3.13"
dependencies = [
    "click>=8.1.0",
    "rich>=13.0.0",
    "azure-identity>=1.15.0",
    "azure-mgmt-resource>=23.0.0",
    "azure-mgmt-compute>=30.0.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.1.0",
    "black>=23.0.0",
    "mypy>=1.7.0",
]

[project.scripts]
copilot = "cli:cli"
```

### .env.example Template
```bash
# Azure Configuration
AZURE_SUBSCRIPTION_ID=your-subscription-id-here
AZURE_TENANT_ID=your-tenant-id-here

# Optional: Service Principal Authentication
# AZURE_CLIENT_ID=your-client-id
# AZURE_CLIENT_SECRET=your-client-secret

# Default Settings
DEFAULT_LOCATION=eastus
DEFAULT_RESOURCE_GROUP=my-default-rg

# Azure OpenAI (Week 3+)
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
# AZURE_OPENAI_API_KEY=your-api-key
# AZURE_OPENAI_DEPLOYMENT=gpt-4-turbo
```

## Troubleshooting Guide

### Common Issues

**Issue**: "Command not recognized"
**Solution**: Check keyword matching in `cli.py`. Currently only "list", "resource", and "help" are recognized.

**Issue**: Azure authentication fails
**Solution**: Run `az login` first, or set environment variables correctly.

**Issue**: Module not found errors
**Solution**: Install dependencies: `pip install click rich`

**Issue**: Permission denied on Azure operations
**Solution**: Ensure your Azure account has required RBAC roles (Contributor or specific resource permissions)

## Resources

### Documentation Links
- [Azure SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/)
- [Click Documentation](https://click.palletsprojects.com/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [Azure CLI Reference](https://learn.microsoft.com/en-us/cli/azure/)

### Internal Project Files
- `roadmap.md` - Detailed 12-week implementation plan
- `README.md` - User-facing project documentation
- `AGENTS.md` - Agent-related documentation

## Notes for Claude Code

When working on this project:

1. **Always prioritize safety** - Add confirmation prompts before any destructive operation
2. **Create tests first** when adding new features (TDD approach)
3. **Use type hints** in all new code (Python 3.13 syntax)
4. **Keep functions focused** - One function, one responsibility, under 50 lines
5. **Ask before major changes** - Confirm architectural decisions with the user
6. **Document as you build** - Update this file and README.md when adding features
7. **Check the roadmap** - Verify new features align with the 12-week plan
8. **Cost awareness** - Track and log token usage when LLM features are added (Week 3+)

### Context for AI Assistants
- This is a **greenfield project** in early development (Week 1 phase)
- The user is following an **aggressive 12-week roadmap** to MVP
- **Safety and testing** are non-negotiable priorities
- The project uses **Python 3.13** - leverage modern features
- Focus on **shipping working code** over perfect architecture

---

**Last Updated**: October 2025
**Version**: 2.1 (Enhanced Documentation)
**Current Phase**: Week 1 - Foundation
**Next Milestone**: Azure authentication + basic resource operations
