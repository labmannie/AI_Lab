<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=6366f1,8b5cf6&height=160&section=header&text=AI%20Lab%20Programs&fontSize=42&fontColor=ffffff&fontAlignY=42&animation=fadeIn" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1200&color=8B5CF6&center=true&vCenter=true&width=600&lines=Intelligent+Agents+in+Pure+Python;BFS+%7C+DFS+%7C+UCS+%7C+A*+%7C+IDDFS;Search+Algorithms+%2B+Agent+Design;Zero+Dependencies.+Real+AI.)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.6+-6366f1?style=flat-square&logo=python&logoColor=white)
![Programs](https://img.shields.io/badge/Programs-13-8b5cf6?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-f59e0b?style=flat-square)

</div>

---

## About

A complete AI lab record covering **intelligent agent design** and **search algorithms** — built as part of the AI/ML curriculum at NIE. Organized into two sections: agent-based programs and classical search implementations. Pure Python, no external dependencies.

---

## Repository Structure

```
├── Vacuum_Agent/
│   ├── prog1.py          # Simple Reflex Vacuum Agent
│   ├── prog2.py          # Iterative Reflex Simulation
│   ├── prog3.py          # Goal-Seeking Movement
│   ├── prog4.py          # Rational Agent (PEAS)
│   └── prog5.py          # Grid Vacuum Cleaner
│
├── BFS.py                # Breadth-First Search
├── DFS.py                # Depth-First Search
├── DLS.py                # Depth-Limited Search
├── IDDFS.py              # Iterative Deepening DFS
├── UCS.py                # Uniform Cost Search
├── 8puzzle_A*.py         # 8-Puzzle via A* Search
└── wumpus.py             # Wumpus World Agent
```

---

## Vacuum Agent Programs

Programs inside `Vacuum_Agent/` — progressive agent design from simple to rational.

| # | File | What it does | Type |
|---|------|-------------|------|
| 1 | `prog1.py` | Agent reacts to dirty/clean room states | Simple Reflex |
| 2 | `prog2.py` | Reflex agent runs across multiple iterations | Reflex + Loop |
| 3 | `prog3.py` | Agent navigates toward a defined goal position | Goal-Based |
| 4 | `prog4.py` | Full agent class built around PEAS architecture | Rational |
| 5 | `prog5.py` | Vacuum cleaner on a 2D grid world | Utility-Based |

```bash
cd Vacuum_Agent
python prog1.py
python prog2.py
python prog3.py
python prog4.py
python prog5.py
```

---

## Search Algorithm Programs

| File | Algorithm | Strategy | Complete | Optimal |
|------|-----------|----------|----------|---------|
| `BFS.py` | Breadth-First Search | Level-by-level exploration | Yes | Yes (unweighted) |
| `DFS.py` | Depth-First Search | Explore deep before backtracking | Yes | No |
| `DLS.py` | Depth-Limited Search | DFS with a hard depth cutoff | No | No |
| `IDDFS.py` | Iterative Deepening DFS | Repeated DLS with increasing limit | Yes | Yes (unweighted) |
| `UCS.py` | Uniform Cost Search | Expand lowest-cost path first | Yes | Yes |
| `8puzzle_A*.py` | A\* Search | UCS + heuristic (Manhattan Distance) | Yes | Yes |
| `wumpus.py` | Wumpus World | Knowledge-based agent in a grid cave | — | — |

```bash
python BFS.py
python DFS.py
python DLS.py
python IDDFS.py
python UCS.py
python "8puzzle_A*.py"
python wumpus.py
```

---

## Algorithm Quick Reference

```
BFS      →  guaranteed shortest path, explores level by level, high memory use
DFS      →  low memory, no optimality guarantee, can get stuck in deep branches
DLS      →  DFS with depth cap, avoids infinite loops, may miss solutions
IDDFS    →  combines DFS memory efficiency with BFS completeness
UCS      →  optimal for weighted graphs, expands by cumulative cost
A*       →  UCS + heuristic guidance, optimal and faster than UCS alone
Wumpus   →  logical inference, knowledge base, percept-driven decisions
```

---

## Concepts Covered

```
Reflex Agents     →  Vacuum_Agent/prog1, prog2    (no memory, stimulus → response)
Goal-Based        →  Vacuum_Agent/prog3, prog4    (plan toward a target)
Rational Agent    →  Vacuum_Agent/prog4           (PEAS model)
Grid Environment  →  Vacuum_Agent/prog5           (2D world, full state tracking)
Uninformed Search →  BFS, DFS, DLS, IDDFS         (no domain knowledge used)
Informed Search   →  UCS, A*                      (cost/heuristic guided)
Knowledge Agent   →  wumpus.py                    (logic-based reasoning)
```

---

## License

MIT — free to use, modify, and distribute.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=6366f1,8b5cf6&height=100&section=footer&animation=fadeIn" width="100%"/>

**Lab Man NIE · 2026**

</div>
