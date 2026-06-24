"""conflict-arbiter — 冲突仲裁者 (C/V4, 火 🟥)

热点冲突分析：不同数据源对同一物种的保护推荐冲突时做熔断/仲裁。

五行: 火 🟥
角色: C (Conflict) → V4 (ArbitrateVertex)
专精: 矛盾检测 + 可信度加权仲裁 + 熔断逻辑
"""

import sys as _sys
from pathlib import Path as _Path
_PROJECT_ROOT = str(_Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in _sys.path:
    _sys.path.insert(0, _PROJECT_ROOT)

def _load_version():
    """Read version from VERSION.yaml — single source of truth."""
    try:
        import yaml
        _vpath = _Path(__file__).resolve().parent.parent.parent / "VERSION.yaml"
        with open(_vpath, encoding="utf-8") as _f:
            _data = yaml.safe_load(_f)
        _key = _Path(__file__).resolve().parent.parent.name
        return _data.get("projects", {}).get(_key, {}).get("version", "0.0.0")
    except Exception:
        return "0.0.0"

__version__ = _load_version()
