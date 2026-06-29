"""
Pattern 04: Prefix Sum
=======================
Use when: Repeated range sum/min/max queries needed.
Build: O(n)   Query: O(1)   Space: O(n)

Problems: Range Sum Query, Subarray Sum Equals K,
          Product Except Self, 2D Range Sum Query
"""


# ── Example 1: Range Sum Query (1D) ─────────────────────────────────────────
class RangeSumQuery:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + v

    def query(self, left, right):
        """Return sum of nums[left..right] inclusive. O(1)"""
        return self.prefix[right + 1] - self.prefix[left]


# ── Example 2: Subarray Sum Equals K ────────────────────────────────────────
def subarray_sum(nums, k):
    """Count subarrays with sum == k. O(n)"""
    from collections import defaultdict
    count = 0
    prefix = 0
    freq = defaultdict(int)
    freq[0] = 1
    for num in nums:
        prefix += num
        count += freq[prefix - k]
        freq[prefix] += 1
    return count


# ── Example 3: Product of Array Except Self ──────────────────────────────────
def product_except_self(nums):
    """For each i, product of all elements except nums[i]. O(n), no division"""
    n = len(nums)
    result = [1] * n
    # Left prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    # Right suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


# ── Example 4: 2D Range Sum Query ────────────────────────────────────────────
class NumMatrix:
    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.dp[r+1][c+1] = (matrix[r][c]
                                     + self.dp[r][c+1]
                                     + self.dp[r+1][c]
                                     - self.dp[r][c])

    def sum_region(self, r1, c1, r2, c2):
        """Sum of rectangle defined by top-left (r1,c1) bottom-right (r2,c2)."""
        return (self.dp[r2+1][c2+1]
                - self.dp[r1][c2+1]
                - self.dp[r2+1][c1]
                + self.dp[r1][c1])


if __name__ == "__main__":
    print("=== Prefix Sum Demo ===\n")

    rsq = RangeSumQuery([1, 2, 3, 4, 5])
    print("Range Sum [0,2] →", rsq.query(0, 2))   # 6
    print("Range Sum [1,4] →", rsq.query(1, 4))   # 14

    print("Subarray sum=2 in [1,1,1] →", subarray_sum([1, 1, 1], 2))  # 2

    print("Product Except Self [1,2,3,4] →", product_except_self([1, 2, 3, 4]))

    mat = NumMatrix([[3, 0, 1, 4, 2],
                     [5, 6, 3, 2, 1],
                     [1, 2, 0, 1, 5],
                     [4, 1, 0, 1, 7],
                     [1, 0, 3, 0, 5]])
    print("2D Sum Region (2,1)-(4,3) →", mat.sum_region(2, 1, 4, 3))  # 8
