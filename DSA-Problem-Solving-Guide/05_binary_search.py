"""
Pattern 05: Binary Search
==========================
Use when: Fastest search in sorted data, or answer lies on a monotonic range.
Time:  O(log n)   Space: O(1)

Problems: Search in Rotated Array, Find Peak, Koko Eating Bananas,
          Median of Two Sorted Arrays, First/Last Position of Element
"""


# ── Example 1: Classic Binary Search ────────────────────────────────────────
def binary_search(arr, target):
    """Standard binary search. Returns index or -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ── Example 2: Search in Rotated Sorted Array ────────────────────────────────
def search_rotated(nums, target):
    """Binary search in a rotated sorted array. O(log n)"""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:              # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                  # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# ── Example 3: Find Peak Element ─────────────────────────────────────────────
def find_peak(nums):
    """Return index of any peak element. O(log n)"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ── Example 4: Koko Eating Bananas ───────────────────────────────────────────
def min_eating_speed(piles, h):
    """Min speed k so Koko can eat all piles in h hours. O(n log max(piles))"""
    import math
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ── Example 5: First and Last Position of Element ───────────────────────────
def search_range(nums, target):
    """Find first and last position of target. O(log n)"""
    def find_bound(is_left):
        lo, hi = 0, len(nums) - 1
        bound = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                bound = mid
                if is_left:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return bound
    return [find_bound(True), find_bound(False)]


if __name__ == "__main__":
    print("=== Binary Search Demo ===\n")

    print("Binary Search 5 in [1,3,5,7,9] →", binary_search([1, 3, 5, 7, 9], 5))
    print("Search Rotated 0 in [4,5,6,7,0,1,2] →", search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
    print("Find Peak in [1,2,3,1] →", find_peak([1, 2, 3, 1]))
    print("Koko piles=[3,6,7,11] h=8 →", min_eating_speed([3, 6, 7, 11], 8))
    print("Search Range 8 in [5,7,7,8,8,10] →", search_range([5, 7, 7, 8, 8, 10], 8))
