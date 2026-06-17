# Changelog — conflict-arbiter

> 版本变更记录。参见 ROADMAP.md 了解技术改进路线图。

## v1.1.0 — 2026-06-27

### 🌐 IUCN/CITES API 客户端 + CLI 工具

- 🌐 **IUCN API 客户端**: `src/api_clients.py` — IUCNClient (Red List API v4: 评估/栖息地/威胁)
- 📋 **CITES API 客户端**: `src/api_clients.py` — CITESClient (Species+ Checklist API: 附录列名/分布)
- 🛠️ **CLI 仲裁工具**: `scripts/arbitrate.py` — 命令行 `python scripts/arbitrate.py "Coilia nasus"`
- 🔗 Arbiter.realtime_arbitrate() 集成 IUCN/CITES 实时 API 数据源

---

## v1.0.0 — 2026-06-07
- 初始发布 — 三段式仲裁 · 中国区域策略 · 熔断保护
