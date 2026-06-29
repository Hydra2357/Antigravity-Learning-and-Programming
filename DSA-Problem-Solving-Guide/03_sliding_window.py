"""
Pattern 03: Sliding Window
===========================
Use when: Need optimum over a contiguous subarray/substring.
Time:  O(n)   Space: O(k) where k = window size or alphabet

Problems: Longest Substring Without Repeating Chars, Max Sum Subarray of Size K,
          Minimum Window Substring, Fruit Into Baskets
"""

from collections import defaultdict


# ── Example 1: Max Sum Subarray of Fixed Size K ──────────────────────────────
def max_sum_subarray(arr, k):
    """Maximum sum of any subarray of size k. O(n)"""
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


# ── Example 2: Longest Substring Without Repeating Characters ────────────────
def length_of_longest_substring(s):
    """Longest substring with all unique chars. O(n)"""
    char_index = {}
    max_len = 0
    left = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1   # shrink window
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len


# ── Example 3: Minimum Window Substring ─────────────────────────────────────
def min_window(s, t):
    """Smallest window in s containing all chars of t. O(n)"""
    if not t or not s:
        return ""
    need = Counter(t) if False else {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    have, required = 0, len(need)
    window = defaultdict(int)
    result = ""
    min_len = float("inf")
    left = 0

    for right, char in enumerate(s):
        window[char] += 1
        if char in need and window[char] == need[char]:
            have += 1
        while have == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    return result


# ── Example 4: Fruit Into Baskets (Longest Subarray with 2 distinct) ────────
def total_fruit(fruits):
    """Longest subarray with at most 2 distinct elements. O(n)"""
    basket = defaultdict(int)
    left = 0
    max_len = 0
    for right, fruit in enumerate(fruits):
        basket[fruit] += 1
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    print("=== Sliding Window Demo ===\n")

    print("Max Sum k=3 in [2,1,5,1,3,2] →", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
    print("Longest Unique Substring 'abcabcbb' →", length_of_longest_substring("abcabcbb"))
    print("Min Window 'ADOBECODEBANC' for 'ABC' →", min_window("ADOBECODEBANC", "ABC"))
    print("Fruit Baskets [1,2,1,2,3] →", total_fruit([1, 2, 1, 2, 3]))
