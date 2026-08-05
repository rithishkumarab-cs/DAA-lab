import random
import time

# ==========================================
# Global Comparison Counter
# ==========================================

comparison_count = 0


# ==========================================
# Divide and Conquer Algorithm
# ==========================================

def min_max_dc(arr, low, high):
    global comparison_count

    # Base Case: One Element
    if low == high:
        return arr[low], arr[low]

    # Base Case: Two Elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


# ==========================================
# Naive Algorithm
# ==========================================

def min_max_naive(arr):

    minimum = arr[0]
    maximum = arr[0]

    comparisons = 0

    for value in arr[1:]:

        comparisons += 1
        if value < minimum:
            minimum = value

        comparisons += 1
        if value > maximum:
            maximum = value

    return minimum, maximum, comparisons


# ==========================================
# Demonstration
# ==========================================

sample_array = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

print("=" * 70)
print("DIVIDE AND CONQUER - FIND MINIMUM AND MAXIMUM")
print("=" * 70)

print("\nInput Array")
print(sample_array)

# Divide & Conquer
comparison_count = 0

start = time.perf_counter()

minimum, maximum = min_max_dc(
    sample_array,
    0,
    len(sample_array) - 1
)

dc_time = (time.perf_counter() - start) * 1000
dc_comparisons = comparison_count

# Naive
start = time.perf_counter()

_, _, naive_comparisons = min_max_naive(sample_array)

naive_time = (time.perf_counter() - start) * 1000

print("\nResults")
print("-" * 70)

print(f"Minimum Element                : {minimum}")
print(f"Maximum Element                : {maximum}")
print(f"Divide & Conquer Comparisons   : {dc_comparisons}")
print(f"Naive Comparisons              : {naive_comparisons}")

print("\nExecution Time")
print("-" * 70)

print(f"Divide & Conquer : {dc_time:.6f} ms")
print(f"Naive Method     : {naive_time:.6f} ms")


# ==========================================
# Performance Comparison
# ==========================================

print("\n")
print("=" * 70)
print("PERFORMANCE ANALYSIS")
print("=" * 70)

sizes = [10, 100, 1000, 10000]

print(
    f"{'Size':<10}"
    f"{'D&C':>12}"
    f"{'Naive':>12}"
    f"{'Formula':>15}"
)

print("-" * 50)

for size in sizes:

    arr = [random.randint(1, 100000) for _ in range(size)]

    comparison_count = 0

    min_max_dc(arr, 0, len(arr) - 1)

    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = (3 * size // 2) - 2

    print(
        f"{size:<10}"
        f"{dc:>12}"
        f"{naive:>12}"
        f"{formula:>15}"
    )


# ==========================================
# Complexity
# ==========================================

print("\n")
print("=" * 70)
print("COMPLEXITY")
print("=" * 70)

print("Divide & Conquer")
print("Time Complexity  : O(n)")
print("Space Complexity : O(log n)")

print()

print("Naive Method")
print("Time Complexity  : O(n)")
print("Space Complexity : O(1)")

print("\nExperiment Completed Successfully.")