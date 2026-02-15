"""Tests for documentation tracking system."""

import json
from datetime import datetime
from pathlib import Path

import pytest

from tracking_manager.models import Generation, HistoryEntry, Mapping, TrackingData
from tracking_manager.utils import hash_file, validate_tracking_file


class TestModels:
    """Test Pydantic models."""

    def test_mapping_creation(self):
        """Test creating a mapping with new multi-file format."""
        mapping = Mapping(
            inputs=["inputs/test.csv"],
            outputs=["docs/test.md"],
            description="Test mapping",
        )
        assert mapping.inputs == ["inputs/test.csv"]
        assert mapping.outputs == ["docs/test.md"]
        assert mapping.description == "Test mapping"
    
    def test_multi_file_mapping_creation(self):
        """Test creating a mapping with multiple files."""
        mapping = Mapping(
            inputs=["inputs/file1.csv", "inputs/file2.json"],
            outputs=["docs/out1.md", "docs/out2.md"],
            description="Multi-file mapping",
        )
        assert len(mapping.inputs) == 2
        assert len(mapping.outputs) == 2
        assert mapping.inputs[0] == "inputs/file1.csv"
        assert mapping.outputs[1] == "docs/out2.md"
    
    def test_backward_compatibility_single_file(self):
        """Test backward compatibility with old single-file format."""
        # Old format with 'input' and 'output' fields
        old_format_data = {
            "input": "inputs/test.csv",
            "output": "docs/test.md",
            "description": "Test mapping",
        }
        mapping = Mapping.model_validate(old_format_data)
        
        # Should be converted to new format
        assert mapping.inputs == ["inputs/test.csv"]
        assert mapping.outputs == ["docs/test.md"]
        assert mapping.description == "Test mapping"

    def test_mapping_with_hash(self):
        """Test mapping with hashes in new format."""
        mapping = Mapping(
            inputs=["inputs/test.csv"],
            outputs=["docs/test.md"],
            description="Test mapping",
            input_hashes={"inputs/test.csv": "a" * 64},
            output_hashes={"docs/test.md": "b" * 64},
        )
        assert mapping.input_hashes["inputs/test.csv"] == "a" * 64
        assert mapping.output_hashes["docs/test.md"] == "b" * 64
    
    def test_backward_compatibility_with_hash(self):
        """Test backward compatibility for old hash format."""
        old_format_data = {
            "input": "inputs/test.csv",
            "output": "docs/test.md",
            "description": "Test mapping",
            "input_hash": "a" * 64,
            "output_hash": "b" * 64,
        }
        mapping = Mapping.model_validate(old_format_data)
        
        # Should be converted to new format
        assert mapping.inputs == ["inputs/test.csv"]
        assert mapping.outputs == ["docs/test.md"]
        assert mapping.input_hashes == {"inputs/test.csv": "a" * 64}
        assert mapping.output_hashes == {"docs/test.md": "b" * 64}

    def test_generation_creation(self):
        """Test creating a generation."""
        generation = Generation(
            commit_id="abc1234",
            timestamp=datetime.now(),
            generator="test",
            mappings=[
                Mapping(
                    inputs=["inputs/test.csv"],
                    outputs=["docs/test.md"],
                    description="Test",
                )
            ],
        )
        assert generation.commit_id == "abc1234"
        assert generation.generator == "test"
        assert len(generation.mappings) == 1

    def test_tracking_data_creation(self):
        """Test creating tracking data."""
        data = TrackingData(
            version="1.0.0",
            last_generation=Generation(
                commit_id="abc1234",
                timestamp=datetime.now(),
                generator="test",
                mappings=[],
            ),
            history=[],
        )
        assert data.version == "1.0.0"
        assert len(data.history) == 0


class TestUtils:
    """Test utility functions."""

    def test_hash_file(self, tmp_path):
        """Test file hashing."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content")

        hash_val = hash_file(test_file)
        assert len(hash_val) == 64
        assert all(c in "0123456789abcdef" for c in hash_val)

    def test_hash_file_consistency(self, tmp_path):
        """Test that same content produces same hash."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content")

        hash1 = hash_file(test_file)
        hash2 = hash_file(test_file)
        assert hash1 == hash2

    def test_hash_file_different_content(self, tmp_path):
        """Test that different content produces different hash."""
        file1 = tmp_path / "test1.txt"
        file2 = tmp_path / "test2.txt"
        file1.write_text("content 1")
        file2.write_text("content 2")

        hash1 = hash_file(file1)
        hash2 = hash_file(file2)
        assert hash1 != hash2


class TestTrackingFile:
    """Test tracking file operations."""

    def test_tracking_file_exists(self):
        """Test that tracking file exists."""
        tracking_file = Path(".docs-tracking.json")
        assert tracking_file.exists(), "Tracking file should exist"

    def test_tracking_file_valid_json(self):
        """Test that tracking file is valid JSON."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)
        assert isinstance(data, dict)

    def test_tracking_file_has_required_fields(self):
        """Test that tracking file has required fields."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)

        assert "version" in data
        assert "last_generation" in data
        assert "history" in data

    def test_tracking_file_validates(self):
        """Test that tracking file passes validation."""
        is_valid, error = validate_tracking_file()
        assert is_valid, f"Tracking file validation failed: {error}"

    def test_version_format(self):
        """Test that version follows semver."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)

        version = data["version"]
        parts = version.split(".")
        assert len(parts) == 3, "Version should be in format X.Y.Z"
        assert all(part.isdigit() for part in parts), "Version parts should be numeric"

    def test_commit_id_format(self):
        """Test that commit IDs are valid git hashes."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)

        commit_id = data["last_generation"]["commit_id"]
        assert len(commit_id) >= 7, "Commit ID should be at least 7 characters"
        assert all(c in "0123456789abcdef" for c in commit_id), "Commit ID should be hex"

    def test_mappings_exist(self):
        """Test that mappings are present."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)

        mappings = data["last_generation"]["mappings"]
        assert len(mappings) > 0, "Should have at least one mapping"

    def test_mapped_files_exist(self):
        """Test that mapped input and output files exist."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)

        for mapping in data["last_generation"]["mappings"]:
            # Handle both old and new formats
            inputs = mapping.get("inputs") or [mapping.get("input")]
            outputs = mapping.get("outputs") or [mapping.get("output")]
            
            for input_file in inputs:
                if input_file:  # Skip None values
                    input_path = Path(input_file)
                    assert input_path.exists(), f"Input file should exist: {input_file}"
            
            for output_file in outputs:
                if output_file:  # Skip None values
                    output_path = Path(output_file)
                    assert output_path.exists(), f"Output file should exist: {output_file}"


class TestIntegrity:
    """Test data integrity."""

    def test_history_chronological(self):
        """Test that history entries are in chronological order."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)

        history = data["history"]
        if len(history) > 1:
            timestamps = [
                datetime.fromisoformat(entry["timestamp"]) for entry in history
            ]
            for i in range(len(timestamps) - 1):
                assert (
                    timestamps[i] <= timestamps[i + 1]
                ), "History should be in chronological order"

    def test_no_duplicate_mappings(self):
        """Test that there are no duplicate input-output mappings."""
        tracking_file = Path(".docs-tracking.json")
        with open(tracking_file) as f:
            data = json.load(f)

        mappings = data["last_generation"]["mappings"]
        # Handle both old and new formats
        pairs = []
        for m in mappings:
            inputs = tuple(m.get("inputs") or [m.get("input")])
            outputs = tuple(m.get("outputs") or [m.get("output")])
            pairs.append((inputs, outputs))
        
        assert len(pairs) == len(set(pairs)), "Should not have duplicate mappings"
