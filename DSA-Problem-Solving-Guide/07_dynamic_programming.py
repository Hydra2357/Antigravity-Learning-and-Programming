"""
Pattern 07: Dynamic Programming (DP)
======================================
Use when: Problem has overlapping subproblems + optimal substructure.
Approach: Top-down (memoization) or Bottom-up (tabulation)
Time:  varies   Space: O(n) or O(n*m)

Problems: Fibonacci, Coin Change, Knapsack, LCS, LIS, Edit Distance,
          House Robber, Climbing Stairs, Partition Equal Subset Sum
"""

from functools import lru_cache


# ── Example 1: Fibonacci (memoization) ──────────────────────────────────────
def fib(n, memo={}):
    """Fibonacci with memoization. O(n)"""
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# ── Example 2: Climbing Stairs ───────────────────────────────────────────────
def climb_stairs(n):
    """Count ways to climb n stairs (1 or 2 steps). O(n)"""
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# ── Example 3: House Robber ──────────────────────────────────────────────────
def rob(nums):
    """Max money from non-adjacent houses. O(n)"""
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1


# ── Example 4: Coin Change ───────────────────────────────────────────────────
def coin_change(coins, amount):
    """Minimum coins to make amount. O(amount * len(coins))"""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


# ── Example 5: Longest Common Subsequence ────────────────────────────────────
def lcs(text1, text2):
    """Length of longest common subsequence. O(m*n)"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


# ── Example 6: 0/1 Knapsack ──────────────────────────────────────────────────
def knapsack(weights, values, capacity):
    """Max value with items of given weight within capacity. O(n*W)"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    return dp[n][capacity]


# ── Example 7: Longest Increasing Subsequence ────────────────────────────────
def lis(nums):
    """Length of longest strictly increasing subsequence. O(n log n)"""
    import bisect
    sub = []
    for num in nums:
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num
    return len(sub)


if __name__ == "__main__":
    print("=== Dynamic Programming Demo ===\n")

    print("Fibonacci(10) →", fib(10))
    print("Climb Stairs(5) →", climb_stairs(5))
    print("House Robber [2,7,9,3,1] →", rob([2, 7, 9, 3, 1]))
    print("Coin Change coins=[1,5,11] amount=15 →", coin_change([1, 5, 11], 15))
    print("LCS 'abcde','ace' →", lcs("abcde", "ace"))
    print("Knapsack weights=[1,3,4,5] values=[1,4,5,7] cap=7 →",
          knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))
    print("LIS [10,9,2,5,3,7,101,18] →", lis([10, 9, 2, 5, 3, 7, 101, 18]))
