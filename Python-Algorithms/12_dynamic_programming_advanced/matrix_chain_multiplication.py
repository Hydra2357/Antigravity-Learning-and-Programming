"""
Matrix Chain Multiplication (MCM)
Finds the most efficient way to multiply a chain of matrices.
Given a sequence of matrices, find the optimal order of multiplications to minimize scalar multiplications.
Includes optimal parenthesization printing.
Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""

def matrix_chain_order(dims):
    """
    dims: List representing matrix dimensions.
          Matrix i has dimensions dims[i] x dims[i+1].
          n is the number of matrices. len(dims) = n + 1.
    Returns: (m, s) matrices where:
             m[i][j] is the min multiplication cost.
             s[i][j] is the split index for optimal parenthesization.
    """
    n = len(dims) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    # l is chain length (l=2 to n)
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
                    
    return m, s

def get_optimal_parenthesization(s, i, j):
    """Recursively builds optimal parenthesization string."""
    if i == j:
        return f"A{i}"
    else:
        k = s[i][j]
        left = get_optimal_parenthesization(s, i, k)
        right = get_optimal_parenthesization(s, k + 1, j)
        return f"({left} x {right})"

if __name__ == "__main__":
    print("=== Matrix Chain Multiplication Demo ===")
    
    # 4 matrices:
    # A0: 10 x 20
    # A1: 20 x 30
    # A2: 30 x 40
    # A3: 40 x 30
    dims = [10, 20, 30, 40, 30]
    
    print(f"Matrix dimensions: {dims}")
    m, s = matrix_chain_order(dims)
    
    n_matrices = len(dims) - 1
    min_ops = m[0][n_matrices - 1]
    order_str = get_optimal_parenthesization(s, 0, n_matrices - 1)
    
    print(f"Minimum cost of scalar multiplications: {min_ops}")
    print(f"Optimal Parenthesization Order:          {order_str}")
