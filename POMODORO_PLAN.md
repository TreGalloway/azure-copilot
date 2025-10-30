# 🍅 4-Pomodoro Plan: Azure Copilot Week 1

**Goal**: Get real Azure operations working with safety features and tests

---

## ✅ Pomodoro 1: Project Assessment & Planning (COMPLETED)
**Duration**: 30 minutes
**Status**: ✅ Done

### What We Did
- Reviewed current project state
- Identified what's already built (pyproject.toml, config.py, .env.example)
- Identified what's missing (tests, Azure operations)
- Created revised 4-pomodoro plan based on actual state
- Aligned on learning approach (you implement, I provide boilerplate)

### Deliverables
✅ Understanding of current project state
✅ Clear 4-session roadmap
✅ Agreed on learning methodology

---

## 🔄 Pomodoro 2: Learning pytest & Test Implementation (CURRENT)
**Duration**: 30 minutes
**Status**: 🔄 In Progress

### Your Tasks
1. **Setup (5 min)**
   - Create `.env` file from `.env.example`
   - Add your Azure subscription ID
   - Run `pytest tests/ -v` to see baseline

2. **Learn & Implement (20 min)**
   - Read `tests/README.md` for guidance
   - Implement TODOs in `test_config.py` (start here - easiest)
   - Implement TODOs in `test_cli.py`
   - Run tests frequently to see progress

3. **Stretch Goals (5 min)**
   - Complete `conftest.py` TODOs (fixture implementations)
   - Run coverage: `pytest tests/ --cov=.`

### Learning Objectives
- Understand pytest fixtures and how they work
- Learn `assert` statements and test structure
- Practice `monkeypatch` for environment variables
- Use `pytest.raises()` for exception testing
- Test CLI commands with `CliRunner`

### Success Criteria
- [ ] `.env` file created with real subscription ID
- [ ] 5+ tests implemented in `test_config.py`
- [ ] 3+ tests implemented in `test_cli.py`
- [ ] At least 1 test passing (green ✅)
- [ ] Understand what fixtures do and why we use them

### Resources
- `tests/README.md` - Your main guide with examples
- https://docs.pytest.org/en/stable/getting-started.html
- https://click.palletsprojects.com/en/8.1.x/testing/
- TODO comments in each test file

---

## 🍅 Pomodoro 3: Azure SDK Integration & First Operations
**Duration**: 30 minutes
**Status**: ⏳ Pending

### What I'll Generate
- `azure_commands.py` with:
  - `list_resource_groups()` - Async function with Azure SDK
  - Input validation helpers
  - Error handling patterns
  - Type hints and docstrings
- Helper functions in `config.py` for creating Azure clients
- Rich Console table formatters for output

### What You'll Implement
- Wire up `list_resource_groups()` to `cli.py`
- Test authentication with `az login`
- Run: `python cli.py "list resource groups"`
- Debug any authentication issues
- See your actual Azure resource groups displayed in a pretty table

### Learning Objectives
- Azure SDK patterns (`DefaultAzureCredential`, `ResourceManagementClient`)
- Async/await in Python
- Error handling for Azure API calls
- Rich Console table formatting

### Success Criteria
- [ ] Azure authentication working (`az login` or service principal)
- [ ] CLI successfully lists your real resource groups
- [ ] Output formatted as a Rich Console table
- [ ] Error messages are helpful (not stack traces)
- [ ] Code has type hints on all functions

### Key Files Modified
- `azure_commands.py` - Azure SDK operations
- `cli.py` - Connect commands to Azure operations
- `config.py` - Azure client creation helpers

---

## 🍅 Pomodoro 4: Safety Features & Create Operations
**Duration**: 30 minutes
**Status**: ⏳ Pending

### What I'll Generate
- `--dry-run` flag implementation in `cli.py`
- `--force` flag to skip confirmations
- `create_resource_group()` function in `azure_commands.py`
- Confirmation prompt helpers with Rich styling
- Resource name validation (Azure naming rules)
- Tests for safety features (`tests/test_azure_commands.py`)

### What You'll Implement
- Wire up create command to CLI
- Test dry-run mode: `copilot "create rg called test-rg in eastus" --dry-run`
- Test confirmation flow: `copilot "create rg called test-rg in eastus"`
- Actually create a resource group in Azure
- Verify it exists: `az group show -n test-rg`
- Clean up: `az group delete -n test-rg -y`

### Learning Objectives
- CLI flags with Click (`@click.option`)
- User confirmation patterns
- Input validation and sanitization
- Safety-first design principles
- Dry-run implementation patterns

### Success Criteria
- [ ] `--dry-run` flag shows what would happen (no actual changes)
- [ ] Confirmation prompt asks before creating resources
- [ ] `--force` flag skips confirmation (use carefully!)
- [ ] Can create a real resource group in Azure
- [ ] Resource names are validated (no invalid chars)
- [ ] Dry-run shows equivalent Azure CLI command
- [ ] Tests for safety features passing

### Commands You'll Test
```bash
# Dry-run (safe - shows what would happen)
copilot "create a resource group called test-rg in eastus" --dry-run

# Real creation (asks for confirmation)
copilot "create a resource group called test-rg in eastus"

# Skip confirmation (dangerous - use carefully!)
copilot "create a resource group called test-rg in eastus" --force
```

---

## 🎯 Overall Success Criteria (All 4 Pomodoros)

After 2 hours of focused work, you'll have:

### ✅ Functional Features
- [ ] Working test suite (10+ tests passing)
- [ ] Azure authentication configured
- [ ] List resource groups command working
- [ ] Create resource group command working
- [ ] Beautiful Rich Console output
- [ ] Safety checks (dry-run, confirmations)

### 📚 Knowledge Gained
- [ ] Pytest fundamentals (fixtures, assertions, mocking)
- [ ] Azure SDK usage patterns
- [ ] Click CLI framework
- [ ] Async/await in Python
- [ ] Type hints and modern Python
- [ ] Safety-first development practices

### 🏗️ Project Infrastructure
- [ ] Test directory structure (`tests/`)
- [ ] Pytest configuration in `pyproject.toml`
- [ ] Azure command implementations (`azure_commands.py`)
- [ ] Rich Console formatting
- [ ] Input validation helpers
- [ ] Error handling patterns

### 🔐 Safety Features
- [ ] No hardcoded credentials
- [ ] Dry-run mode for testing
- [ ] Confirmation prompts for destructive ops
- [ ] Input validation
- [ ] Helpful error messages

---

## 📊 Progress Tracking

| Pomodoro | Status | Key Deliverable | Time |
|----------|--------|----------------|------|
| 1 | ✅ Done | Project assessment & planning | 30m |
| 2 | 🔄 Current | pytest learning & test implementation | 30m |
| 3 | ⏳ Pending | Azure SDK integration | 30m |
| 4 | ⏳ Pending | Safety features & create operations | 30m |

---

## 🚀 Next Steps After Pomodoro 4

Once you complete these 4 sessions, you'll be ready for:

**Week 1 Remaining Work:**
- Add more Azure operations (delete, update resource groups)
- Implement VM listing (`copilot "show me all VMs"`)
- Add storage account operations
- Improve natural language parsing

**Week 2 (Next Pomodoros):**
- Comprehensive error handling
- Better command parsing (move beyond keyword matching)
- Command history and context
- More Azure resource types

**Week 3:**
- Azure OpenAI integration
- Intent classification
- Entity extraction
- Natural language understanding

---

## 💡 Tips for Success

1. **Stay Focused**: 30 minutes is short - minimize distractions
2. **Run Tests Often**: `pytest` after every change
3. **Read Error Messages**: They're usually helpful
4. **Google Freely**: "pytest how to X", "Azure SDK example"
5. **Don't Perfectionist**: Working > Perfect
6. **Take Breaks**: 5-10 min between pomodoros
7. **Ask Questions**: Come back if stuck

---

## 📝 Notes & Learnings

Use this space to track what you learned each session:

### Pomodoro 1 Notes
- Learned project structure and current state
- Understood the 4-session plan
- Ready to dive into pytest

### Pomodoro 2 Notes
<!-- Add your notes here after completing session 2 -->

### Pomodoro 3 Notes
<!-- Add your notes here after completing session 3 -->

### Pomodoro 4 Notes
<!-- Add your notes here after completing session 4 -->

---

**Current Focus**: 🍅 Pomodoro 2 - Learning pytest & implementing test TODOs

**Start Timer**: When ready, begin your 30-minute focused session!
