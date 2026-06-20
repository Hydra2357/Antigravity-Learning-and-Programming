"""
Knuth-Morris-Pratt (KMP) Pattern Matching Algorithm
Searches for occurrences of a pattern within a text.
Avoids backing up in the text by preprocessing the pattern to build the Longest Prefix Suffix (LPS) array.
Time Complexity: O(N + M) where N is text length, M is pattern length.
Space Complexity: O(M) for the LPS array.
"""

def kmp_search(text, pattern):
    """
    Searches for all occurrences of pattern in text.
    Returns: List of starting indices of matches.
    """
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return list(range(n + 1))
        
    # Preprocess pattern to construct LPS array
    lps = compute_lps_array(pattern)
    
    match_indices = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            # Match found
            match_indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return match_indices

def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

if __name__ == "__main__":
    print("=== Knuth-Morris-Pratt (KMP) Demo ===")
    
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    print(f"Text:    '{text}'")
    print(f"Pattern: '{pattern}'")
    
    indices = kmp_search(text, pattern)
    print(f"Pattern found at indices: {indices}")
