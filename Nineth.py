import time
import math

# ==========================================
# First Fit Algorithm
# ==========================================

def first_fit(items, capacity=1.0):

    remaining = []
    bins = []

    for item in items:

        placed = False

        for i in range(len(remaining)):

            if remaining[i] >= item:
                remaining[i] -= item
                bins[i].append(item)
                placed = True
                break

        if not placed:
            remaining.append(capacity - item)
            bins.append([item])

    return bins


# ==========================================
# First Fit Decreasing
# ==========================================

def first_fit_decreasing(items, capacity=1.0):

    sorted_items = sorted(items, reverse=True)

    return first_fit(sorted_items, capacity)


# ==========================================
# Best Fit Decreasing
# ==========================================

def best_fit_decreasing(items, capacity=1.0):

    sorted_items = sorted(items, reverse=True)

    remaining = []
    bins = []

    for item in sorted_items:

        best_bin = -1
        minimum_space = float("inf")

        for i in range(len(remaining)):

            if remaining[i] >= item:

                leftover = remaining[i] - item

                if leftover < minimum_space:
                    minimum_space = leftover
                    best_bin = i

        if best_bin == -1:

            remaining.append(capacity - item)
            bins.append([item])

        else:

            remaining[best_bin] -= item
            bins[best_bin].append(item)

    return bins


# ==========================================
# Display Function
# ==========================================

def display_bins(title, bins):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print(f"Total Bins Used : {len(bins)}\n")

    for i, b in enumerate(bins, start=1):

        used = sum(b)

        bar = "#" * int(used * 20)

        print(
            f"Bin {i:<2}: {b} "
            f"| Used = {used:.1f} "
            f"[{bar:<20}]"
        )


# ==========================================
# Main Program
# ==========================================

items = [0.5, 0.7, 0.3, 0.9, 0.2,
         0.6, 0.8, 0.4, 0.1, 0.5]

capacity = 1.0

lower_bound = math.ceil(sum(items) / capacity)

print("=" * 70)
print("BIN PACKING APPROXIMATION ALGORITHMS")
print("=" * 70)

print(f"\nItems          : {items}")
print(f"Bin Capacity   : {capacity}")
print(f"Total Weight   : {sum(items)}")
print(f"Lower Bound    : {lower_bound}")

start = time.perf_counter()
ff = first_fit(items, capacity)
ff_time = (time.perf_counter() - start) * 1000

start = time.perf_counter()
ffd = first_fit_decreasing(items, capacity)
ffd_time = (time.perf_counter() - start) * 1000

start = time.perf_counter()
bfd = best_fit_decreasing(items, capacity)
bfd_time = (time.perf_counter() - start) * 1000

display_bins("FIRST FIT (FF)", ff)

display_bins("FIRST FIT DECREASING (FFD)", ffd)

display_bins("BEST FIT DECREASING (BFD)", bfd)

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"{'Algorithm':<25}{'Bins Used':<15}{'Execution Time (ms)'}")
print("-" * 55)

print(f"{'First Fit':<25}{len(ff):<15}{ff_time:.6f}")
print(f"{'First Fit Decreasing':<25}{len(ffd):<15}{ffd_time:.6f}")
print(f"{'Best Fit Decreasing':<25}{len(bfd):<15}{bfd_time:.6f}")

print(f"\nTheoretical Lower Bound : {lower_bound}")

print("\n")
print("=" * 70)
print("COMPLEXITY")
print("=" * 70)

print("First Fit               : O(n²)")
print("First Fit Decreasing    : O(n log n + n²)")
print("Best Fit Decreasing     : O(n log n + n²)")

print("\nExperiment Completed Successfully.")