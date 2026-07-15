import random
import time

# -------------------------------
# Naive String Matching Algorithm
# -------------------------------
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# -------------------------------
# KMP Algorithm
# -------------------------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# -------------------------------
# Rabin-Karp Algorithm
# -------------------------------
def rabin_karp(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)

    d = 256

    pattern_hash = 0
    text_hash = 0
    h = 1

    matches = []
    comparisons = 0

    for _ in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):

        if pattern_hash == text_hash:

            match = True

            for j in range(m):
                comparisons += 1

                if text[i + j] != pattern[j]:
                    match = False
                    break

            if match:
                matches.append(i)

        if i < n - m:
            text_hash = (
                d * (text_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return matches, comparisons


# -------------------------------
# Measure Execution Time
# -------------------------------
def run_algorithm(name, func, text, pattern):
    start = time.perf_counter()

    matches, comparisons = func(text, pattern)

    end = time.perf_counter()

    elapsed = (end - start) * 1000

    return {
        "Algorithm": name,
        "Matches": matches,
        "Comparisons": comparisons,
        "Time": elapsed
    }


# -------------------------------
# Sample Test
# -------------------------------
print("=" * 70)
print("STRING MATCHING ALGORITHMS")
print("=" * 70)

sample_text = "AABAACAADAABAABA"
sample_pattern = "AABA"

print("\nSample Text   :", sample_text)
print("Sample Pattern:", sample_pattern)

algorithms = [
    ("Naive", naive_search),
    ("KMP", kmp_search),
    ("Rabin-Karp", rabin_karp)
]

print("\nResults")
print("-" * 70)

for name, algorithm in algorithms:
    result = run_algorithm(name, algorithm, sample_text, sample_pattern)

    print(f"\n{name}")
    print("Matches          :", result["Matches"])
    print("Comparisons      :", result["Comparisons"])
    print(f"Execution Time   : {result['Time']:.6f} ms")

# -------------------------------
# Large Performance Comparison
# -------------------------------
print("\n")
print("=" * 70)
print("PERFORMANCE COMPARISON")
print("=" * 70)

random.seed(42)

text_large = "".join(random.choices("ABCD", k=10000))

pattern_lengths = [5, 10, 20, 50]

print(
    f"{'Length':<10}"
    f"{'Naive':>15}"
    f"{'KMP':>15}"
    f"{'RK':>15}"
)

print("-" * 55)

for length in pattern_lengths:

    pattern = "".join(random.choices("ABCD", k=length))

    _, naive_comp = naive_search(text_large, pattern)
    _, kmp_comp = kmp_search(text_large, pattern)
    _, rk_comp = rabin_karp(text_large, pattern)

    print(
        f"{length:<10}"
        f"{naive_comp:>15}"
        f"{kmp_comp:>15}"
        f"{rk_comp:>15}"
    )

print("\nExperiment Completed Successfully.")