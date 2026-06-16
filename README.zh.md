# Conflict Arbiter 🔥

**C 万物衍生** — 多源保护级别冲突检测 · 中国优先加权 · 时空可比性。

> 🌊 万物皆变 · Panta Rhei
>
> IUCN 说濒危，国标说无危，CITES 说附录 II。
> 一个物种，三张红牌——谁是对的？

[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://python.org)

[English](README.md) · [中文](README.zh.md) · [更新日志](CHANGELOG.md)

---

## 📋 项目简介

**Conflict Arbiter** 是三角核心生态系统的 **C 衍生项目**，负责检测和仲裁多来源（IUCN、中国红皮书、CITES、省级保护名录等）的物种保护等级冲突，使用加权仲裁 + 熔断机制处理不可调和的分歧。

### 🚀 核心能力

| 🚀 能力 | 📝 说明 |
|:---------|:--------|
| 🔄 多源标准化 | 将 IUCN / 中国红皮 / CITES / 省级映射到统一 [0-100] 数值轴 |
| ⚡ 3 级冲突检测 | 0=一致 / 1=轻微 / 2=显著 / 3=**熔断** |
| ⚖️ 加权仲裁 | region="china" 时中国分类权威优先 |
| ⏱ 时空一致性 | 不同时段/不同地区的数据不构成冲突 |
| 🛡️ 熔断机制 | 严重冲突自动升级为人工审查 |

---

## ⚡ 快速开始

### 📦 安装

```bash
git clone https://github.com/fangtaocai041/conflict-arbiter.git
cd conflict-arbiter
pip install -e .
```

### 🔧 基本使用

```python
from conflict_arbiter.src.arbiter import ConflictArbiter

arbiter = ConflictArbiter()

# 检测多源保护等级冲突
result = arbiter.detect_conflicts(
    species_name="Coilia nasus",
    sources=[
        {"source": "iucn", "protection_level": "EN"},
        {"source": "chinese_red_list", "protection_level": "国家二级"},
    ],
    region="china",
)
print(f"冲突等级: {result['conflict_level']}")
print(f"裁决: {result['verdict']}")
```

---

## 🚀 核心功能

### 🔄 多源冲突检测

```python
result = arbiter.detect_conflicts(
    species_name="Neophocaena asiaeorientalis",
    sources=[
        {"source": "iucn", "protection_level": "CR"},
        {"source": "chinese_red_list", "protection_level": "极危"},
    ],
    region="china",
)
# 冲突等级 0 → 完全一致
```

### ⚖️ 通用声明仲裁（含时空检查）

```python
result = arbiter.arbitrate(
    species_name="Culter alburnus",
    claims=[
        {"claim": "种群下降", "source": "2020 调查",
         "weight": 80, "value": 65,
         "time_period": {"start": 2018, "end": 2020},
         "region": "长江中游"},
        {"claim": "资源稳定", "source": "2015 报告",
         "weight": 60, "value": 40,
         "time_period": {"start": 2010, "end": 2015},
         "region": "长江下游"},
    ],
)
# 不同时段 → 不构成冲突
```

---

## 📁 项目架构

```
conflict-arbiter/
├── src/
│   ├── arbiter.py                ← ConflictArbiter 核心引擎
│   │   ├── detect_conflicts()    ← 多源保护等级冲突检测
│   │   ├── arbitrate()           ← 通用声明仲裁
│   │   └── _normalize_source()   ← 保护等级→数值映射
│   └── adapter.py                ← 跨项目接口
├── config/
│   ├── agent.yaml                ← 阈值/权重/熔断配置
│   └── arbitration_rules.yaml    ← 仲裁规则
├── pyproject.toml
└── Dockerfile
```

---

## ⚙️ 配置

```yaml
# config/agent.yaml
trust_thresholds:
  high: 75
  medium: 45
  low: 20
source_weights:
  chinese_red_list: 100
  provincial_protection: 90
  iucn: 40
  cites: 40
```

---

## 🔗 关联项目

| 🏗️ 项目 | 🎯 角色 |
|:---------|:--------|
| fish-ecology-assistant | 知识供给 — 保护数据来源 |
| cognitive-search-engine | 搜索验证 — 文献证据 |
| eon-core | 协调内核 — 仲裁输出路由 |
| porpoise-agent / coilia-agent / culter-agent | 保护建议来源 |

## 📜 许可证

MIT

---

> 🌊 万物皆变 · Panta Rhei
>
> 🏛️ 赫拉克利特说：人不能两次踏进同一条河流。
>
> 💻 我们说：但一个物种可能被三个保护名录给出三种结论。我们的工作是——找出真相。
>
> **📅 最后更新: 2026-06-21 · 🖥️ Reasonix Code · ⚡ DeepSeek 驱动**

[⬆ 回到顶部](#)
