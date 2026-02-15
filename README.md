# Documentation Tracking System

A comprehensive system for tracking and validating documentation generation from input sources.

## Features

- 📝 **Input-Output Tracking**: Maintain mappings between input files and generated documentation
- ✅ **Validation**: JSON schema validation and file synchronization checks
- 🔍 **History**: Track changes over time with git commit integration
- 🛠️ **CLI Tool**: Easy-to-use command-line interface
- 🧪 **Testing**: Comprehensive test suite with pytest
- 🔄 **CI/CD**: GitHub Actions workflow for automated validation
- 🎯 **Pre-commit Hooks**: Automatic validation before commits

## Quick Start

### Installation

```bash
# Install with uv (recommended)
make install-dev

# Or manually
uv pip install -e ".[dev]"
pre-commit install
```

### Basic Usage

```bash
# Check tracking status
track status

# Validate tracking file
track validate

# Check if files are in sync
track sync

# View history
track history

# Track a new mapping
track track inputs/data.csv docs/output.md -d "Generated from data"
```

## Project Structure

```
.
├── .docs-tracking.json          # Main tracking data file
├── pyproject.toml               # Project configuration
├── Makefile                     # Automation commands
├── schema/
│   └── tracking-schema.json     # JSON validation schema
├── src/
│   └── tracking_manager/
│       ├── __init__.py
│       ├── cli.py              # CLI commands
│       ├── models.py           # Pydantic models
│       └── utils.py            # Utility functions
├── scripts/
│   ├── validate_tracking.py    # Validation script
│   ├── update_tracking.py      # Update script
│   └── check_docs_sync.py      # Sync check script
├── tests/
│   └── test_tracking.py        # Test suite
└── .github/
    └── workflows/
        └── validate-docs.yml    # CI/CD workflow
```

## CLI Commands

### `track status`
Display current tracking status including version, last update, mappings, and sync status.

```bash
track status
```

### `track validate`
Validate the tracking file against the JSON schema.

```bash
track validate
```

### `track sync`
Check if tracked files are synchronized (no modifications since last tracking).

```bash
track sync
```

### `track history`
Show tracking history with commit information.

```bash
# Show last 10 entries
track history

# Show last 5 entries
track history --limit 5
```

### `track track`
Add a new input-output mapping to the tracking system.

```bash
track track INPUT OUTPUT -d "Description" [--with-hash] [--generator NAME]

# Example
track track inputs/uri.csv docs/tools-catalog.md -d "Tool descriptions" --with-hash
```

## Makefile Targets

```bash
make help          # Show all available targets
make install       # Install package
make install-dev   # Install with dev dependencies
make test          # Run tests
make lint          # Run linting
make format        # Format code
make validate      # Validate tracking file
make sync          # Check file synchronization
make status        # Show tracking status
make clean         # Clean build artifacts
make dev           # Setup dev environment
make ci            # Run all CI checks
```

## Development Workflow

### 1. Setup Development Environment

```bash
make dev
```

This will:
- Install the package with dev dependencies
- Install pre-commit hooks
- Set up your development environment

### 2. Make Changes

Edit files as needed. The pre-commit hooks will automatically:
- Validate tracking files on commit
- Check documentation synchronization
- Format code with ruff
- Check for common issues

### 3. Run Tests

```bash
# Run all tests
make test

# Run fast (fail-fast mode)
make test-fast
```

### 4. Validate Before Push

```bash
# Run all CI checks locally
make ci
```

## CI/CD Pipeline

The GitHub Actions workflow runs on every push and pull request:

1. **Validate**: Check tracking file against schema
2. **Sync Check**: Verify files are synchronized
3. **Tests**: Run full test suite with coverage
4. **Lint**: Check code quality with ruff
5. **Integration**: Test CLI commands
6. **Security**: Scan for vulnerabilities with Trivy

## Tracking File Format

The `.docs-tracking.json` file contains:

```json
{
  "version": "1.0.0",
  "last_generation": {
    "commit_id": "abc1234",
    "timestamp": "2026-02-14T20:00:00Z",
    "generator": "warp-ai",
    "mappings": [
      {
        "input": "inputs/uri.csv",
        "output": "docs/tools-catalog.md",
        "description": "Generated tool descriptions",
        "input_hash": "...",
        "output_hash": "..."
      }
    ]
  },
  "history": [
    {
      "commit_id": "abc1234",
      "timestamp": "2026-02-14T20:00:00Z",
      "version": "1.0.0",
      "changes": ["Initial release"]
    }
  ]
}
```

## Testing

The test suite includes:

- **Model Tests**: Pydantic model validation
- **Utility Tests**: File hashing and validation
- **Tracking File Tests**: Schema compliance and data integrity
- **Integration Tests**: End-to-end workflow testing

Run tests with:

```bash
pytest tests/ -v --cov=src
```

## Pre-commit Hooks

The following hooks run automatically:

- Trailing whitespace removal
- End-of-file fixes
- YAML/JSON validation
- Large file checks
- Merge conflict detection
- Ruff formatting and linting
- Tracking file validation
- Documentation sync check

Install hooks:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## Contributing

1. Create a feature branch
2. Make changes
3. Run `make ci` to validate
4. Commit with conventional commit format
5. Push and create PR

## License

See LICENSE file for details.

## Commits

- Initial tools catalog: `ad4712a`
- Tracking system implementation: `414b478`
- Full tracking tools: `a803248`
