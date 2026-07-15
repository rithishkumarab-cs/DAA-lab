import heapq
import time

# ============================================
# UNION-FIND (Disjoint Set) FOR KRUSKAL
# ============================================

class UnionFind:
    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


# ============================================
# KRUSKAL ALGORITHM
# ============================================

def kruskal(vertices, edges):

    start = time.perf_counter()

    edges = sorted(edges)

    uf = UnionFind(vertices)

    mst = []
    total_cost = 0

    for weight, u, v in edges:

        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == vertices - 1:
                break

    end = time.perf_counter()

    return mst, total_cost, (end - start) * 1000


# ============================================
# PRIM ALGORITHM
# ============================================

def prim(vertices, adjacency_list, start_vertex=0):

    start = time.perf_counter()

    visited = [False] * vertices

    priority_queue = [(0, start_vertex, -1)]

    mst = []

    total_cost = 0

    while priority_queue:

        weight, current, parent = heapq.heappop(priority_queue)

        if visited[current]:
            continue

        visited[current] = True

        if parent != -1:
            mst.append((parent, current, weight))
            total_cost += weight

        for neighbour, edge_weight in adjacency_list[current]:
            if not visited[neighbour]:
                heapq.heappush(priority_queue,
                               (edge_weight, neighbour, current))

    end = time.perf_counter()

    return mst, total_cost, (end - start) * 1000


# ============================================
# PRINT FUNCTION
# ============================================

def print_mst(title, mst, cost, runtime):

    print("=" * 55)
    print(title)
    print("=" * 55)

    for u, v, w in mst:
        print(f"Edge ({u} - {v})   Weight = {w}")

    print("-" * 55)
    print(f"Total MST Cost : {cost}")
    print(f"Execution Time : {runtime:.6f} ms")
    print()


# ============================================
# MAIN PROGRAM
# ============================================

vertices = 7

edges = [

    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)

]

adjacency_list = [[] for _ in range(vertices)]

for weight, u, v in edges:
    adjacency_list[u].append((v, weight))
    adjacency_list[v].append((u, weight))


kruskal_mst, kruskal_cost, kruskal_time = kruskal(vertices, edges)

prim_mst, prim_cost, prim_time = prim(vertices, adjacency_list)


print("\n")
print("MINIMUM SPANNING TREE USING GREEDY ALGORITHMS\n")

print_mst("KRUSKAL'S ALGORITHM", kruskal_mst,
          kruskal_cost, kruskal_time)

print_mst("PRIM'S ALGORITHM", prim_mst,
          prim_cost, prim_time)


print("=" * 55)
print("COMPARISON")
print("=" * 55)

print(f"Kruskal Cost : {kruskal_cost}")
print(f"Prim Cost    : {prim_cost}")

if kruskal_cost == prim_cost:
    print("\nBoth algorithms produced the SAME Minimum Spanning Tree Cost.")
else:
    print("\nAlgorithms produced different MST costs.")

print("\nExecution Time")
print(f"Kruskal : {kruskal_time:.6f} ms")
print(f"Prim    : {prim_time:.6f} ms")

print("\nTime Complexity")
print("Kruskal : O(E log E)")
print("Prim    : O(E log V)")

print("\nExperiment Completed Successfully.")