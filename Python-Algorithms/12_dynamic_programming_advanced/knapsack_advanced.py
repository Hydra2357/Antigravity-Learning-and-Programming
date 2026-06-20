"""
Advanced/Optimized Knapsack Algorithms
Includes:
1. Space-Optimized 0/1 Knapsack: Uses O(W) space instead of O(N * W).
2. Unbounded Knapsack: Infinite copies of each item are available. Uses O(W) space and O(N * W) time.
"""

def zero_one_knapsack_space_optimized(capacity, weights, values):
    """
    Solves 0/1 Knapsack using O(W) space.
    """
    n = len(values)
    # dp[w] stores the maximum value that can be obtained with capacity w
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse backwards to ensure each item is used at most once
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
            
    return dp[capacity]

def unbounded_knapsack(capacity, weights, values):
    """
    Solves Unbounded Knapsack (items can be selected multiple times).
    """
    n = len(values)
    # dp[w] stores max value with capacity w
    dp = [0] * (capacity + 1)
    
    for w in range(capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
                
    return dp[capacity]

if __name__ == "__main__":
    print("=== Advanced Knapsack Demo ===")
    
    values = [10, 30, 20]
    weights = [5, 10, 15]
    capacity = 100
    
    print(f"Items: values={values}, weights={weights}, capacity={capacity}")
    
    val_01 = zero_one_knapsack_space_optimized(capacity, weights, values)
    print(f"Space-optimized 0/1 Knapsack Max Value: {val_01} (Expected: 40)")
    
    val_unbounded = unbounded_knapsack(capacity, weights, values)
    print(f"Unbounded Knapsack Max Value:          {val_unbounded} (Expected: 300 - by taking 10 of item 1)")
