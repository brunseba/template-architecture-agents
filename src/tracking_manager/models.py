"""Pydantic models for documentation tracking."""

from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field, field_validator, model_validator


class Mapping(BaseModel):
    """Input-output mapping for documentation generation.
    
    Supports both single and multiple input/output files.
    """

    inputs: list[str] = Field(..., description="List of input file paths", min_length=1)
    outputs: list[str] = Field(..., description="List of output file paths", min_length=1)
    description: str = Field(..., description="Transformation description")
    input_hashes: Optional[dict[str, str]] = Field(
        None, description="SHA-256 hashes of input files (filename -> hash)"
    )
    output_hashes: Optional[dict[str, str]] = Field(
        None, description="SHA-256 hashes of output files (filename -> hash)"
    )
    
    # Backward compatibility fields (deprecated)
    input: Optional[str] = Field(None, exclude=True, description="Deprecated: use inputs")
    output: Optional[str] = Field(None, exclude=True, description="Deprecated: use outputs")
    input_hash: Optional[str] = Field(None, exclude=True, description="Deprecated: use input_hashes")
    output_hash: Optional[str] = Field(None, exclude=True, description="Deprecated: use output_hashes")
    
    @model_validator(mode='before')
    @classmethod
    def handle_backward_compatibility(cls, data: dict) -> dict:
        """Handle backward compatibility for old single-file format."""
        if isinstance(data, dict):
            # Convert old single-file format to new multi-file format
            if 'input' in data and 'inputs' not in data:
                data['inputs'] = [data['input']]
            if 'output' in data and 'outputs' not in data:
                data['outputs'] = [data['output']]
            if 'input_hash' in data and data['input_hash'] and 'input_hashes' not in data:
                # Use the input filename as the key
                input_file = data.get('input') or (data['inputs'][0] if 'inputs' in data else None)
                if input_file:
                    data['input_hashes'] = {input_file: data['input_hash']}
            if 'output_hash' in data and data['output_hash'] and 'output_hashes' not in data:
                # Use the output filename as the key
                output_file = data.get('output') or (data['outputs'][0] if 'outputs' in data else None)
                if output_file:
                    data['output_hashes'] = {output_file: data['output_hash']}
        return data


class Generation(BaseModel):
    """Documentation generation metadata."""

    commit_id: str = Field(..., description="Git commit hash")
    timestamp: datetime = Field(..., description="Generation timestamp")
    generator: str = Field(..., description="Generator tool name")
    mappings: list[Mapping] = Field(..., description="Input-output mappings")


class HistoryEntry(BaseModel):
    """Historical tracking entry."""

    commit_id: str = Field(..., description="Git commit hash")
    timestamp: datetime = Field(..., description="Timestamp")
    version: str = Field(..., description="Version number")
    changes: list[str] = Field(default_factory=list, description="List of changes")


class TrackingData(BaseModel):
    """Complete tracking data structure."""

    version: str = Field(..., description="Tracking data format version")
    last_generation: Generation = Field(..., description="Most recent generation")
    history: list[HistoryEntry] = Field(..., description="Historical entries")
