.PHONY: help install install-dev test lint format validate sync status clean docs

# Default target
help:
	@echo "Available targets:"
	@echo "  install       Install package with uv"
	@echo "  install-dev   Install package with dev dependencies"
	@echo "  test          Run tests with pytest"
	@echo "  lint          Run linting with ruff"
	@echo "  format        Format code with ruff"
	@echo "  validate      Validate tracking file"
	@echo "  sync          Check documentation synchronization"
	@echo "  status        Show tracking status"
	@echo "  docs          Generate documentation"
	@echo "  clean         Clean build artifacts"
	@echo "  pre-commit    Install pre-commit hooks"

# Installation
install:
	uv pip install -e .

install-dev:
	uv pip install -e ".[dev]"
	pre-commit install

# Testing
test:
	pytest tests/ -v --cov=src --cov-report=term-missing

test-fast:
	pytest tests/ -v -x

# Linting and formatting
lint:
	ruff check src/ tests/ scripts/

format:
	ruff format src/ tests/ scripts/
	ruff check --fix src/ tests/ scripts/

# Tracking operations
validate:
	@python scripts/validate_tracking.py

sync:
	@python scripts/check_docs_sync.py

status:
	@track status

update:
	@python scripts/update_tracking.py

# Documentation
docs:
	@echo "Generating documentation..."
	@echo "Note: Implement your documentation generation logic here"

# Pre-commit
pre-commit:
	pre-commit install
	@echo "Pre-commit hooks installed successfully"

pre-commit-run:
	pre-commit run --all-files

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".coverage" -delete

# Development workflow
dev: install-dev pre-commit
	@echo "Development environment ready!"

# CI workflow
ci: lint test validate sync
	@echo "CI checks passed!"
