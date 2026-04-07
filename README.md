<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=6366f1,8b5cf6&height=160&section=header&text=AI%20Lab%20Programs&fontSize=42&fontColor=ffffff&fontAlignY=42&animation=fadeIn" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1200&color=8B5CF6&center=true&vCenter=true&width=600&lines=Intelligent+Agents+in+Pure+Python;Reflex+%E2%86%92+Goal-Based+%E2%86%92+Search+Algorithms;6+Programs.+Zero+Dependencies.+Real+AI.)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.6+-6366f1?style=flat-square&logo=python&logoColor=white)
![Programs](https://img.shields.io/badge/Programs-6-8b5cf6?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-f59e0b?style=flat-square)

</div>

---

## About

A lab record of **6 Python programs** covering intelligent agent design and search algorithms — built as part of the AI/ML curriculum at NIE. No external libraries, no fluff — just clean Python that actually teaches you how agents think.

---

## Programs

| # | File | What it does | Agent Type |
|---|------|-------------|------------|
| 1 | `prog1.py` | Vacuum agent reacts to dirty/clean states | Simple Reflex |
| 2 | `prog2.py` | Runs the reflex agent over multiple iterations | Reflex + Loop |
| 3 | `prog3.py` | Agent navigates toward a defined goal position | Goal-Based |
| 4 | `prog4.py` | Full agent class with PEAS architecture | Rational |
| 5 | `prog5.py` | Vacuum cleaner operating on a 2D grid world | Utility-Based |
| 6 | `program6_ucs.py` | Least-cost path search using a Priority Queue | Search (UCS) |

---

## Run Anything

```bash
python prog1.py
python prog2.py
python prog3.py
python prog4.py
python prog5.py
python program6_ucs.py
```

No `pip install` needed. Just Python.

---

## Program 6 — Uniform Cost Search

Finds the minimum-cost path from **A → G** using a hand-rolled `PriorityQueue` class.

```
Graph:

    A --1--> B --1--> D
    |        |         \
    4        3          2
    |        |           \
    v        v            v
    C --5--> F --2--> G <-- E
                      ^
                      1
```

```
Output: (3, ['A', 'B', 'E', 'G'])
```

The UCS algorithm explores paths in order of cumulative cost, guaranteeing the optimal solution.

---

## Concepts Covered

```
Reflex Agents     →   prog1, prog2    (stimulus → response, no memory)
Goal-Based        →   prog3, prog4    (planning toward a target state)
Rational Agent    →   prog4           (PEAS: Performance, Environment, Actuators, Sensors)
Grid Environment  →   prog5           (2D world with full state tracking)
UCS / Search      →   prog6           (priority queue, cumulative cost, optimal path)
```

---

## Learning Path

```
prog1 ──► prog2 ──► prog3 ──► prog4 ──► prog5 ──► prog6
  │          │         │         │         │         │
Reflex    Iterate    Goals    Rational   Grid     Search
```

Start at `prog1` if you're new to agents. Jump to `program6_ucs.py` if you're here for the assignment.

---

## License

MIT — free to use, modify, and distribute.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=6366f1,8b5cf6&height=100&section=footer&animation=fadeIn" width="100%"/>

**Lab Man NIE · 2026**

</div>
