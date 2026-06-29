"""
Pattern 02: Two Pointer
========================
Use when: Need a pair/triplet satisfying a condition in sorted or linear data.
Time:  O(n)   Space: O(1)

Problems: Two Sum (sorted), 3Sum, Container With Most Water,
          Palindrome Check, Remove Duplicates
"""


# ── Example 1: Two Sum (sorted array) ───────────────────────────────────────
def two_sum_sorted(nums, target):
    """Find pair that sums to target in sorted array. O(n)"""
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


# ── Example 2: 3Sum ──────────────────────────────────────────────────────────
def three_sum(nums):
    """Find all unique triplets that sum to zero. O(n^2)"""
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue          # skip duplicates
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


# ── Example 3: Container With Most Water ────────────────────────────────────
def max_water(height):
    """Find two lines that form container with most water. O(n)"""
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


# ── Example 4: Valid Palindrome ──────────────────────────────────────────────
def is_palindrome(s):
    """Check if string is a palindrome (ignore non-alphanumeric). O(n)"""
    s = [c.lower() for c in s if c.isalnum()]
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# ── Example 5: Remove Duplicates from Sorted Array ──────────────────────────
def remove_duplicates(nums):
    """Remove duplicates in-place and return new length. O(n)"""
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


if __name__ == "__main__":
    print("=== Two Pointer Demo ===\n")

    print("Two Sum sorted [1,2,3,4,6] target=6 →", two_sum_sorted([1, 2, 3, 4, 6], 6))
    print("3Sum [-1,0,1,2,-1,-4] →", three_sum([-1, 0, 1, 2, -1, -4]))
    print("Max Water [1,8,6,2,5,4,8,3,7] →", max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("Is Palindrome 'A man a plan a canal Panama' →", is_palindrome("A man a plan a canal Panama"))
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("Remove Duplicates length →", remove_duplicates(nums))
