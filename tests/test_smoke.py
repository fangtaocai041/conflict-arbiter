"""Smoke test for conflict-arbiter imports and adapter."""
import sys
from pathlib import Path

_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)


def test_imports():
    from src import __version__
    from src.adapter import ConflictArbiterAdapter
    from src.arbiter import ConflictArbiter
    from src.rcca_core import SelfModelEngine
    print(f"[OK] conflict-arbiter v{__version__} imports OK")


def test_adapter():
    from src.adapter import ConflictArbiterAdapter
    adapter = ConflictArbiterAdapter()
    health = adapter.health()
    assert health["project"] == "conflict-arbiter"
    print(f"[OK] adapter health: {health['status']}")


if __name__ == "__main__":
    for name, fn in [("imports", test_imports), ("adapter", test_adapter)]:
        try:
            fn()
        except Exception as e:
            print(f"[FAIL] {name}: {e}")
            sys.exit(1)
    print(f"\n2/2 passed")
