"""
Randomized QuickSort (Las Vegas algorithm)
Uses a random index for the pivot to avoid O(N^2) worst-case on sorted/nearly-sorted inputs.
Expected Time Complexity: O(N log N)
Worst-case Time Complexity: O(N^2) (probability is extremely low)
Space Complexity: O(log N) expected stack space.
"""

import random

def randomized_quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)
    return arr

def _quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        p_idx = randomized_partition(arr, low, high)
        _quicksort(arr, low, p_idx - 1)
        _quicksort(arr, p_idx + 1, high)

def randomized_partition(arr, low, high):
    # Select pivot randomly from low to high
    pivot_idx = random.randint(low, high)
    # Swap randomized pivot with high element
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
    print("=== Randomized QuickSort Demo ===")
    
    # Test random array
    test_arr = [10, 7, 8, 9, 1, 5, 2, 8, 3]
    print(f"Original array: {test_arr}")
    sorted_arr = randomized_quicksort(test_arr)
    print(f"Sorted array:   {sorted_arr}")
    
    # Test on already sorted array (problematic for standard deterministic QuickSort)
    sorted_input = list(range(1, 100))
    # Randomized QuickSort will shuffle pivot selections, preventing O(N^2) behavior
    res = randomized_quicksort(sorted_input)
    print(f"Sorted input of size {len(res)} sorted successfully!")
