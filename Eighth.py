import time
from itertools import permutations

INF = float("inf")

# ==========================================
# Brute Force TSP (Lab Version)
# ==========================================

def tsp_solver(cost_matrix):

    n = len(cost_matrix)

    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    for perm in permutations(cities):

        path = [0] + list(perm) + [0]

        total_cost = 0

        for i in range(n):
            total_cost += cost_matrix[path[i]][path[i + 1]]

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


# ==========================================
# Main Program
# ==========================================

cities = ["A", "B", "C", "D", "E"]

cost_matrix = [

    [INF, 10, 8, 9, 7],

    [10, INF, 10, 5, 6],

    [8, 10, INF, 8, 9],

    [9, 5, 8, INF, 6],

    [7, 6, 9, 6, INF]

]

print("=" * 70)
print("TRAVELLING SALESMAN PROBLEM")
print("=" * 70)

print("\nCost Matrix\n")

print("     ", end="")

for city in cities:
    print(f"{city:>6}", end="")

print()

for i in range(len(cost_matrix)):

    print(f"{cities[i]:>3}", end="")

    for value in cost_matrix[i]:

        if value == INF:
            print(f"{'INF':>6}", end="")
        else:
            print(f"{value:>6}", end="")

    print()

start = time.perf_counter()

path, minimum_cost = tsp_solver(cost_matrix)

end = time.perf_counter()

print("\nOptimal Tour")
print("-" * 70)

tour = " -> ".join(cities[i] for i in path)

print(tour)

print(f"\nMinimum Cost : {minimum_cost}")

print("\nPath Details")
print("-" * 70)

for i in range(len(path) - 1):

    u = path[i]
    v = path[i + 1]

    print(f"{cities[u]} -> {cities[v]} : {cost_matrix[u][v]}")

print("\n")
print("=" * 70)
print("COMPLEXITY")
print("=" * 70)

print("Time Complexity  : O((n-1)!)")
print("Space Complexity : O(n)")
print(f"Execution Time   : {(end-start)*1000:.6f} ms")

print("\nExperiment Completed Successfully.")