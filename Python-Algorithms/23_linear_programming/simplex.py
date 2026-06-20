"""
Primal Simplex Algorithm Solver
Solves linear programming problems in standard maximization form:
Maximize   z = c^T * x
Subject to A * x <= b
           x >= 0
Uses Simplex tableaux and pivoting operations.
Time Complexity: Exponential in the worst case (Klee-Minty cube), but extremely fast (polynomial-like) in practice.
Space Complexity: O(M * N) for the tableau.
"""

class SimplexSolver:
    def __init__(self, c, A, b):
        """
        c: List of coefficients of objective function (length N)
        A: 2D list of constraint coefficients (M x N)
        b: List of constraints right-hand values (length M)
        """
        self.num_vars = len(c)
        self.num_constraints = len(b)
        
        # Build initial tableau
        # Rows: M constraints + 1 objective function row
        # Cols: N variables + M slack variables + 1 RHS column
        self.num_cols = self.num_vars + self.num_constraints + 1
        self.num_rows = self.num_constraints + 1
        
        self.table = [[0.0] * self.num_cols for _ in range(self.num_rows)]
        
        # Populate constraint rows
        for i in range(self.num_constraints):
            for j in range(self.num_vars):
                self.table[i][j] = float(A[i][j])
            # Slack variable coefficient is 1.0 for constraint i
            self.table[i][self.num_vars + i] = 1.0
            # RHS value
            self.table[i][-1] = float(b[i])
            
        # Populate objective function row (last row)
        # We write: z - c1*x1 - c2*x2 ... = 0
        for j in range(self.num_vars):
            self.table[-1][j] = -float(c[j])
        self.table[-1][-1] = 0.0

    def _get_pivot_column(self):
        """Finds column with most negative coefficient in objective row (Dantzig's rule)."""
        last_row = self.table[-1]
        min_val = 0.0
        pivot_col = -1
        for j in range(self.num_cols - 1):
            if last_row[j] < min_val:
                min_val = last_row[j]
                pivot_col = j
        return pivot_col

    def _get_pivot_row(self, pivot_col):
        """Finds pivot row using minimum ratio test."""
        min_ratio = float('inf')
        pivot_row = -1
        for i in range(self.num_constraints):
            val = self.table[i][pivot_col]
            if val > 0.0:
                ratio = self.table[i][-1] / val
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i
        return pivot_row

    def _pivot(self, row, col):
        """Performs pivoting operation on the table."""
        pivot_val = self.table[row][col]
        # Divide pivot row by pivot value
        self.table[row] = [x / pivot_val for x in self.table[row]]
        
        # Eliminate pivot variable from other rows
        for i in range(self.num_rows):
            if i != row:
                factor = self.table[i][col]
                self.table[i] = [self.table[i][j] - factor * self.table[row][j] for j in range(self.num_cols)]

    def solve(self):
        """Runs Simplex iterations until optimal."""
        while True:
            pivot_col = self._get_pivot_column()
            if pivot_col == -1:
                break  # Optimal solution reached (no negative coefficients)
                
            pivot_row = self._get_pivot_row(pivot_col)
            if pivot_row == -1:
                raise ValueError("Linear Program is unbounded!")
                
            self._pivot(pivot_row, pivot_col)
            
        # Extract solution
        solution = [0.0] * self.num_vars
        for j in range(self.num_vars):
            col = [self.table[i][j] for i in range(self.num_rows)]
            # If column is a basic column (has exactly one 1.0 and rest 0.0)
            if col.count(0.0) == self.num_rows - 1 and col.count(1.0) == 1:
                row_idx = col.index(1.0)
                solution[j] = self.table[row_idx][-1]
                
        max_value = self.table[-1][-1]
        return solution, max_value

if __name__ == "__main__":
    print("=== Simplex Solver Demo ===")
    
    # Maximize   z = 3*x1 + 5*x2
    # Subject to  1*x1 + 0*x2 <= 4
    #             0*x1 + 2*x2 <= 12
    #             3*x1 + 2*x2 <= 18
    #             x1, x2 >= 0
    c = [3.0, 5.0]
    A = [
        [1.0, 0.0],
        [0.0, 2.0],
        [3.0, 2.0]
    ]
    b = [4.0, 12.0, 18.0]
    
    solver = SimplexSolver(c, A, b)
    sol, max_val = solver.solve()
    
    print("\nMaximization Problem:")
    print("  Maximize 3*x1 + 5*x2")
    print("  Subject to:")
    print("    x1      <= 4")
    print("       2*x2 <= 12")
    print("    3*x1 + 2*x2 <= 18")
    
    print(f"\nOptimal Solution variables: x1 = {sol[0]:.2f}, x2 = {sol[1]:.2f}")
    print(f"Maximum Objective value:   {max_val:.2f} (Expected: 36.00)")
