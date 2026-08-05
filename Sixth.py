import time

# ==========================================
# Matrix Chain Multiplication using DP
# ==========================================

def matrix_chain_order(dimensions):

    n = len(dimensions) - 1

    cost = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for chain_length in range(2, n + 1):

        for i in range(1, n - chain_length + 2):

            j = i + chain_length - 1

            cost[i][j] = float("inf")

            for k in range(i, j):

                current_cost = (
                    cost[i][k]
                    + cost[k + 1][j]
                    + dimensions[i - 1] * dimensions[k] * dimensions[j]
                )

                if current_cost < cost[i][j]:

                    cost[i][j] = current_cost
                    split[i][j] = k

    return cost, split


# ==========================================
# Print Optimal Parenthesization
# ==========================================

def optimal_parenthesization(split, i, j):

    if i == j:
        return f"A{i}"

    k = split[i][j]

    left = optimal_parenthesization(split, i, k)
    right = optimal_parenthesization(split, k + 1, j)

    return f"({left} × {right})"


# ==========================================
# Print DP Cost Table
# ==========================================

def print_cost_table(cost, n):

    print("\nDP Cost Table")
    print("-" * 60)

    print(f"{'':<6}", end="")

    for j in range(1, n + 1):
        print(f"A{j:<8}", end="")

    print()

    for i in range(1, n + 1):

        print(f"A{i:<5}", end="")

        for j in range(1, n + 1):

            if j < i:
                print(f"{'---':<9}", end="")
            else:
                print(f"{cost[i][j]:<9}", end="")

        print()


# ==========================================
# Main Program
# ==========================================

dimensions = [10, 30, 5, 60, 10]

number_of_matrices = len(dimensions) - 1

print("=" * 70)
print("MATRIX CHAIN MULTIPLICATION USING DYNAMIC PROGRAMMING")
print("=" * 70)

print("\nMatrix Dimensions")

for i in range(number_of_matrices):
    print(f"A{i+1} : {dimensions[i]} x {dimensions[i+1]}")

start = time.perf_counter()

cost, split = matrix_chain_order(dimensions)

end = time.perf_counter()

minimum_cost = cost[1][number_of_matrices]

parenthesization = optimal_parenthesization(
    split,
    1,
    number_of_matrices
)

print("\nResults")
print("-" * 70)

print(f"Minimum Scalar Multiplications : {minimum_cost}")

print(f"Optimal Parenthesization       : {parenthesization}")

print_cost_table(cost, number_of_matrices)

print("\n")
print("=" * 70)
print("COMPLEXITY")
print("=" * 70)

print("Time Complexity  : O(n^3)")
print("Space Complexity : O(n^2)")
print(f"Execution Time   : {(end-start)*1000:.6f} ms")

print("\nExperiment Completed Successfully.")