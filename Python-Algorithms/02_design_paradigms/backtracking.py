"""
Backtracking Paradigm Demo
Includes:
- N-Queens Solver: Finds all valid placements of N queens on an NxN chessboard such that no two queens attack each other.
Time Complexity: O(N!)
Space Complexity: O(N) recursion stack
"""

def solve_n_queens(n):
    """
    Solves the N-Queens problem.
    Returns a list of solutions, where each solution is a list of column indices.
    For example, [1, 3, 0, 2] means:
    - Queen at row 0 is in col 1
    - Queen at row 1 is in col 3
    - Queen at row 2 is in col 0
    - Queen at row 3 is in col 2
    """
    solutions = []
    # Tracks column occupancy and diagonal occupancy:
    # main diagonal: row - col is constant
    # anti-diagonal: row + col is constant
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # row - col + (n-1)
    diag2 = [False] * (2 * n - 1)  # row + col
    
    board = [-1] * n
    
    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
            
        for col in range(n):
            d1_idx = row - col + (n - 1)
            d2_idx = row + col
            
            # Check safety
            if not cols[col] and not diag1[d1_idx] and not diag2[d2_idx]:
                # Place Queen
                board[row] = col
                cols[col] = True
                diag1[d1_idx] = True
                diag2[d2_idx] = True
                
                # Recurse
                backtrack(row + 1)
                
                # Backtrack / Remove Queen
                board[row] = -1
                cols[col] = False
                diag1[d1_idx] = False
                diag2[d2_idx] = False
                
    backtrack(0)
    return solutions

def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = []
        for col in range(n):
            if solution[row] == col:
                line.append("Q")
            else:
                line.append(".")
        print(" ".join(line))

if __name__ == "__main__":
    print("=== Backtracking N-Queens Solver ===")
    n = 4
    solutions = solve_n_queens(n)
    print(f"Total solutions for {n}-Queens: {len(solutions)}")
    for idx, sol in enumerate(solutions):
        print(f"\nSolution #{idx + 1}: {sol}")
        print_board(sol)
        
    print("\nScaling check:")
    for size in range(1, 9):
        sols = solve_n_queens(size)
        print(f"Queens: {size} | Solutions: {len(sols)}")
