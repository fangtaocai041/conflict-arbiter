<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║   🔥  CONFLICT ARBITER  ·  C 冲突仲裁层  ·  v1.0.1           ║
║  ─────────────────────────────────────────────────────────  ║
║  多源聚合 · 保护级加权 · 熔断器 · 四级冲突升级                  ║
║      IUCN 红名单 · CITES · 中国红皮书 · 冲突仲裁               ║
╚══════════════════════════════════════════════════════════════╝
```

<p align="center">
  🇬🇧 <a href="README.md">English</a>
</p>

# 🔥 Conflict Arbiter · 冲突仲裁 (C)

> **角色**: C — 三生万物 S-T-V-P₁-P₂-P₃-C 六体架构中的衍生冲突仲裁层。
> **问题**: 当 S（知识供给）与 V（搜索验证）意见不一，或多个衍生项目产出矛盾发现时，谁来裁定？
> **方案**: C — 多源保护级加权、熔断器保护的冲突仲裁引擎。

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.1-8b5cf6)]()
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB)]()
[![Conflict](https://img.shields.io/badge/冲突-4级-red)]()
[![China Weighted](https://img.shields.io/badge/中国加权-orange)]()
[![Circuit Breaker](https://img.shields.io/badge/熔断器-yellow)]()
[![Triangle](https://img.shields.io/badge/三角赋能-EC4899)]()
[![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/conflict-arbiter)

<p align="center">
  <a href="https://github.com/fangtaocai041/conflict-arbiter/stargazers"><img src="https://img.shields.io/github/stars/fangtaocai041/conflict-arbiter?style=social" alt="Stars"></a>
  <a href="https://github.com/fangtaocai041/conflict-arbiter/network/members"><img src="https://img.shields.io/github/forks/fangtaocai041/conflict-arbiter?style=social" alt="Forks"></a>
</p>

</div>

---

## 📑 目录

- [🔺 S-T-V-P₁-P₂-P₃-C 架构角色: C (冲突仲裁)](#-s-t-v-p-p-p-c-架构角色-c-冲突仲裁)
- [📊 自我评价](#-自我评价)
- [📋 版本历史](#-版本历史)
- [🧩 这个项目是什么](#-这个项目是什么)
- [🚀 快速开始](#-快速开始)
- [⚖ 仲裁等级](#-仲裁等级)
- [✨ 功能特性](#-功能特性)
- [🔗 生态体系](#-生态体系)
- [📋 README 变更记录](#-readme-变更记录)
- [📜 许可证](#-许可证)

---

## 🔺 S-T-V-P₁-P₂-P₃-C 架构角色: **C (冲突仲裁)**

> 三生万物六体架构: `fish(S) → cognitive(V) → eon-core(Coord)`，衍生: `porpoise(P₁)` + `coilia(P₂)` + `culter(P₃)` + `conflict-arbiter(C)`。
> **C** 是冲突解决层——当多个来源在保护状态、分类学或生态发现上存在分歧时，C 使用保护级加权、来源可信度评分和熔断器保护进行仲裁。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

## 📊 自我评价

| 维度 | 评分 | 说明 |
|------|:----:|------|
| ⚖ 仲裁逻辑 | ⭐⭐⭐⭐⭐ | 4 级冲突升级 + 加权裁定 |
| 🌐 多源集成 | ⭐⭐⭐⭐⭐ | IUCN API v4 + CITES Checklist API + 中国红皮书 + 国家重点保护 |
| 🛡️ 熔断器 | ⭐⭐⭐⭐⭐ | 防止不可靠 API 源导致级联故障 |
| 📡 三角集成 | ⭐⭐⭐⭐⭐ | 接收 S 层声明、V 层验证 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## 📋 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| **v1.0.1** | 2026-06-18 | README 复原 — 从历史会话恢复完整文档 |
| **v1.0.0** | 2026-06-17 | 初始发布 — IUCN API, CITES API, CLI 工具, 熔断器 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## 🧩 这个项目是什么

**Conflict Arbiter** 是三生万物生态中的冲突解决层。当鱼类生态助手说"此物种为濒危"，但认知搜索引擎找到更新的 IUCN 评估为"易危"——仲裁器介入。

### 核心功能

| 功能 | 说明 |
|------|------|
| **多源聚合** | IUCN 红名单 API v4 + CITES 物种+ Checklist API + 中国红皮书 + 国家重点保护名录 |
| **4 级冲突分类** | INFORMATION → WARNING → CRITICAL → BLOCKING 严重度阶梯 |
| **中国加权评分** | 中国来源在国内保护决策中获得加权 |
| **熔断器** | 防止不可靠 API 源污染仲裁结果 |
| **保护级仲裁** | 当来源保护状态不一致时，加权投票解决 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## 🚀 快速开始

```bash
git clone https://github.com/fangtaocai041/conflict-arbiter.git
cd conflict-arbiter
pip install -e .
python -m conflict_arbiter arbitrate "刀鲚"
```

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## ⚖ 仲裁等级

| 等级 | 触发条件 | 响应 |
|:----:|------|------|
| **INFORMATION** | 微小差异（如年份差异） | 记录 + 通知 |
| **WARNING** | 跨来源状态不一致 | 加权投票 + 报告 |
| **CRITICAL** | 保护级冲突（如 EN vs VU） | 深入调查 + 建议 |
| **BLOCKING** | 根本矛盾（如物种鉴定冲突） | 暂停管线 + 人工审查 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## ✨ 功能特性

<details open><summary><b>📋 特性列表</b></summary>

| 功能 | 状态 | 说明 |
|------|:----:|------|
| ⚖ 4 级冲突 | ✅ | INFORMATION→WARNING→CRITICAL→BLOCKING 升级 |
| 🌐 IUCN API 客户端 | ✅ | IUCN 红名单 API v4 实时评估数据 |
| 📋 CITES API 客户端 | ✅ | CITES 物种+ Checklist API 附录列名查询 |
| 🇨🇳 中国加权 | ✅ | 中国红皮书 + 国家重点保护加权 |
| 🛡️ 熔断器 | ✅ | 防止不可靠源的级联故障 |
| 🛠️ CLI 工具 | ✅ | `scripts/arbitrate.py` — 命令行仲裁 |

</details>

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## 🔗 生态体系

```
三角核心 (sealed 3):
  📦 fish-ecology-assistant    → 知识供给 (V0)
  🔍 cognitive-search-engine   → 搜索验证 (V1)
  ⚙ eon-core                  → 协调内核 (Coord)

万物衍生 (open N):
  🐬 porpoise-agent    → P₁ 江豚专研
  🐟 coilia-agent      → P₂ 刀鲚专研
  🐟 culter-agent      → P₃ 鲌类专研
  🔥 conflict-arbiter  → C  冲突仲裁 — 本项目
```

> 🔥 和则无穷力量，分则顶尖专家引擎。

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## 📋 README 变更记录

| 版本 | 日期 | 主题 | 变更内容 |
|:-----|:-----|:-----|:---------|
| **v8.0** | 2026-06-18 | README 复原 | 从 stub 扩展: 完整哲学、架构、功能表、仲裁等级、自我评价、变更记录、DeepWiki 徽标 |
| **v1.0.0** | 2026-06-17 | 初始 | Stub README — 基本项目描述 |

<p align="right"><a href="#-目录">↑ 返回目录</a></p>

---

## 📜 许可证

MIT © 2026 fangtaocai041

---

🌱 **万物皆变 · Panta Rhei**

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 我们说：知识会老去，但人类对世界的追问永不落幕。昨日之真理为今日之基石，今日之未知为明日之征途。我们的目光，从不囿于已知的疆界；我们的脚步，终将踏上那片星光璀璨的浩瀚征途。

这个项目不是一套固定的工具集——它是一个**活的系统**。每个组件都内置了过期机制、版本追踪和涌现感知。随着你的研究深入、R包更新、新方法涌现，它会和你一起进化。


> 🔧 Agent 约束: [AGENTS.md](../AGENTS.md) · [core-constitution.md](../.reasonix/core-constitution.md) · [research-first](../skills/research-first.md) · [retro-session](../skills/retro-session.md)

*最后更新: 2026-06-18 | 适用环境: Reasonix Code · DeepSeek 驱动*

---

<div align="center">

### 🏷️ 技术标签

`冲突仲裁` `IUCN` `CITES` `红名单` `熔断器` `多源聚合` `保护级加权` `保护生物学` `Reasonix` `MCP`

<br>

<sub>🔥 属于 **三生万物** 生态体系 · C 冲突仲裁层 · 由 [eon-core](https://github.com/fangtaocai041/eon-core) 统一协调</sub>

</div>
