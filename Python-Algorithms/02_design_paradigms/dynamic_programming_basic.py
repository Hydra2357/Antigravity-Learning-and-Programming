"""
Basic Dynamic Programming Demo
Includes:
1. 0/1 Knapsack Problem: Bottom-Up DP. O(N * W) time and space.
2. Longest Common Subsequence (LCS): Bottom-Up DP with traceback. O(M * N) time and space.
"""

def zero_one_knapsack(capacity, weights, values):
    """
    Solves 0/1 Knapsack.
    Returns max value and indices of items selected.
    """
    n = len(values)
    # DP Table: rows = items (0 to n), cols = capacities (0 to capacity)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
                
    # Traceback to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # If the value changed, it means the item was included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
            
    selected_items.reverse()
    return dp[n][capacity], selected_items

def longest_common_subsequence(s1, s2):
    """
    Computes LCS between strings s1 and s2.
    Returns LCS length and string representation.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    # Traceback
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

if __name__ == "__main__":
    print("=== Basic Dynamic Programming Demo ===")
    
    # 0/1 Knapsack Test
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_val, items_picked = zero_one_knapsack(capacity, weights, values)
    print(f"\n0/1 Knapsack (Capacity {capacity}):")
    print(f"Max Value: {max_val}")
    print(f"Selected Item Indices: {items_picked}")
    for idx in items_picked:
        print(f"  - Item {idx}: Value = {values[idx]}, Weight = {weights[idx]}")

    # LCS Test
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    lcs_len, lcs_str = longest_common_subsequence(s1, s2)
    print(f"\nLCS between '{s1}' and '{s2}':")
    print(f"Length: {lcs_len}")
    print(f"LCS String: '{lcs_str}'")
