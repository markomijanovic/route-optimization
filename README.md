# Route Optimization Heuristic

A Python route-search experiment over 20 predefined points using Manhattan distance, nearest-neighbor initialization, repeated randomized starts, and 2-opt improvement.

## Run

Requires Python 3; the code imports only standard-library modules.

```sh
python main.py
python main.py --points 8 12 20 --iterations 300 --seed 42
python -m unittest discover -s tests -v
```

The solver constructs an **open route**: it visits each selected point once without returning to the start. It minimizes Manhattan (L1) distance using randomized nearest-neighbor starts and segment reversals. This is a heuristic with no guarantee of global optimality.

Use `--seed` to reproduce an experiment, `--iterations` to set the number of restarts, and `--points` to select one or more prefix sizes from 1 to 20. The public function is `nearest_neighbor_two_opt(indices, iterations=300, seed=None)`; the original `lkh_heuristic` name remains a compatibility alias, not a claim to implement LKH.

Review the script's entry point before running longer experiments. Syntax validation alone does not establish solution optimality.

## Context

Educational project by [Marko Mijanovic](https://github.com/markomijanovic), University of Belgrade, School of Electrical Engineering. Supplied course scaffolding and assets retain their original licensing terms.

## Verification

- Three unit tests passed, covering seeded reproducibility, route membership and cost, empty input, and invalid arguments.
- A seeded command-line run completed for 8, 12, and 20 points.
- No claim of global optimality is made.
