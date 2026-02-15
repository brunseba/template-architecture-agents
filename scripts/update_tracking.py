#!/usr/bin/env python3
"""Update tracking file with current commit and timestamp."""

import sys
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tracking_manager.models import Generation, HistoryEntry
from tracking_manager.utils import (
    get_current_commit,
    load_tracking_data,
    save_tracking_data,
)


def main():
    """Update tracking file with current git state."""
    try:
        print("Updating tracking file...")

        data = load_tracking_data()
        commit_id = get_current_commit()
        timestamp = datetime.now()

        # Update last generation commit and timestamp
        data.last_generation.commit_id = commit_id
        data.last_generation.timestamp = timestamp

        # Add to history
        data.history.append(
            HistoryEntry(
                commit_id=commit_id,
                timestamp=timestamp,
                version=data.version,
                changes=["Updated tracking metadata"],
            )
        )

        save_tracking_data(data)
        print(f"✓ Updated tracking file (commit: {commit_id})")
        return 0

    except Exception as e:
        print(f"✗ Error updating tracking file: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
