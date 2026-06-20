"""
Longest Increasing Subsequence (LIS)
Computes the length and actual sequence of the longest increasing subsequence in an array.
Uses binary search (patience sorting style).
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

import bisect

def longest_increasing_subsequence(arr):
    """
    Computes LIS.
    Returns: (lis_length, lis_sequence)
    """
    if not arr:
        return 0, []
        
    n = len(arr)
    # tails[i] stores index of the smallest tail of all increasing subsequences of length i+1
    tails = []
    # parent[i] stores index of the predecessor of arr[i] in LIS
    parent = [-1] * n
    
    # We store indices in tails rather than values, to help reconstruct path
    for i in range(n):
        # Binary search to find where arr[i] fits in tails values
        low = 0
        high = len(tails)
        while low < high:
            mid = (low + high) // 2
            if arr[tails[mid]] < arr[i]:
                low = mid + 1
            else:
                high = mid
                
        idx = low
        if idx == len(tails):
            tails.append(i)
        else:
            tails[idx] = i
            
        if idx > 0:
            parent[i] = tails[idx - 1]
            
    # Reconstruct LIS sequence
    lis_len = len(tails)
    lis_seq = []
    curr = tails[-1]
    while curr != -1:
        lis_seq.append(arr[curr])
        curr = parent[curr]
        
    lis_seq.reverse()
    return lis_len, lis_seq

if __name__ == "__main__":
    print("=== Longest Increasing Subsequence Demo ===")
    
    test_arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    length, seq = longest_increasing_subsequence(test_arr)
    print(f"Array: {test_arr}")
    print(f"LIS Length: {length} (Expected: 6)")
    print(f"LIS Sequence: {seq} (Expected: [10, 22, 33, 50, 60, 80] or similar)")
