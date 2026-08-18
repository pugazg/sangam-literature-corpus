#!/usr/bin/env python3
"""Compatibility entry point for the exact R1.5/R1.5A 29-dimension gate.

The canonical implementation remains validate_r15_production_dimensions.py.
This shim preserves the command name used by the R1.5A workflow and active
continuity documentation without duplicating validator logic.
"""
from validate_r15_production_dimensions import main


if __name__ == "__main__":
    main()
