"""
Pattern 08: Monotonic Stack
=============================
Use when: Need nearest greater/smaller element, or range spans.
Time:  O(n)   Space: O(n)

Problems: Next Greater Element, Daily Temperatures, Largest Rectangle
          in Histogram, Trapping Rain Water, Stock Span Problem
"""


# ── Example 1: Next Greater Element ─────────────────────────────────────────
def next_greater_element(nums):
    """For each element, find next greater to the right. O(n)"""
    result = [-1] * len(nums)
    stack = []   # holds indices, stack is monotonically decreasing
    for i, val in enumerate(nums):
        while stack and nums[stack[-1]] < val:
            idx = stack.pop()
            result[idx] = val
        stack.append(i)
    return result


# ── Example 2: Daily Temperatures ───────────────────────────────────────────
def daily_temperatures(temps):
    """Days to wait for a warmer temperature. O(n)"""
    result = [0] * len(temps)
    stack = []   # holds indices
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


# ── Example 3: Largest Rectangle in Histogram ────────────────────────────────
def largest_rectangle(heights):
    """Largest rectangle area in histogram. O(n)"""
    stack = []   # monotonically increasing
    max_area = 0
    heights = heights + [0]   # sentinel to flush stack
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    return max_area


# ── Example 4: Trapping Rain Water ───────────────────────────────────────────
def trap_rain_water(height):
    """Total rain water trapped. O(n) two-pointer approach."""
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water


# ── Example 5: Stock Span Problem ────────────────────────────────────────────
def stock_span(prices):
    """Span of stock prices (consecutive days price <= today). O(n)"""
    spans = []
    stack = []   # (price, span)
    for price in prices:
        span = 1
        while stack and stack[-1][0] <= price:
            span += stack.pop()[1]
        stack.append((price, span))
        spans.append(span)
    return spans


if __name__ == "__main__":
    print("=== Monotonic Stack Demo ===\n")

    print("Next Greater [2,1,2,4,3] →", next_greater_element([2, 1, 2, 4, 3]))
    print("Daily Temps [73,74,75,71,69,72,76,73] →",
          daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print("Largest Rectangle [2,1,5,6,2,3] →", largest_rectangle([2, 1, 5, 6, 2, 3]))
    print("Trap Rain Water [0,1,0,2,1,0,1,3,2,1,2,1] →",
          trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print("Stock Span [100,80,60,70,60,75,85] →",
          stock_span([100, 80, 60, 70, 60, 75, 85]))
