"""
Linear Programming Duality
Demonstrates the relationship between a primal LP and its dual.
Primal (Maximization):
  Maximize   c^T * x
  Subject to A * x <= b, x >= 0
Dual (Minimization):
  Minimize   b^T * y
  Subject to A^T * y >= c, y >= 0

Strong Duality Theorem:
  If either primal or dual has an optimal solution, then both do, and Max(c^T * x) = Min(b^T * y).
This script:
1. Takes a primal LP.
2. Constructs the dual LP.
3. Solves both using the Simplex solver (by rewriting dual as a maximization problem).
4. Verifies strong duality.
"""

from simplex import SimplexSolver

def solve_dual_lp(primal_c, primal_A, primal_b):
    """
    Constructs and solves the dual LP.
    Primal constraints: A * x <= b (M constraints, N variables)
    Dual variables: y (length M)
    Dual objective coefficients: primal_b
    Dual constraints: A^T * y >= primal_c  ==>  -A^T * y <= -primal_c
    Dual objective: Minimize b^T * y  ==>  Maximize -b^T * y
    """
    m_constraints = len(primal_b)
    n_vars = len(primal_c)
    
    # 1. Construct Dual Objective c_dual = -primal_b
    dual_c = [-val for val in primal_b]
    
    # 2. Construct Dual Constraints A_dual = -A^T, b_dual = -primal_c
    dual_A = [[0.0] * m_constraints for _ in range(n_vars)]
    for i in range(n_vars):
        for j in range(m_constraints):
            dual_A[i][j] = -float(primal_A[j][i])
            
    dual_b = [-val for val in primal_c]
    
    # 3. Solve the dual maximization problem using Simplex
    solver = SimplexSolver(dual_c, dual_A, dual_b)
    dual_sol, max_val_negative = solver.solve()
    
    # The minimum cost of dual is -max_val_negative
    min_dual_value = -max_val_negative
    return dual_sol, min_dual_value

if __name__ == "__main__":
    print("=== Linear Programming Duality Demo ===")
    
    # Primal:
    # Maximize   z = 3*x1 + 5*x2
    # Subject to  1*x1 + 0*x2 <= 4
    #             0*x1 + 2*x2 <= 12
    #             3*x1 + 2*x2 <= 18
    primal_c = [3.0, 5.0]
    primal_A = [
        [1.0, 0.0],
        [0.0, 2.0],
        [3.0, 2.0]
    ]
    primal_b = [4.0, 12.0, 18.0]
    
    # 1. Solve Primal
    primal_solver = SimplexSolver(primal_c, primal_A, primal_b)
    primal_sol, primal_val = primal_solver.solve()
    
    # 2. Solve Dual
    dual_sol, dual_val = solve_dual_lp(primal_c, primal_A, primal_b)
    
    print("\n--- Primal LP (Maximization) ---")
    print(f"  Optimal Variables: x = {primal_sol}")
    print(f"  Maximum Value:     {primal_val:.4f}")
    
    print("\n--- Dual LP (Minimization) ---")
    print(f"  Optimal Variables: y = {dual_sol}")
    print(f"  Minimum Value:     {dual_val:.4f}")
    
    print("\nVerification:")
    print(f"  Primal Max Value = {primal_val:.4f}")
    print(f"  Dual Min Value   = {dual_val:.4f}")
    difference = abs(primal_val - dual_val)
    print(f"  Difference:        {difference:.8f}")
    if difference < 1e-9:
        print("  Strong Duality Verified successfully!")
    else:
        print("  Duality Gap exists (check parameters).")
