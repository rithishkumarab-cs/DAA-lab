import time

# ==========================================
# Check Safe Position
# ==========================================

def is_safe(board, row, col):

    for previous_row in range(row):

        previous_col = board[previous_row]

        if previous_col == col:
            return False

        if abs(previous_row - row) == abs(previous_col - col):
            return False

    return True


# ==========================================
# N Queens Solver
# ==========================================

def solve_n_queens(n):

    board = [-1] * n

    solutions = []

    backtracks = [0]

    def backtrack(row):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                backtrack(row + 1)

                board[row] = -1

                backtracks[0] += 1

    backtrack(0)

    return solutions, backtracks[0]


# ==========================================
# Display Chess Board
# ==========================================

def display_board(solution):

    n = len(solution)

    print(" +" + "---+" * n)

    for row in range(n):

        print(" |", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()

        print(" +" + "---+" * n)


# ==========================================
# Main Program
# ==========================================

print("=" * 70)
print("N-QUEENS USING BACKTRACKING")
print("=" * 70)

for n in [4, 6, 8]:

    start = time.perf_counter()

    solutions, backtracks = solve_n_queens(n)

    end = time.perf_counter()

    print(f"\nBoard Size : {n} x {n}")
    print(f"Solutions  : {len(solutions)}")
    print(f"Backtracks : {backtracks}")
    print(f"Execution Time : {(end-start)*1000:.6f} ms")

    if n == 4:

        print("\nAll Solutions for 4-Queens\n")

        for index, solution in enumerate(solutions, start=1):

            print(f"Solution {index}")
            display_board(solution)
            print()

print("=" * 70)
print("COMPLEXITY")
print("=" * 70)
print("Time Complexity  : O(N!)")
print("Space Complexity : O(N)")
print("\nExperiment Completed Successfully.")