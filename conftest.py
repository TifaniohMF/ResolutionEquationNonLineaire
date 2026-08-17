"""Garantit que le package `src` est importable quel que soit le
répertoire depuis lequel pytest est lancé."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
