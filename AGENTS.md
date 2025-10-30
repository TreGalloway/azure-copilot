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

## 📋 Project Roadmap

### MVP (Week 3)
- ✅ Basic natural language parsing for core Azure commands
- ✅ Command execution with safety validation
- ✅ Resource listing and basic CRUD operations
- ✅ Simple CLI interface with rich output formatting

### v1.0 (Week 12)
- 🔄 Advanced NLP with context awareness and conversation memory
- 🔄 Multi-resource operations and batch processing
- 🔄 Azure Key Vault integration for secure credential management
- 🔄 Intelligent command suggestions and auto-completion
- 🔄 Comprehensive error handling and rollback capabilities
- 🔄 Plugin architecture for extensibility

### Feature Comparison Matrix

| Feature | Current | MVP | v1.0 |
|---------|---------|-----|------|
| Natural Language Parsing | Basic | ✅ Core commands | ✅ Advanced NLP |
| Command Execution | Manual | ✅ Safe execution | ✅ Batch operations |
| Resource Management | None | ✅ CRUD basics | ✅ Multi-resource ops |
| Security | None | ✅ Basic validation | ✅ Key Vault integration |
| Context Awareness | None | ❌ | ✅ Conversation memory |
| Error Handling | Basic | ✅ User-friendly | ✅ Rollback support |

### Use Cases

**Resource Management**
```bash
# Natural language input
"Show me all VMs in my eastus resource group"

# Generated Azure CLI
az vm list --resource-group myRG --location eastus --output table
```

**Infrastructure Deployment**
```bash
# Natural language input
"Create a new web app with Node.js runtime in West Europe"

# Generated Azure CLI
az webapp create --name myWebApp --resource-group myRG \
  --runtime "NODE:18-lts" --location "West Europe"
```

**Monitoring & Diagnostics**
```bash
# Natural language input
"Check the health of my storage account and show recent logs"

# Generated Azure CLI
az storage account show --name mystorage --resource-group myRG \
  && az monitor diagnostic-settings list --resource /subscriptions/.../mystorage
```

### Development Strategy
- **Week 1-2**: Core NLP engine and basic command mapping
- **Week 3**: MVP release with essential Azure operations
- **Week 4-8**: Advanced features (context, batch ops, security)
- **Week 9-11**: Testing, documentation, and performance optimization
- **Week 12**: v1.0 production release with full feature set
