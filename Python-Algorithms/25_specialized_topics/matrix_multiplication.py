"""
Matrix Multiplication Optimizations - Strassen's Algorithm
Includes:
1. Standard Matrix Multiplication: O(N^3) time.
2. Strassen's Algorithm: O(N^log2(7)) ~ O(N^2.807) time.
   - Divides matrices recursively into quadrants and uses 7 multiplications instead of 8.
   - Designed for power-of-2 square matrices.
"""

def add_matrices(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]

def sub_matrices(a, b):
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]

def standard_matrix_multiply(a, b):
    """O(N^3) standard matrix multiplication."""
    n = len(a)
    c = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def strassen_multiply(a, b):
    """
    Strassen's matrix multiplication.
    Assumes size of a and b is N x N where N is a power of 2.
    """
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]
        
    mid = n // 2
    
    # Split matrices into quadrants
    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]
    
    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]
    
    # 7 Strassen products
    # P1 = A11 * (B12 - B22)
    p1 = strassen_multiply(a11, sub_matrices(b12, b22))
    # P2 = (A11 + A12) * B22
    p2 = strassen_multiply(add_matrices(a11, a12), b22)
    # P3 = (A21 + A22) * B11
    p3 = strassen_multiply(add_matrices(a21, a22), b11)
    # P4 = A22 * (B21 - B11)
    p4 = strassen_multiply(a22, sub_matrices(b21, b11))
    # P5 = (A11 + A22) * (B11 + B22)
    p5 = strassen_multiply(add_matrices(a11, a22), add_matrices(b11, b22))
    # P6 = (A12 - A22) * (B21 + B22)
    p6 = strassen_multiply(sub_matrices(a12, a22), add_matrices(b21, b22))
    # P7 = (A11 - A21) * (B11 + B12)
    p7 = strassen_multiply(sub_matrices(a11, a21), add_matrices(b11, b12))
    
    # Combine quadrants
    # C11 = P5 + P4 - P2 + P6
    c11 = add_matrices(sub_matrices(add_matrices(p5, p4), p2), p6)
    # C12 = P1 + P2
    c12 = add_matrices(p1, p2)
    # C21 = P3 + P4
    c21 = add_matrices(p3, p4)
    # C22 = P5 + P1 - P3 - P7
    c22 = sub_matrices(sub_matrices(add_matrices(p5, p1), p3), p7)
    
    # Construct result matrix
    c = []
    for i in range(mid):
        c.append(c11[i] + c12[i])
    for i in range(mid):
        c.append(c21[i] + c22[i])
        
    return c

if __name__ == "__main__":
    print("=== Matrix Multiplication Optimizations ===")
    
    a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ]
    
    b = [
        [9, 8, 7, 6],
        [5, 4, 3, 2],
        [1, 0, 9, 8],
        [7, 6, 5, 4]
    ]
    
    print("Matrix A:")
    for r in a:
        print(f"  {r}")
    print("\nMatrix B:")
    for r in b:
        print(f"  {r}")
        
    c_std = standard_matrix_multiply(a, b)
    c_strassen = strassen_multiply(a, b)
    
    print("\nResult (Standard O(N^3)):")
    for r in c_std:
        print(f"  {r}")
        
    print("\nResult (Strassen's O(N^2.81)):")
    for r in c_strassen:
        print(f"  {r}")
        
    # Check correctness
    correct = True
    for i in range(4):
        for j in range(4):
            if c_std[i][j] != c_strassen[i][j]:
                correct = False
                
    print(f"\nAre both results identical? {correct}")
