"""
Rabin-Karp Pattern Matching Algorithm
Uses a rolling hash to find matching patterns in text.
Average and Best Time Complexity: O(N + M) where N is text length, M is pattern length.
Worst-case Time Complexity: O(N * M) (due to hash collisions).
Space Complexity: O(1) auxiliary space.
"""

def rabin_karp_search(text, pattern, prime=101, base=256):
    """
    Searches for all occurrences of pattern in text.
    Returns: List of starting indices of matches.
    """
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n < m:
        return []
        
    match_indices = []
    
    # Hash values for pattern and text window
    pattern_hash = 0
    window_hash = 0
    
    # h = pow(base, m-1) % prime
    h = 1
    for _ in range(m - 1):
        h = (h * base) % prime
        
    # Calculate initial hash values of pattern and first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime
        
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == window_hash:
            # Check characters one by one to resolve collision
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                match_indices.append(i)
                
        # Calculate hash value for next window: Remove leading digit, add trailing digit
        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Correct negative hash value
            if window_hash < 0:
                window_hash += prime
                
    return match_indices

if __name__ == "__main__":
    print("=== Rabin-Karp Algorithm Demo ===")
    
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    
    print(f"Text:    '{text}'")
    print(f"Pattern: '{pattern}'")
    
    indices = rabin_karp_search(text, pattern)
    print(f"Pattern found at indices: {indices}")
