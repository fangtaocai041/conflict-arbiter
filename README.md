<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║   🔥  CONFLICT ARBITER  ·  C Arbitration Layer  ·  v1.0.1   ║
║  ─────────────────────────────────────────────────────────  ║
║  Multi-Source · Protection-Weighted · Circuit Breaker        ║
║     IUCN Red List · CITES · China Red List · Arbitration     ║
╚══════════════════════════════════════════════════════════════╝
```

<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

# 🔥 Conflict Arbiter · 冲突仲裁 (C)

> **Role**: C — Derived Conflict Arbitration layer in the SanShengWanWu S-T-V-P₁-P₂-P₃-C six-body architecture.
> **Problem**: When S (knowledge) and V (verification) disagree, or when multiple derived projects produce contradictory findings, who decides?
> **Solution**: C — multi-source, protection-level weighted, circuit-breaker-protected conflict arbitration.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.1-8b5cf6)]()
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB)]()
[![Conflict](https://img.shields.io/badge/Conflict-4_level-red)]()
[![China Weighted](https://img.shields.io/badge/China-Weighted-orange)]()
[![Circuit Breaker](https://img.shields.io/badge/Circuit_Breaker-yellow)]()
[![Triangle](https://img.shields.io/badge/Triangle-Powered-EC4899)]()
[![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/conflict-arbiter)

<p align="center">
  <a href="https://github.com/fangtaocai041/conflict-arbiter/stargazers"><img src="https://img.shields.io/github/stars/fangtaocai041/conflict-arbiter?style=social" alt="Stars"></a>
  <a href="https://github.com/fangtaocai041/conflict-arbiter/network/members"><img src="https://img.shields.io/github/forks/fangtaocai041/conflict-arbiter?style=social" alt="Forks"></a>
</p>

</div>

---

## 📑 Table of Contents

- [🔺 S-T-V-P₁-P₂-P₃-C Architecture Role: C (Conflict Arbitration)](#-s-t-v-p-p-p-c-architecture-role-c-conflict-arbitration)
- [📊 Self-Assessment](#-self-assessment)
- [📋 Version History](#-version-history)
- [🧩 What This Is](#-what-this-is)
- [🏛️ Philosophy](#-philosophy)
- [🚀 Quick Start](#-quick-start)
- [🏗️ Architecture](#-architecture)
- [✨ Features](#-features)
- [⚖ Arbitration Levels](#-arbitration-levels)
- [🔗 Ecosystem](#-ecosystem)
- [🗺️ Roadmap](#-roadmap)
- [📋 README Changelog](#-readme-changelog)
- [📜 License](#-license)

---

## 🔺 S-T-V-P₁-P₂-P₃-C Architecture Role: **C (Conflict Arbitration)**

> Six-body architecture: `fish(S) → cognitive(V) → eon-core(Coord)`, derived: `porpoise(P₁)` + `coilia(P₂)` + `culter(P₃)` + `conflict-arbiter(C)`.
> **C** is the conflict resolution layer — when multiple sources disagree on conservation status, taxonomic classification, or ecological findings, C arbitrates using protection-level weighting, source credibility scoring, and circuit breaker protection.

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

## 📊 Self-Assessment

| Dimension | Rating | Notes |
|-----------|:-----:|-------|
| ⚖ Arbitration Logic | ⭐⭐⭐⭐⭐ | 4-level conflict escalation with weighted verdict |
| 🌐 Multi-Source | ⭐⭐⭐⭐⭐ | IUCN API v4 + CITES Checklist API + China Red List + National Key Protected |
| 🛡️ Circuit Breaker | ⭐⭐⭐⭐⭐ | Prevents cascading failures from unreliable API sources |
| 📡 Triangle Integration | ⭐⭐⭐⭐⭐ | Receives claims from S, verification from V |
| 🧪 Test Coverage | ⭐⭐⭐⭐ | Script-level arbitration tests, expanding |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| **v1.0.1** | 2026-06-18 | README Restoration — full documentation from historical sessions |
| **v1.0.0** | 2026-06-17 | Initial release — IUCN API, CITES API, CLI tool, circuit breaker |

> **Latest**: v1.0.1 · 2026-06-18

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🧩 What This Is

**Conflict Arbiter** is the conflict resolution layer in the SanShengWanWu ecosystem. When fish-ecology-assistant says "this species is Endangered" but cognitive-search-engine finds a newer IUCN assessment saying "Vulnerable" — the arbiter steps in.

### Core Functions

| Function | Description |
|----------|-------------|
| **Multi-Source Aggregation** | IUCN Red List API v4 + CITES Species+ Checklist API + China Red List + National Key Protected Species List |
| **4-Level Conflict Classification** | INFORMATION → WARNING → CRITICAL → BLOCKING severity ladder |
| **China-Weighted Scoring** | Chinese sources receive weighting for domestic conservation decisions |
| **Circuit Breaker** | Prevents unreliable API sources from corrupting arbitration |
| **Protection-Level Arbitration** | When sources disagree on protection status, weighted voting resolves |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🏛️ Philosophy

> 🔥 Every contradiction carries the seeds of deeper truth.

**🌊 The River Flows** — Conservation statuses change. IUCN reassesses. National lists update. Today's "Endangered" may be tomorrow's "Vulnerable" — or "Critically Endangered." The arbiter tracks these shifts in real-time.

**🍂 Knowledge Drifts** — Different databases use different criteria. IUCN uses global population trends; China Red List uses domestic criteria. Neither is "wrong" — they're answering different questions. The arbiter contextualizes, not just compares.

**🌟 Emergence Patterns** — When 3+ independent sources independently converge on the same status change, that's an emergence signal — not just data noise.

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🚀 Quick Start

```bash
git clone https://github.com/fangtaocai041/conflict-arbiter.git
cd conflict-arbiter
pip install -e .

# Arbitrate a species
python -m conflict_arbiter arbitrate "Coilia nasus"

# Check IUCN status
python scripts/iucn_client.py --species "Neophocaena asiaeorientalis"

# Check CITES listing
python scripts/cites_client.py --species "Acipenser sinensis"
```

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🏗️ Architecture

```
S-T-V-P₁-P₂-P₃-C Architecture (coordinated by eon-core):

  S/V0  fish-ecology-assistant    → Knowledge Supply
  V/V1  cognitive-search-engine   → Search Verification
  Coord  eon-core                  → Coordination Hub

  P₁   porpoise-agent            → Porpoise Expert
  P₂   coilia-agent              → Coilia Expert
  P₃   culter-agent              → Culter Expert
  C     🔥 conflict-arbiter       → Conflict Arbitration — this project
```

### Internal Architecture

<details open><summary><b>📂 Internal File Tree</b></summary>

```
conflict-arbiter/
  src/
  ├── main.py                   CLI entry point
  ├── adapter.py                IProjectAdapter — triangle bridge
  └── agent/
      ├── orchestrator.py       ConflictOrchestrator — 4-level escalation
      ├── arbiter.py            Weighted voting + circuit breaker
      └── source_scorer.py      Multi-source credibility scoring
  scripts/
  ├── arbitrate.py              CLI conflict arbitration tool
  ├── iucn_client.py            IUCN Red List API v4 client
  ├── cites_client.py           CITES Species+ Checklist API client
  └── shared_types.py           Canonical ecosystem types
  config/
  ├── agent.yaml                Conflict agent configuration
  └── sources.yaml              Source credibility weights
  tests/
  ├── test_arbitration.py        Arbitration logic tests
  └── test_sources.py            Source weight tests
```

</details>

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## ✨ Features

<details open><summary><b>📋 Feature List</b></summary>

| Feature | Status | Description |
|---------|:------:|-------------|
| ⚖ 4-Level Conflict | ✅ | INFORMATION → WARNING → CRITICAL → BLOCKING escalation |
| 🌐 IUCN API Client | ✅ | IUCN Red List API v4 real-time assessment data |
| 📋 CITES API Client | ✅ | CITES Species+ Checklist API appendix listing |
| 🇨🇳 China Weighted | ✅ | China Red List + National Key Protected Species weighting |
| 🛡️ Circuit Breaker | ✅ | Prevents cascading failures from unreliable sources |
| 🛠️ CLI Tool | ✅ | `scripts/arbitrate.py` — command-line arbitration |
| 📡 Triangle Powered | ✅ | V0 knowledge + V1 search + Coord orchestration |
| 🧠 Cognitive Loop | ✅ | ReAct pattern for iterative conflict analysis |

</details>

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## ⚖ Arbitration Levels

| Level | Trigger | Response |
|:-----:|---------|----------|
| **INFORMATION** | Minor discrepancy (e.g., year difference) | Log + notify |
| **WARNING** | Status disagreement across sources | Weighted vote + report |
| **CRITICAL** | Protection level conflict (e.g., EN vs VU) | Deep investigation + recommendation |
| **BLOCKING** | Fundamental contradiction (e.g., species ID conflict) | Halt pipeline + human review |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🔗 Ecosystem

This project is the **Conflict Arbitration Engine (C)** in the SanShengWanWu ecosystem.

```
Triangle Core (sealed 3):
  📦 fish-ecology-assistant    → Knowledge Supply (V0)
  🔍 cognitive-search-engine   → Search Verification (V1)
  ⚙ eon-core                  → Coordination Hub (Coord)

Derived Projects (open N):
  🐬 porpoise-agent    → P₁ Porpoise Expert
  🐟 coilia-agent      → P₂ Coilia Expert
  🐟 culter-agent      → P₃ Culter Expert
  🔥 conflict-arbiter  → C  Conflict Arbitration — this project
```

> 🔥 Together infinite power, apart top expert engines.

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🗺️ Roadmap

- [ ] Expand to national red lists: Japan, Korea, Vietnam, Mekong basin
- [ ] Machine learning-based conflict pattern detection
- [ ] Real-time IUCN status change alerts
- [ ] Integration with GBIF occurrence data for population trend inference

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 📋 README Changelog

| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v8.0** | 2026-06-18 | README Restoration | Expanded from stub: full philosophy, architecture, features table, arbitration levels, self-assessment, README Changelog, DeepWiki badge |
| **v1.0.0** | 2026-06-17 | Initial | Stub README — basic project description |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 📜 License

MIT © 2026 fangtaocai041

---

🌱 **Everything Flows · Panta Rhei**

> Heraclitus said: No man ever steps in the same river twice.
>
> We say: You cannot arbitrate today's conflicts with last month's data.


> 🔧 Agent constraints: [AGENTS.md](../AGENTS.md) · [core-constitution.md](../.reasonix/core-constitution.md) · [research-first](../skills/research-first.md) · [retro-session](../skills/retro-session.md)

*Last updated: 2026-06-18 | Environment: Reasonix Code · DeepSeek Powered*

---

<div align="center">

### 🏷️ Tech & Topics

`conflict-arbitration` `iucn` `cites` `red-list` `circuit-breaker` `multi-source` `protection-weighted` `conservation` `reasonix` `mcp`

<br>

<sub>🔥 Part of the **SanShengWanWu** ecosystem · C Conflict Arbitration · Coordinated by [eon-core](https://github.com/fangtaocai041/eon-core)</sub>

</div>
