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
__version__ = "1.0.0"
