"""
Basic Dynamic Programming Demo
Includes:
1. Fibonacci Sequence & Climbing Stairs (1D DP):
   - Top-down memoized, bottom-up tabulated, and space-optimized.
2. 0/1 Knapsack Problem (Subset selection without replacement):
   - Bottom-up tabulation with traceback to retrieve selected items.
3. Coin Change (Fewest Coins) (Unbounded Knapsack):
   - Bottom-up tabulated with O(Amount) space optimization.
4. Longest Common Subsequence (LCS) (Grid DP / Multi-sequence alignment):
   - Bottom-up grid-based tabulation with traceback.
5. Edit Distance / Levenshtein Distance (Grid DP):
   - Calculating min edits (insert, delete, replace) between strings.
6. Longest Increasing Subsequence (LIS) (Sequence DP):
   - Basic O(N^2) DP pattern.
7. Matrix Chain Multiplication (MCM) (Interval DP):
   - Minimizing scalar multiplications for matrix products.
"""

# =====================================================================
# 1. Fibonacci Sequence (1D DP Pattern)
# =====================================================================

def fibonacci_memoized(n, memo=None):
    """
    Computes the N-th Fibonacci number using Top-Down DP (Memoization).
    Time Complexity: O(N)
    Space Complexity: O(N) (call stack + memo table)
    """
    if memo is None:
        memo = {}
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_tabulated(n):
    """
    Computes the N-th Fibonacci number using Bottom-Up DP (Tabulation).
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]


def fibonacci_space_optimized(n):
    """
    Computes the N-th Fibonacci number using Space-Optimized Bottom-Up DP.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return prev1


# =====================================================================
# 2. 0/1 Knapsack Problem (Bounded Selection Pattern)
# =====================================================================

def zero_one_knapsack(capacity, weights, values):
    """
    Solves 0/1 Knapsack using Bottom-Up Tabulation.
    Returns: (max_value, indices of items selected)
    Time Complexity: O(N * Capacity)
    Space Complexity: O(N * Capacity)
    """
    n = len(values)
    # dp[i][w] represents max value using first i items with weight capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Decide to include or exclude the item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
                
    # Traceback to retrieve selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
            
    selected_items.reverse()
    return dp[n][capacity], selected_items


# =====================================================================
# 3. Coin Change - Fewest Coins (Unbounded Knapsack Pattern)
# =====================================================================

def coin_change_min_coins(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount.
    Returns -1 if that amount cannot be made.
    Time Complexity: O(N * Amount) where N is the number of coin types.
    Space Complexity: O(Amount) (Space-Optimized Tabulation)
    """
    # dp[i] represents the minimum coins needed to make amount i
    # Initialize with infinity, representing unreachable amounts
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1


# =====================================================================
# 4. Longest Common Subsequence (LCS) (Grid DP Pattern)
# =====================================================================

def longest_common_subsequence(s1, s2):
    """
    Computes the Longest Common Subsequence between strings s1 and s2.
    Returns: (LCS length, LCS string)
    Time Complexity: O(M * N)
    Space Complexity: O(M * N)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    # Traceback to reconstruct the LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    lcs.reverse()
    return dp[m][n], "".join(lcs)


# =====================================================================
# 5. Edit Distance (Levenshtein Distance) (Grid DP Pattern)
# =====================================================================

def edit_distance(s1, s2):
    """
    Computes minimum operations (Insert, Delete, Replace) to convert s1 to s2.
    Time Complexity: O(M * N)
    Space Complexity: O(M * N)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting i characters from s1
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting j characters into empty s1
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete from s1
                    dp[i][j - 1],      # Insert into s1
                    dp[i - 1][j - 1]   # Replace character
                )
                
    return dp[m][n]


# =====================================================================
# 6. Longest Increasing Subsequence (LIS) (Sequence DP Pattern)
# =====================================================================

def longest_increasing_subsequence(arr):
    """
    Computes the length of the Longest Increasing Subsequence.
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    if not arr:
        return 0
        
    n = len(arr)
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)


# =====================================================================
# 7. Matrix Chain Multiplication (MCM) (Interval DP Pattern)
# =====================================================================

def matrix_chain_order(dims):
    """
    Finds the minimum multiplication operations needed to multiply matrices
    with dimensions given in dims list. A matrix i has dimensions dims[i] x dims[i+1].
    Time Complexity: O(N^3)
    Space Complexity: O(N^2)
    """
    n = len(dims) - 1  # Number of matrices
    # dp[i][j] stores minimum cost to multiply matrices from index i to j
    dp = [[0] * n for _ in range(n)]
    
    # l is the chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                # cost = cost of left subchain + cost of right subchain + cost of multiplying results
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    
    return dp[0][n - 1]


# =====================================================================
# Main / Demo execution
# =====================================================================

if __name__ == "__main__":
    print("=== Dynamic Programming Basics Demo ===")
    
    # 1. Fibonacci
    n_fib = 10
    print(f"\n1. Fibonacci of {n_fib}:")
    print(f"  - Memoized:       {fibonacci_memoized(n_fib)}")
    print(f"  - Tabulated:      {fibonacci_tabulated(n_fib)}")
    print(f"  - Space-Optimized:{fibonacci_space_optimized(n_fib)}")
    
    # 2. 0/1 Knapsack
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_val, items_picked = zero_one_knapsack(capacity, weights, values)
    print(f"\n2. 0/1 Knapsack (Capacity {capacity}):")
    print(f"  - Max Value: {max_val}")
    print(f"  - Selected Indices: {items_picked}")
    for idx in items_picked:
        print(f"    Item {idx}: Value = {values[idx]}, Weight = {weights[idx]}")
        
    # 3. Coin Change (Min Coins)
    coins = [1, 2, 5]
    change_amount = 11
    min_c = coin_change_min_coins(coins, change_amount)
    print(f"\n3. Coin Change (Min Coins to make {change_amount} using {coins}):")
    print(f"  - Min Coins: {min_c}")
    
    # 4. LCS
    s1, s2 = "ABCDGH", "AEDFHR"
    lcs_len, lcs_str = longest_common_subsequence(s1, s2)
    print(f"\n4. LCS between '{s1}' and '{s2}':")
    print(f"  - Length: {lcs_len}")
    print(f"  - LCS String: '{lcs_str}'")
    
    # 5. Edit Distance
    word1, word2 = "horse", "ros"
    ed_dist = edit_distance(word1, word2)
    print(f"\n5. Edit Distance between '{word1}' and '{word2}':")
    print(f"  - Min Operations: {ed_dist}")
    
    # 6. LIS
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis_len = longest_increasing_subsequence(arr)
    print(f"\n6. LIS of {arr}:")
    print(f"  - LIS Length: {lis_len}")
    
    # 7. Matrix Chain Multiplication
    # Dimensions of 3 matrices: 10x20, 20x30, 30x40
    dims = [10, 20, 30, 40]
    mcm_cost = matrix_chain_order(dims)
    print(f"\n7. Matrix Chain Multiplication for dimensions {dims}:")
    print(f"  - Min Scalar Multiplications: {mcm_cost}")
    print("\nAll basic DP implementations executed successfully!")
