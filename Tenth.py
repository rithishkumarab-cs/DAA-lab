import random
import time
import sys

sys.setrecursionlimit(20000)

# ==========================================
# Global Comparison Counter
# ==========================================

comparisons = 0


# ==========================================
# Partition Function
# ==========================================

def partition(arr, low, high):

    global comparisons

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        comparisons += 1

        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# ==========================================
# Deterministic Quick Sort
# ==========================================

def deterministic_quicksort(arr, low, high):

    if low < high:

        pivot_index = partition(arr, low, high)

        deterministic_quicksort(arr, low, pivot_index - 1)

        deterministic_quicksort(arr, pivot_index + 1, high)


# ==========================================
# Randomized Quick Sort
# ==========================================

def randomized_quicksort(arr, low, high):

    if low < high:

        random_index = random.randint(low, high)

        arr[random_index], arr[high] = arr[high], arr[random_index]

        pivot_index = partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)

        randomized_quicksort(arr, pivot_index + 1, high)


# ==========================================
# Run Test
# ==========================================

def run_algorithm(sort_function, array):

    global comparisons

    arr = array[:]

    comparisons = 0

    start = time.perf_counter()

    sort_function(arr, 0, len(arr) - 1)

    end = time.perf_counter()

    return comparisons, (end - start) * 1000


# ==========================================
# Test Cases
# ==========================================

N = 5000

random.seed(42)

test_cases = {

    "Random":
        [random.randint(1, 100000) for _ in range(N)],

    "Sorted":
        list(range(N)),

    "Reverse":
        list(range(N, 0, -1)),

    "Nearly Sorted":
        list(range(N))
}

# Make Nearly Sorted slightly shuffled

nearly = test_cases["Nearly Sorted"]

for _ in range(N // 20):

    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)

    nearly[i], nearly[j] = nearly[j], nearly[i]


# ==========================================
# Display Output
# ==========================================

print("=" * 90)
print("QUICK SORT PERFORMANCE COMPARISON")
print("=" * 90)

print(
    f"{'Input Type':<18}"
    f"{'DQS Comparisons':>18}"
    f"{'DQS Time(ms)':>15}"
    f"{'RQS Comparisons':>18}"
    f"{'RQS Time(ms)':>15}"
)

print("-" * 90)

for name, arr in test_cases.items():

    d_comp, d_time = run_algorithm(
        deterministic_quicksort,
        arr
    )

    r_comp, r_time = run_algorithm(
        randomized_quicksort,
        arr
    )

    print(
        f"{name:<18}"
        f"{d_comp:>18}"
        f"{d_time:>15.2f}"
        f"{r_comp:>18}"
        f"{r_time:>15.2f}"
    )


print("\n")
print("=" * 90)
print("COMPLEXITY")
print("=" * 90)

print("Deterministic Quick Sort")
print("Average Time : O(n log n)")
print("Worst Time   : O(n²)")
print()

print("Randomized Quick Sort")
print("Expected Time : O(n log n)")
print("Worst Time    : O(n²)")

print("\nExperiment Completed Successfully.")