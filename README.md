# Route Optimization Heuristic

A Python route-search experiment over 20 predefined points using Manhattan distance, nearest-neighbor initialization, repeated randomized starts, and 2-opt improvement.

## Run

Requires Python 3; the code imports only standard-library modules.

```sh
python main.py
```

The implementation describes its approach as LKH-like, but it is a nearest-neighbor/2-opt heuristic, not a full implementation of the Lin-Kernighan-Helsgaun algorithm. Results are stochastic because no random seed is set. The path-length helper sums consecutive edges without automatically adding a closing edge.

Review the script's entry point before running longer experiments. Syntax validation alone does not establish solution optimality.

## Context

Educational project by Marko Mijanovic, University of Belgrade, School of Electrical Engineering. Course scaffolding and supplied assets remain part of the project; this preparation does not grant a new license to third-party material.

## Preparation validation

- fixed-seed route visits each point once and matches reported length: passed.
- AST syntax check for 1 Python files: passed.
