#!/usr/bin/env python3
"""Check if documentation is in sync with inputs."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tracking_manager.utils import check_files_in_sync


def main():
    """Check synchronization and exit with appropriate code."""
    print("Checking documentation synchronization...")

    in_sync, issues = check_files_in_sync()

    if in_sync:
        print("✓ All tracked files are in sync")
        return 0
    else:
        print(f"✗ Found {len(issues)} issue(s):", file=sys.stderr)
        for issue in issues:
            print(f"  - {issue}", file=sys.stderr)
        print(
            "\nHint: Files may be out of sync. Consider regenerating documentation.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
