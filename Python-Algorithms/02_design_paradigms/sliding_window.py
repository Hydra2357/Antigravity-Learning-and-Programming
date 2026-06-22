"""
Sliding Window Pattern Suite
============================
This module implements all variations of the Sliding Window algorithmic pattern in Python.
The sliding window technique is used to perform required operations on a specific window 
size of a given array or string, reducing the time complexity from O(N^2) or O(N^3) to O(N).

Included Patterns:
1. Fixed Size Sliding Window
   - Max Sum Subarray of Size K
   - Find All Anagrams in a String
2. Variable Size Sliding Window (Shrinkable)
   - Longest Subarray with Sum <= K
   - Minimum Size Subarray Sum >= Target
   - Longest Substring with At Most K Distinct Characters
3. Variable Size Sliding Window (Non-Shrinkable / Shift-Only)
   - Max Consecutive Ones III (Shrinkable vs Non-Shrinkable comparison)
4. Sliding Window with Monotonic Deque
   - Sliding Window Maximum
5. Two-String Sliding Window
   - Minimum Window Substring
"""

from typing import List, Dict, Tuple
from collections import deque, Counter

# ==============================================================================
# 1. FIXED SIZE SLIDING WINDOW
# ==============================================================================

def max_sum_subarray(arr: List[int], k: int) -> int:
    """
    Finds the maximum sum of any contiguous subarray of size k.
    
    Intuition:
    Maintain a running sum of a window of size k. As we slide the window one 
    element to the right, add the new element and subtract the element that 
    just left the window.

    Time Complexity: O(N) where N is the length of the array.
    Space Complexity: O(1) auxiliary space.
    """
    if not arr or k <= 0 or k > len(arr):
        return 0
        
    # Calculate sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum


def find_anagrams(s: str, p: str) -> List[int]:
    """
    Finds all start indices of p's anagrams in s.
    
    Intuition:
    A string p's anagram has the exact same character frequencies as p.
    We maintain a window of size len(p) in s and track its character counts.
    Since we only deal with character counts of a fixed alphabet size (at most 26),
    comparing two frequency maps takes O(1) time.

    Time Complexity: O(N) where N = len(s).
    Space Complexity: O(1) auxiliary space (character counts take up to O(26) space).
    """
    ns, np = len(s), len(p)
    if ns < np:
        return []
        
    p_count = Counter(p)
    s_count = Counter(s[:np])
    
    result = []
    if p_count == s_count:
        result.append(0)
        
    # Slide window of size np
    for i in range(np, ns):
        # Include new char on right
        s_count[s[i]] += 1
        # Exclude old char on left
        s_count[s[i - np]] -= 1
        if s_count[s[i - np]] == 0:
            del s_count[s[i - np]]
            
        if s_count == p_count:
            result.append(i - np + 1)
            
    return result


# ==============================================================================
# 2. VARIABLE SIZE SLIDING WINDOW (SHRINKABLE)
# ==============================================================================

def longest_subarray_sum_limit(arr: List[int], k: int) -> int:
    """
    Finds the length of the longest contiguous subarray with sum <= k.
    Assuming all elements in arr are non-negative.
    
    Intuition:
    Expand the window by moving the 'right' pointer. If the current window's sum
    exceeds k, shrink the window from the 'left' until the sum is <= k.
    Track the maximum window size at each step.

    Time Complexity: O(N) as each element is processed at most twice (by left and right).
    Space Complexity: O(1).
    """
    left = 0
    current_sum = 0
    max_len = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink from left if current sum exceeds limit k
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len


def min_subarray_len_target(arr: List[int], target: int) -> int:
    """
    Finds the minimum length of a contiguous subarray with sum >= target.
    Assuming all elements in arr are positive integers.
    
    Intuition:
    Expand the window with 'right'. Once the window sum is >= target, record
    the length and try to shrink the window from the 'left' as much as possible
    to find a smaller valid window.

    Time Complexity: O(N)
    Space Complexity: O(1).
    """
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink window from left as long as the condition (sum >= target) is met
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Finds the length of the longest substring with at most k distinct characters.
    
    Intuition:
    Expand the window with 'right'. If the number of unique characters in the window
    exceeds k, shrink the window from 'left' until we have at most k unique characters.

    Time Complexity: O(N)
    Space Complexity: O(K) for character frequencies.
    """
    if k == 0 or not s:
        return 0
        
    char_count = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        
        # Shrink the window if we have more than k distinct characters
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len


# ==============================================================================
# 3. VARIABLE SIZE SLIDING WINDOW (NON-SHRINKABLE / SHIFT-ONLY)
# ==============================================================================

def max_consecutive_ones_shrinkable(arr: List[int], k: int) -> int:
    """
    Finds the maximum number of consecutive 1s after flipping at most k 0s.
    Uses the standard SHRINKABLE sliding window technique.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left = 0
    zeros_count = 0
    max_len = 0
    
    for right in range(len(arr)):
        if arr[right] == 0:
            zeros_count += 1
            
        while zeros_count > k:
            if arr[left] == 0:
                zeros_count -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len


def max_consecutive_ones_non_shrinkable(arr: List[int], k: int) -> int:
    """
    Finds the maximum number of consecutive 1s after flipping at most k 0s.
    Uses the NON-SHRINKABLE sliding window technique.
    
    Intuition:
    If we are only interested in finding the MAXIMUM size of a valid window,
    we don't need to shrink the window when it becomes invalid. We can just shift
    the entire window to the right by incrementing 'left' once.
    This maintains the maximum window size seen so far. The window only grows when
    a new maximum size is found.
    At the end of the array, the size of the window (len(arr) - left) will represent
    the maximum valid size.

    Time Complexity: O(N) (Note: cleaner logic with no inner while-loop, better branch prediction).
    Space Complexity: O(1)
    """
    left = 0
    zeros_count = 0
    
    for right in range(len(arr)):
        if arr[right] == 0:
            zeros_count += 1
            
        # If window is invalid, slide the window by incrementing left by 1.
        # This keeps the window size constant instead of shrinking it.
        if zeros_count > k:
            if arr[left] == 0:
                zeros_count -= 1
            left += 1
            
    return len(arr) - left


# ==============================================================================
# 4. SLIDING WINDOW WITH MONOTONIC DEQUE
# ==============================================================================

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    """
    Finds the maximum element in each sliding window of size k.
    
    Intuition:
    We use a deque (double-ended queue) to store indices of elements in the window.
    We maintain a monotonic decreasing structure in the deque:
    - The value at the front of the deque is always the maximum element in the window.
    - When moving the window:
      1. Remove indices that are out of the current window's boundary.
      2. Remove indices of elements smaller than the new element (as they can 
         never be the maximum in any future window containing the new element).
      3. Add the current element index.
      4. Append the front element value to the result.

    Time Complexity: O(N) since each index is pushed and popped from the deque at most once.
    Space Complexity: O(K) for storing indices inside the deque.
    """
    if not nums or k <= 0:
        return []
    if k == 1:
        return nums
        
    deq = deque()  # Monotonically decreasing queue of indices
    result = []
    
    for i in range(len(nums)):
        # Remove elements out of the window boundary
        if deq and deq[0] < i - k + 1:
            deq.popleft()
            
        # Remove elements smaller than the current element from the back
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
            
        # Add current index
        deq.append(i)
        
        # If the window has reached size k, record the max (front of the deque)
        if i >= k - 1:
            result.append(nums[deq[0]])
            
    return result


# ==============================================================================
# 5. TWO-STRING MATCHING SLIDING WINDOW
# ==============================================================================

def min_window_substring(s: str, t: str) -> str:
    """
    Finds the minimum window substring of s that contains all characters in t.
    If no such substring exists, returns "".
    
    Intuition:
    Use a variable sliding window. 
    1. Expand the window with 'right' until it contains all characters of t (is valid).
    2. Once valid, record/update the minimum window, then shrink from 'left' 
       to see if a smaller window is also valid.
    3. Repeat this process until 'right' reaches the end.

    Time Complexity: O(|S| + |T|)
    Space Complexity: O(U) where U is the number of unique characters in S and T.
    """
    if not s or not t or len(s) < len(t):
        return ""
        
    t_count = Counter(t)
    required_count = len(t_count)
    
    window_count: Dict[str, int] = {}
    formed_count = 0  # number of unique characters matching required count in t
    
    left = 0
    min_len = float('inf')
    min_window_indices = (0, 0)
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if current character's count in window matches its target count in t
        if char in t_count and window_count[char] == t_count[char]:
            formed_count += 1
            
        # Try to contract the window from left while it's valid
        while formed_count == required_count and left <= right:
            # Update min window details
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_indices = (left, right)
                
            # Remove left character
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed_count -= 1
                
            left += 1
            
    l, r = min_window_indices
    return s[l:r+1] if min_len != float('inf') else ""


# ==============================================================================
# DEMONSTRATIONS AND VERIFICATION
# ==============================================================================

if __name__ == "__main__":
    print("=== Sliding Window Patterns Verification Runner ===")
    
    # 1. Fixed Size Sliding Window Tests
    print("\n--- Testing Fixed Size Sliding Window ---")
    
    # Max Sum Subarray
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    res_max_sum = max_sum_subarray(arr1, k1)
    print(f"Max Sum Subarray of size {k1} in {arr1}: {res_max_sum}")
    assert res_max_sum == 9, "Failed Max Sum Subarray"
    
    # Find All Anagrams
    s_anag, p_anag = "cbaebabacd", "abc"
    res_anag = find_anagrams(s_anag, p_anag)
    print(f"Anagram indices of '{p_anag}' in '{s_anag}': {res_anag}")
    assert res_anag == [0, 6], "Failed Find All Anagrams"
    
    # 2. Variable Size Sliding Window (Shrinkable) Tests
    print("\n--- Testing Variable Size Sliding Window (Shrinkable) ---")
    
    # Longest Subarray with Sum <= K
    arr_sum_lim = [3, 1, 2, 1, 1, 4, 5]
    k_lim = 4
    res_sum_lim = longest_subarray_sum_limit(arr_sum_lim, k_lim)
    print(f"Longest Subarray with sum <= {k_lim} in {arr_sum_lim}: len = {res_sum_lim}")
    assert res_sum_lim == 3, "Failed Longest Subarray Sum Limit"
    
    # Minimum Size Subarray Sum >= Target
    arr_min_sub = [2, 3, 1, 2, 4, 3]
    target_min_sub = 7
    res_min_sub = min_subarray_len_target(arr_min_sub, target_min_sub)
    print(f"Min Subarray length with sum >= {target_min_sub} in {arr_min_sub}: {res_min_sub}")
    assert res_min_sub == 2, "Failed Min Subarray Length"
    
    # Longest Substring with at most K Distinct Characters
    s_dist, k_dist = "araaci", 2
    res_dist = longest_substring_k_distinct(s_dist, k_dist)
    print(f"Longest Substring with at most {k_dist} distinct chars in '{s_dist}': len = {res_dist}")
    assert res_dist == 4, "Failed Longest Substring K Distinct"
    
    # 3. Variable Size Sliding Window (Non-Shrinkable / Shift-Only) Tests
    print("\n--- Testing Variable Size Sliding Window (Non-Shrinkable) ---")
    arr_zeros = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k_zeros = 3
    res_shrink = max_consecutive_ones_shrinkable(arr_zeros, k_zeros)
    res_non_shrink = max_consecutive_ones_non_shrinkable(arr_zeros, k_zeros)
    print(f"Max Consecutive Ones (Shrinkable) with k={k_zeros}: {res_shrink}")
    print(f"Max Consecutive Ones (Non-Shrinkable) with k={k_zeros}: {res_non_shrink}")
    assert res_shrink == 10, "Failed Max Consecutive Ones (Shrinkable)"
    assert res_non_shrink == 10, "Failed Max Consecutive Ones (Non-Shrinkable)"
    assert res_shrink == res_non_shrink, "Shrinkable and Non-Shrinkable methods did not match!"
    
    # 4. Sliding Window with Monotonic Deque Tests
    print("\n--- Testing Sliding Window with Monotonic Deque ---")
    nums_max = [1, 3, -1, -3, 5, 3, 6, 7]
    k_max = 3
    res_window_max = sliding_window_max(nums_max, k_max)
    print(f"Sliding Window Maximum of size {k_max} in {nums_max}: {res_window_max}")
    assert res_window_max == [3, 3, 5, 5, 6, 7], "Failed Sliding Window Maximum"
    
    # 5. Two-String Sliding Window Tests
    print("\n--- Testing Two-String Sliding Window ---")
    s_win, t_win = "ADOBECODEBANC", "ABC"
    res_win = min_window_substring(s_win, t_win)
    print(f"Minimum Window Substring of '{s_win}' containing '{t_win}': '{res_win}'")
    assert res_win == "BANC", "Failed Minimum Window Substring"
    
    print("\nAll sliding window algorithm implementations verified successfully!")
