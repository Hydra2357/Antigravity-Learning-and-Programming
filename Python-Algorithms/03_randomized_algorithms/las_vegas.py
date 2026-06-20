"""
Las Vegas Algorithm Demo - Randomized N-Queens
Unlike Monte Carlo algorithms, Las Vegas algorithms ALWAYS produce a correct answer,
but their execution time (or number of iterations) is a random variable.
Here, we solve the N-Queens problem by placing queens randomly row-by-row.
If we reach a state where no safe square is available in the current row, we abort and restart from row 0.
"""

import random

def solve_n_queens_las_vegas(n):
    """
    Attempts to solve N-Queens randomly.
    Restarts the entire board when a dead-end is reached.
    Returns (solution_board, total_restarts).
    """
    restarts = 0
    while True:
        board = [-1] * n
        success = True
        
        for row in range(n):
            # Find all safe columns in the current row
            safe_cols = []
            for col in range(n):
                if is_safe(board, row, col):
                    safe_cols.append(col)
                    
            if not safe_cols:
                # Dead-end! Restart.
                success = False
                restarts += 1
                break
                
            # Randomly select a safe column
            board[row] = random.choice(safe_cols)
            
        if success:
            return board, restarts

def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row] = col."""
    for r in range(row):
        c = board[r]
        # Same column or same diagonals
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

if __name__ == "__main__":
    print("=== Las Vegas Algorithm Demo (Randomized N-Queens) ===")
    
    for n in [4, 6, 8, 10]:
        print(f"\nSolving {n}-Queens:")
        board, restarts = solve_n_queens_las_vegas(n)
        print(f"  Successfully solved!")
        print(f"  Number of restarts required: {restarts}")
        print(f"  Final queen placements: {board}")
        
        # Display board for n = 4 or 8
        if n in [4, 8]:
            for r in range(n):
                row_str = ["Q" if board[r] == c else "." for c in range(n)]
                print("  " + " ".join(row_str))
