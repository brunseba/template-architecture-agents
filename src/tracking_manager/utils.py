"""Utility functions for tracking operations."""

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Optional

import git
from jsonschema import ValidationError, validate

from .models import TrackingData

TRACKING_FILE = ".docs-tracking.json"
SCHEMA_FILE = "schema/tracking-schema.json"


def get_repo() -> git.Repo:
    """Get the current git repository."""
    try:
        return git.Repo(".", search_parent_directories=True)
    except git.InvalidGitRepositoryError as e:
        raise RuntimeError("Not in a git repository") from e


def get_current_commit() -> str:
    """Get the current git commit hash (short)."""
    repo = get_repo()
    return repo.head.commit.hexsha[:7]


def hash_file(file_path: Path) -> str:
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_tracking_data() -> TrackingData:
    """Load and validate tracking data from file."""
    tracking_path = Path(TRACKING_FILE)
    if not tracking_path.exists():
        raise FileNotFoundError(f"Tracking file not found: {TRACKING_FILE}")

    with open(tracking_path) as f:
        data = json.load(f)

    return TrackingData.model_validate(data)


def save_tracking_data(data: TrackingData) -> None:
    """Save tracking data to file."""
    tracking_path = Path(TRACKING_FILE)
    with open(tracking_path, "w") as f:
        json.dump(data.model_dump(mode="json", exclude_none=True), f, indent=2, default=str)
        f.write("\n")


def validate_tracking_file() -> tuple[bool, Optional[str]]:
    """Validate tracking file against JSON schema."""
    try:
        tracking_path = Path(TRACKING_FILE)
        schema_path = Path(SCHEMA_FILE)

        if not tracking_path.exists():
            return False, f"Tracking file not found: {TRACKING_FILE}"

        if not schema_path.exists():
            return False, f"Schema file not found: {SCHEMA_FILE}"

        with open(tracking_path) as f:
            tracking_data = json.load(f)

        with open(schema_path) as f:
            schema = json.load(f)

        validate(instance=tracking_data, schema=schema)

        # Also validate with Pydantic
        TrackingData.model_validate(tracking_data)

        return True, None

    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except ValidationError as e:
        return False, f"Schema validation failed: {e.message}"
    except Exception as e:
        return False, f"Validation error: {e}"


def check_files_in_sync() -> tuple[bool, list[str]]:
    """Check if tracked files are in sync with their recorded hashes.
    
    Supports both single and multiple file mappings.
    """
    try:
        data = load_tracking_data()
        issues = []

        for mapping in data.last_generation.mappings:
            # Check all input files
            for input_file in mapping.inputs:
                input_path = Path(input_file)
                
                if not input_path.exists():
                    issues.append(f"Input file missing: {input_file}")
                    continue
                
                # Check hash if available
                if mapping.input_hashes and input_file in mapping.input_hashes:
                    current_hash = hash_file(input_path)
                    if current_hash != mapping.input_hashes[input_file]:
                        issues.append(
                            f"Input file modified since last generation: {input_file}"
                        )
            
            # Check all output files
            for output_file in mapping.outputs:
                output_path = Path(output_file)
                
                if not output_path.exists():
                    issues.append(f"Output file missing: {output_file}")
                    continue
                
                # Check hash if available
                if mapping.output_hashes and output_file in mapping.output_hashes:
                    current_hash = hash_file(output_path)
                    if current_hash != mapping.output_hashes[output_file]:
                        issues.append(
                            f"Output file modified since last generation: {output_file}"
                        )

        return len(issues) == 0, issues

    except Exception as e:
        return False, [f"Error checking sync: {e}"]


def format_timestamp(dt: datetime) -> str:
    """Format datetime for display."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")
