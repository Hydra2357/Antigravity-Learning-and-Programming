"""
Suffix Array and LCP Array Construction
Suffix Array: Sorted array of all suffix indices of a string.
LCP Array: Longest Common Prefix array, where LCP[i] is the length of the longest common prefix between suffix SA[i] and suffix SA[i-1].
Algorithms:
- Suffix Array: O(N log^2 N) or O(N log N) using prefix doubling and rank sorting.
- LCP Array: O(N) using Kasai's algorithm.
"""

def construct_suffix_array(s):
    """
    Constructs the Suffix Array of string s.
    Time Complexity: O(N log^2 N) where N is length of s.
    """
    n = len(s)
    # Suffixes are represented by their starting indices
    suffixes = list(range(n))
    
    # Initial ranks are the character ord values
    rank = [ord(c) for c in s]
    
    k = 1
    # Sort suffixes using prefix doubling
    while k < n:
        # Sort based on current rank pair: (rank[i], rank[i + k] if i+k < n else -1)
        suffixes.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        
        # Re-assign ranks based on sorted order
        new_rank = [0] * n
        new_rank[suffixes[0]] = 0
        for i in range(1, n):
            prev = suffixes[i - 1]
            curr = suffixes[i]
            prev_pair = (rank[prev], rank[prev + k] if prev + k < n else -1)
            curr_pair = (rank[curr], rank[curr + k] if curr + k < n else -1)
            
            if prev_pair == curr_pair:
                new_rank[curr] = new_rank[prev]
            else:
                new_rank[curr] = new_rank[prev] + 1
        rank = new_rank
        k *= 2
        
    return suffixes

def construct_lcp_array(s, suffix_array):
    """
    Constructs the LCP array in O(N) time using Kasai's algorithm.
    """
    n = len(s)
    lcp = [0] * n
    # rank[i] stores the position of suffix starting at i in the suffix_array
    rank = [0] * n
    for i, sa_val in enumerate(suffix_array):
        rank[sa_val] = i
        
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1  # decrease h for the next suffix (since suffix i+1 is related to suffix j+1)
    return lcp

if __name__ == "__main__":
    print("=== Suffix Array and LCP Array Demo ===")
    
    text = "banana"
    print(f"String: '{text}'")
    
    sa = construct_suffix_array(text)
    lcp = construct_lcp_array(text, sa)
    
    print("\nSorted Suffixes (Suffix Array & LCP Array):")
    print(f"{'Index':<6} | {'SA':<3} | {'LCP':<3} | {'Suffix String'}")
    print("-" * 45)
    for i in range(len(text)):
        idx = sa[i]
        print(f"{i:<6d} | {idx:<3d} | {lcp[i]:<3d} | '{text[idx:]}'")
