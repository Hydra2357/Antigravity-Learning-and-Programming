"""
Pattern 01: Hashing / Frequency Map
=====================================
Use when: Need count, frequency, or fast O(1) lookups.
Time:  O(n)   Space: O(n)

Problems: Two Sum, Anagram Check, Most Frequent Element,
          Subarray Sum Equals K, Group Anagrams
"""

from collections import Counter, defaultdict


# ── Example 1: Two Sum ──────────────────────────────────────────────────────
def two_sum(nums, target):
    """Return indices of two numbers that add to target. O(n)"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ── Example 2: Valid Anagram ─────────────────────────────────────────────────
def is_anagram(s, t):
    """Check if t is an anagram of s. O(n)"""
    return Counter(s) == Counter(t)


# ── Example 3: Most Frequent Element ────────────────────────────────────────
def most_frequent(nums):
    """Return the most frequent element. O(n)"""
    freq = Counter(nums)
    return freq.most_common(1)[0]


# ── Example 4: Group Anagrams ────────────────────────────────────────────────
def group_anagrams(words):
    """Group words that are anagrams of each other. O(n * k log k)"""
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())


# ── Example 5: Subarray Sum Equals K ────────────────────────────────────────
def subarray_sum_k(nums, k):
    """Count subarrays whose sum equals k. O(n)"""
    count = 0
    prefix = 0
    freq = defaultdict(int)
    freq[0] = 1
    for num in nums:
        prefix += num
        count += freq[prefix - k]
        freq[prefix] += 1
    return count


if __name__ == "__main__":
    print("=== Hashing / Frequency Map Demo ===\n")

    print("Two Sum [2,7,11,15], target=9 →", two_sum([2, 7, 11, 15], 9))
    print("Is Anagram ('anagram','nagaram') →", is_anagram("anagram", "nagaram"))
    print("Most Frequent [1,1,2,3,3,3] →", most_frequent([1, 1, 2, 3, 3, 3]))
    print("Group Anagrams →", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("Subarray Sum=2 in [1,1,1] →", subarray_sum_k([1, 1, 1], 2))
