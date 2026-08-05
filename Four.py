import heapq
import time

# ==========================================
# Dijkstra's Shortest Path Algorithm
# ==========================================

def dijkstra(graph, source):
    vertices = len(graph)

    distance = [float('inf')] * vertices
    previous = [None] * vertices

    distance[source] = 0

    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:

        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbour, weight in graph[current_vertex]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbour]:

                distance[neighbour] = new_distance
                previous[neighbour] = current_vertex

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    return distance, previous


# ==========================================
# Reconstruct Shortest Path
# ==========================================

def reconstruct_path(previous, source, destination):

    path = []

    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# ==========================================
# Print Result Table
# ==========================================

def display_result(distance, previous, source):

    print("\n")
    print("=" * 80)
    print(f"SHORTEST PATHS FROM SOURCE VERTEX {source}")
    print("=" * 80)

    print(
        f"{'Vertex':<10}"
        f"{'Distance':<12}"
        f"{'Path'}"
    )

    print("-" * 80)

    for vertex in range(len(distance)):

        path = reconstruct_path(previous, source, vertex)

        if path:
            path_string = " -> ".join(map(str, path))
        else:
            path_string = "No Path"

        dist = (
            distance[vertex]
            if distance[vertex] != float('inf')
            else "INF"
        )

        print(
            f"{vertex:<10}"
            f"{str(dist):<12}"
            f"{path_string}"
        )


# ==========================================
# Graph Definition
# ==========================================

graph = {

    0: [(1, 4), (2, 1)],

    1: [(3, 1)],

    2: [(1, 2), (3, 5)],

    3: [(4, 3)],

    4: [(5, 2)],

    5: []

}

source_vertex = 0


# ==========================================
# Main Execution
# ==========================================

print("\nDIJKSTRA'S SHORTEST PATH ALGORITHM")

start = time.perf_counter()

distance, previous = dijkstra(graph, source_vertex)

end = time.perf_counter()

display_result(distance, previous, source_vertex)

print("\n")
print("=" * 80)
print("PERFORMANCE")
print("=" * 80)

print(f"Source Vertex        : {source_vertex}")
print(f"Total Vertices       : {len(graph)}")
print(f"Execution Time       : {(end-start)*1000:.6f} ms")
print(f"Time Complexity      : O((V + E) log V)")
print(f"Space Complexity     : O(V)")

print("\nExperiment Completed Successfully.")