import argparse
import random
import time

# points_all[0] = label 1, points_all[1] = label 2, ...
points_all = [
    (34.7, 45.1),   # label 1
    (34.7, 26.4),   # label 2
    (33.4, 60.5),   # label 3
    (51.7, 56.0),   # label 4
    (45.7, 25.1),   # label 5
    (62.0, 58.4),   # label 6
    (57.7, 42.1),   # label 7
    (46.0, 45.1),   # label 8
    (54.2, 29.1),   # label 9
    (57.5, 56.0),   # label 10
    (67.9, 19.6),   # label 11
    (21.5, 45.8),   # label 12
    (28.4, 31.7),   # label 13
    (15.1, 49.6),   # label 14
    (22.9, 32.7),   # label 15
    (9.1, 52.8),    # label 16
    (15.3, 37.8),   # label 17
    (2.7, 56.8),    # label 18
    (9.1, 40.3),    # label 19
    (2.7, 33.1),    # label 20
]

# L1 distance
def L1(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# Open-path nearest-neighbor search with segment-reversal improvement.
def nearest_neighbor_two_opt(indices, iterations=300, seed=None):
    indices = list(indices)
    if iterations < 1:
        raise ValueError("iterations must be positive")
    if len(set(indices)) != len(indices):
        raise ValueError("indices must be unique")
    if any(not isinstance(i, int) or i < 0 or i >= len(points_all) for i in indices):
        raise ValueError("point index out of range")
    if not indices:
        return 0, []
    rng = random.Random(seed)
    best_path = None
    best_len = float('inf')

    # distance matrix
    D = [[0]*len(points_all) for _ in range(len(points_all))]
    for i in indices:
        for j in indices:
            D[i][j] = L1(points_all[i], points_all[j])

    def path_length(path):
        return sum(D[path[i]][path[i+1]] for i in range(len(path)-1))

    def two_opt(path):
        improved = True
        while improved:
            improved = False
            for i in range(len(path)-1):
                for j in range(i+2, len(path)+1):
                    new_path = path[:i] + path[i:j][::-1] + path[j:]
                    if path_length(new_path) < path_length(path):
                        path = new_path
                        improved = True
        return path

    for _ in range(iterations):
        # random start node
        start = rng.choice(indices)
        unvisited = indices[:]
        unvisited.remove(start)
        path = [start]

        # Nearest neighbor
        while unvisited:
            last = path[-1]
            next_node = min(unvisited, key=lambda x: D[last][x])
            path.append(next_node)
            unvisited.remove(next_node)

        # 2-opt improvement
        path = two_opt(path)
        L = path_length(path)
        if L < best_len:
            best_len = L
            best_path = path

    return best_len, best_path

# Compatibility with the original coursework entry point.
def lkh_heuristic(indices, iterations=300, seed=None):
    return nearest_neighbor_two_opt(indices, iterations, seed)

def run_case(n, iterations=300, seed=None):
    indices = list(range(n))  # 0-based indices
    print("\n=====================================")
    print(f"PRVIH {n} RUPA (nearest neighbor + 2-opt)")
    print("=====================================")
    start_time = time.time()
    best_len, best_path = nearest_neighbor_two_opt(indices, iterations, seed)
    elapsed = time.time() - start_time
    print(f"Vrijeme izvodjenja: {elapsed:.3f} s")
    print(f"Najkraca duzina aproksimacija (L1): {best_len:.4f} mm")
    print("Redoslijed labela:", [i+1 for i in best_path])  # label = index+1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize an open route using Manhattan distance.")
    parser.add_argument('--points', type=int, nargs='+', default=[8, 12])
    parser.add_argument('--iterations', type=int, default=300)
    parser.add_argument('--seed', type=int)
    args = parser.parse_args()
    if args.iterations < 1 or any(n < 1 or n > len(points_all) for n in args.points):
        parser.error('iterations must be positive; points must be between 1 and 20')
    for n in args.points:
        run_case(n, args.iterations, args.seed)
