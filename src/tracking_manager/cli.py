"""CLI for documentation tracking management."""

from datetime import datetime
from pathlib import Path

import click

from .models import Generation, HistoryEntry, Mapping, TrackingData
from .utils import (
    check_files_in_sync,
    format_timestamp,
    get_current_commit,
    hash_file,
    load_tracking_data,
    save_tracking_data,
    validate_tracking_file,
)


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Documentation tracking and validation system."""
    pass


@cli.command()
@click.argument("input_files", nargs=-1, required=True, type=click.Path(exists=True))
@click.option("--output", "-o", "output_files", multiple=True, required=True, type=click.Path(), help="Output file path(s)")
@click.option("--description", "-d", required=True, help="Description of the transformation")
@click.option("--generator", "-g", default="warp-ai", help="Generator tool name")
@click.option("--with-hash", is_flag=True, help="Include file hashes in tracking")
def track(input_files: tuple[str, ...], output_files: tuple[str, ...], description: str, generator: str, with_hash: bool):
    """Track a new input-output mapping.
    
    Supports both single and multiple input/output files.
    
    Examples:
      track input.csv -o output.md -d "Generate docs"
      track file1.csv file2.json -o out1.md -o out2.md -d "Multi-file transform"
    """
    try:
        # Convert tuples to lists
        input_list = list(input_files)
        output_list = list(output_files)
        
        # Load existing tracking data or create new
        try:
            data = load_tracking_data()
        except FileNotFoundError:
            click.echo("Creating new tracking file...")
            data = TrackingData(
                version="1.0.0",
                last_generation=Generation(
                    commit_id=get_current_commit(),
                    timestamp=datetime.now(),
                    generator=generator,
                    mappings=[],
                ),
                history=[],
            )

        # Create new mapping with multiple files
        input_paths = [Path(f) for f in input_list]
        output_paths = [Path(f) for f in output_list]

        mapping = Mapping(
            inputs=[str(p) for p in input_paths],
            outputs=[str(p) for p in output_paths],
            description=description,
        )

        if with_hash:
            input_hashes = {}
            output_hashes = {}
            
            for input_path in input_paths:
                if input_path.exists():
                    input_hashes[str(input_path)] = hash_file(input_path)
            
            for output_path in output_paths:
                if output_path.exists():
                    output_hashes[str(output_path)] = hash_file(output_path)
            
            if input_hashes:
                mapping.input_hashes = input_hashes
            if output_hashes:
                mapping.output_hashes = output_hashes

        # Update tracking data
        commit_id = get_current_commit()
        timestamp = datetime.now()

        # Format file lists for history
        input_str = ", ".join(input_list)
        output_str = ", ".join(output_list)
        change_msg = f"Added mapping: [{input_str}] -> [{output_str}]"

        # Add to history
        data.history.append(
            HistoryEntry(
                commit_id=commit_id,
                timestamp=timestamp,
                version=data.version,
                changes=[change_msg],
            )
        )

        # Update last generation
        data.last_generation = Generation(
            commit_id=commit_id,
            timestamp=timestamp,
            generator=generator,
            mappings=data.last_generation.mappings + [mapping],
        )

        save_tracking_data(data)
        click.echo(f"✓ Tracked mapping:")
        click.echo(f"  Inputs:  {input_str}")
        click.echo(f"  Outputs: {output_str}")
        click.echo(f"  Commit:  {commit_id}")

    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort()


@cli.command()
def validate():
    """Validate tracking file against schema."""
    click.echo("Validating tracking file...")

    is_valid, error = validate_tracking_file()

    if is_valid:
        click.echo("✓ Tracking file is valid")
        return 0
    else:
        click.echo(f"✗ Validation failed: {error}", err=True)
        return 1


@cli.command()
def sync():
    """Check if tracked files are in sync."""
    click.echo("Checking file synchronization...")

    in_sync, issues = check_files_in_sync()

    if in_sync:
        click.echo("✓ All tracked files are in sync")
        return 0
    else:
        click.echo(f"✗ Found {len(issues)} issue(s):", err=True)
        for issue in issues:
            click.echo(f"  - {issue}", err=True)
        return 1


@cli.command()
@click.option("--limit", "-n", default=10, help="Number of entries to show")
def history(limit: int):
    """Show tracking history."""
    try:
        data = load_tracking_data()

        click.echo(f"\n{'='*70}")
        click.echo(f"Documentation Tracking History (last {limit} entries)")
        click.echo(f"{'='*70}\n")

        for i, entry in enumerate(reversed(data.history[-limit:]), 1):
            click.echo(f"{i}. Commit: {entry.commit_id}")
            click.echo(f"   Time:   {format_timestamp(entry.timestamp)}")
            click.echo(f"   Version: {entry.version}")
            if entry.changes:
                click.echo("   Changes:")
                for change in entry.changes:
                    click.echo(f"     - {change}")
            click.echo()

    except FileNotFoundError:
        click.echo("✗ No tracking file found", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort()


@cli.command()
def migrate():
    """Migrate tracking file from old single-file format to new multi-file format.
    
    This command reads the existing tracking file and saves it back with the new format.
    The Pydantic model automatically handles the conversion from old to new format.
    """
    try:
        click.echo("Migrating tracking file to multi-file format...")
        
        # Load with backward compatibility
        data = load_tracking_data()
        
        # Save with new format
        save_tracking_data(data)
        
        click.echo("✓ Migration complete!")
        click.echo(f"  Migrated {len(data.last_generation.mappings)} mapping(s)")
        
        # Show what was migrated
        for i, mapping in enumerate(data.last_generation.mappings, 1):
            inputs_str = ", ".join(mapping.inputs)
            outputs_str = ", ".join(mapping.outputs)
            click.echo(f"  {i}. [{inputs_str}] -> [{outputs_str}]")
        
    except FileNotFoundError:
        click.echo("✗ No tracking file found", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"✗ Migration failed: {e}", err=True)
        raise click.Abort()


@cli.command()
def status():
    """Show current tracking status."""
    try:
        data = load_tracking_data()

        click.echo(f"\n{'='*70}")
        click.echo("Documentation Tracking Status")
        click.echo(f"{'='*70}\n")

        click.echo(f"Version:        {data.version}")
        click.echo(f"Last Update:    {format_timestamp(data.last_generation.timestamp)}")
        click.echo(f"Last Commit:    {data.last_generation.commit_id}")
        click.echo(f"Generator:      {data.last_generation.generator}")
        click.echo(f"Total Mappings: {len(data.last_generation.mappings)}")
        click.echo(f"History Items:  {len(data.history)}\n")

        click.echo("Current Mappings:")
        for i, mapping in enumerate(data.last_generation.mappings, 1):
            # Format inputs and outputs
            inputs_str = ", ".join(mapping.inputs) if len(mapping.inputs) > 1 else mapping.inputs[0]
            outputs_str = ", ".join(mapping.outputs) if len(mapping.outputs) > 1 else mapping.outputs[0]
            
            if len(mapping.inputs) > 1 or len(mapping.outputs) > 1:
                click.echo(f"  {i}. Multi-file mapping:")
                click.echo(f"     Inputs:  [{inputs_str}]")
                click.echo(f"     Outputs: [{outputs_str}]")
            else:
                click.echo(f"  {i}. {inputs_str} -> {outputs_str}")
            click.echo(f"     {mapping.description}")

        click.echo()

        # Check sync status
        in_sync, issues = check_files_in_sync()
        if in_sync:
            click.echo("✓ All files in sync")
        else:
            click.echo(f"⚠ {len(issues)} file(s) out of sync")

    except FileNotFoundError:
        click.echo("✗ No tracking file found", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort()


if __name__ == "__main__":
    cli()
