"""
Divide and Conquer Paradigm Demo
Includes:
1. Merge Sort: O(N log N) time, O(N) space.
2. Binary Search (Recursive): O(log N) time, O(log N) recursion stack space.
"""

def merge_sort(arr):
    """
    Sorts an array using Divide and Conquer Merge Sort.
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer & Combine
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def binary_search(arr, low, high, x):
    """
    Finds index of x in sorted array arr, or -1 if not present.
    """
    if high >= low:
        # Divide
        mid = (high + low) // 2
        
        # Conquer
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

if __name__ == "__main__":
    print("=== Divide and Conquer Demo ===")
    
    # Test Merge Sort
    unsorted = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(unsorted)
    print(f"Merge Sort: {unsorted} -> {sorted_arr}")
    
    # Test Binary Search
    target = 27
    idx = binary_search(sorted_arr, 0, len(sorted_arr) - 1, target)
    print(f"Binary Search: Finding {target} in {sorted_arr} -> Index: {idx}")
    
    target_missing = 100
    idx_missing = binary_search(sorted_arr, 0, len(sorted_arr) - 1, target_missing)
    print(f"Binary Search: Finding {target_missing} in {sorted_arr} -> Index: {idx_missing}")
