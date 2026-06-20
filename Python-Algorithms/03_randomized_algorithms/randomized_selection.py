"""
Randomized Selection (QuickSelect)
Finds the k-th smallest element in an unsorted list in expected linear time.
Expected Time Complexity: O(N)
Worst-case Time Complexity: O(N^2)
Space Complexity: O(1) auxiliary space (using an iterative approach).
"""

import random

def randomized_select(arr, k):
    """
    Finds the k-th smallest element (0-indexed).
    So k = 0 finds the minimum element.
    k = len(arr) - 1 finds the maximum element.
    """
    if k < 0 or k >= len(arr):
        raise ValueError("k is out of bounds")
    
    # Work on a copy to avoid mutating user's array
    a = list(arr)
    low = 0
    high = len(a) - 1
    
    while low <= high:
        if low == high:
            return a[low]
            
        p_idx = randomized_partition(a, low, high)
        
        # Determine relationship to target index k
        if p_idx == k:
            return a[p_idx]
        elif p_idx > k:
            high = p_idx - 1
        else:
            low = p_idx + 1

def randomized_partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    print("=== Randomized Selection (QuickSelect) Demo ===")
    
    test_arr = [12, 3, 5, 7, 4, 19, 26, 2]
    # Sorted order of test_arr: [2, 3, 4, 5, 7, 12, 19, 26]
    print(f"Array: {test_arr}")
    print(f"Sorted array: {sorted(test_arr)}")
    
    for k in range(len(test_arr)):
        val = randomized_select(test_arr, k)
        print(f"{k}-th smallest element: {val}")
