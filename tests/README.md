# Testing Guide for Azure Copilot

## 🎯 Your Pomodoro 1 Task

Implement the TODOs in the test files to learn pytest and testing patterns!

## 📁 Files Created

```
tests/
├── __init__.py           # Makes this a Python package
├── conftest.py           # Pytest fixtures (test helpers)
├── test_config.py        # Tests for config.py
├── test_cli.py           # Tests for cli.py
└── README.md            # This file
```

## 🚀 Getting Started

### Step 1: Setup Your .env File

Before running tests, create your `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your Azure subscription ID:
```bash
AZURE_SUBSCRIPTION_ID=your-subscription-id-here
```

Get your subscription ID:
```bash
az login
az account show --query id -o tsv
```

### Step 2: Run Tests (They'll Fail - That's Expected!)

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=.

# Run a specific test file
pytest tests/test_config.py -v

# Run a specific test function
pytest tests/test_config.py::test_config_loads_subscription_id -v
```

You'll see lots of failures because tests are not implemented (just `pass` statements).

### Step 3: Implement TODOs One By One

Start with `test_config.py` - it's the easiest!

Pick ONE test function, read the TODO comments, and implement it.

## 📚 Learning Resources

### Pytest Basics
- **Official Tutorial**: https://docs.pytest.org/en/stable/getting-started.html
- **Assertions**: https://docs.pytest.org/en/stable/how-to/assert.html
- **Fixtures**: https://docs.pytest.org/en/stable/how-to/fixtures.html

### Key Concepts to Learn

1. **Writing Tests**
   ```python
   def test_something():
       result = my_function()
       assert result == expected_value
   ```

2. **Using Fixtures**
   ```python
   def test_with_fixture(cli_runner):  # pytest injects cli_runner
       result = cli_runner.invoke(cli, ["help"])
       assert result.exit_code == 0
   ```

3. **Mocking Environment Variables**
   ```python
   def test_config(monkeypatch):
       monkeypatch.setenv("MY_VAR", "test_value")
       # Now os.getenv("MY_VAR") returns "test_value"
   ```

4. **Testing Exceptions**
   ```python
   def test_raises_error():
       with pytest.raises(ValueError):
           my_function_that_should_fail()
   ```

## 🎓 Suggested Learning Order

### Easy Tests (Start Here!)
1. `test_config.py::test_config_loads_subscription_id`
2. `test_config.py::test_config_loads_default_location`
3. `test_cli.py::test_help_command_recognized`
4. `test_cli.py::test_cli_shows_command_in_output`

### Medium Tests
5. `test_config.py::test_config_raises_error_without_subscription_id`
6. `test_config.py::test_get_authentication_method`
7. `test_cli.py::test_list_resources_command_recognized`
8. `test_cli.py::test_unknown_command_shows_error`

### Advanced Tests (Challenge Yourself!)
9. `test_config.py::test_is_service_principal_configured_returns_true_with_credentials`
10. `test_cli.py::test_list_command_variations`
11. Implement the BONUS tests if you have time

## 🧪 Example: First Test Implementation

Here's how to implement the first test in `test_config.py`:

```python
def test_config_loads_subscription_id(mock_env_vars):
    """Test that Config loads AZURE_SUBSCRIPTION_ID from environment."""

    # The mock_env_vars fixture already set this to "00000000-0000-0000-0000-000000000000"
    from config import Config

    config = Config()

    # Assert it loaded correctly
    assert config.subscription_id == "00000000-0000-0000-0000-000000000000"
    assert config.subscription_id != ""  # Not empty
    assert len(config.subscription_id) == 36  # UUID format
```

Now run it:
```bash
pytest tests/test_config.py::test_config_loads_subscription_id -v
```

You should see: ✅ **PASSED**

## 🎯 Success Criteria for Pomodoro 1

By the end of 30 minutes, you should have:

- [ ] Created `.env` file with your subscription ID
- [ ] Run `pytest` and seen test failures
- [ ] Implemented at least 3-5 tests in `test_config.py`
- [ ] Implemented at least 2-3 tests in `test_cli.py`
- [ ] Seen some tests turn from ❌ to ✅
- [ ] Understood how fixtures work (even if basic)
- [ ] Used `assert`, `monkeypatch.setenv()`, and `pytest.raises()`

## 💡 Tips

1. **Start Simple**: Implement the easiest tests first to build confidence
2. **Run Often**: Run `pytest` after each test you implement
3. **Read Error Messages**: Pytest gives helpful error messages
4. **Use `-v` Flag**: Verbose output shows you exactly which tests pass/fail
5. **Don't Worry About Perfection**: The goal is learning, not perfect tests
6. **Google Is Your Friend**: Search "pytest how to X" for anything confusing

## 🐛 Common Issues

**Issue**: Tests fail with "Config error" about missing subscription ID
**Solution**: The `mock_env_vars` fixture should set it automatically. Check that conftest.py is being loaded.

**Issue**: `ModuleNotFoundError: No module named 'config'`
**Solution**: Run tests from the project root directory, not from inside `tests/`

**Issue**: Can't import `cli` or `config`
**Solution**: Make sure you've installed the project in editable mode: `pip install -e .`

## 📊 Checking Coverage

See which lines of code are tested:

```bash
pytest tests/ --cov=. --cov-report=html
open htmlcov/index.html  # On macOS
```

Green lines = tested, red lines = not tested

## 🎉 Next Steps (Pomodoro 2)

After you complete Pomodoro 1, we'll:
- Implement actual Azure operations in `azure_commands.py`
- Test them using the `mock_resource_client` fixture
- Connect real Azure SDK to your CLI

But for now: **Focus on learning pytest basics by implementing the TODOs!**

---

Good luck! Remember: The goal is to **learn by doing**, not to have perfect tests. Start with one test, make it pass, celebrate, then move to the next one! 🚀
