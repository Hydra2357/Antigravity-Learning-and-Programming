"""
Randomized Sorting vs Deterministic Sorting
Demonstrates the performance difference between:
1. Deterministic QuickSort (uses first element as pivot)
2. Randomized QuickSort (uses random element as pivot)
On worst-case inputs (already sorted arrays).
"""

import time
import sys
import random

# Increase recursion depth for deterministic quicksort on sorted arrays
sys.setrecursionlimit(5000)

def deterministic_quicksort(arr):
    a = list(arr)
    _det_quicksort(a, 0, len(a) - 1)
    return a

def _det_quicksort(arr, low, high):
    if low < high:
        p_idx = det_partition(arr, low, high)
        _det_quicksort(arr, low, p_idx - 1)
        _det_quicksort(arr, p_idx + 1, high)

def det_partition(arr, low, high):
    # Pivot is the first element (low)
    pivot = arr[low]
    # Swap to end for partition logic
    arr[low], arr[high] = arr[high], arr[low]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr):
    a = list(arr)
    _rand_quicksort(a, 0, len(a) - 1)
    return a

def _rand_quicksort(arr, low, high):
    if low < high:
        p_idx = rand_partition(arr, low, high)
        _rand_quicksort(arr, low, p_idx - 1)
        _rand_quicksort(arr, p_idx + 1, high)

def rand_partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    print("=== Randomized vs Deterministic Sorting Demo ===")
    
    # 1. Random Input (Average Case)
    n_rand = 1000
    rand_input = [random.randint(1, 10000) for _ in range(n_rand)]
    
    start = time.perf_counter()
    res1 = deterministic_quicksort(rand_input)
    det_rand_time = time.perf_counter() - start
    
    start = time.perf_counter()
    res2 = randomized_quicksort(rand_input)
    rand_rand_time = time.perf_counter() - start
    
    print(f"\nAverage Case (Random Input of size {n_rand}):")
    print(f"  - Deterministic QuickSort: {det_rand_time:.6f} seconds")
    print(f"  - Randomized QuickSort:    {rand_rand_time:.6f} seconds")
    
    # 2. Sorted Input (Worst Case for Deterministic QuickSort)
    n_sorted = 1500
    sorted_input = list(range(n_sorted))
    
    print(f"\nWorst Case (Sorted Input of size {n_sorted}):")
    
    # Run deterministic (can be slow or hit recursion limit)
    try:
        start = time.perf_counter()
        _ = deterministic_quicksort(sorted_input)
        det_sort_time = time.perf_counter() - start
        print(f"  - Deterministic QuickSort: {det_sort_time:.6f} seconds")
    except RecursionError:
        print("  - Deterministic QuickSort: Stack Overflow (Recursion Limit Exceeded)!")
        
    # Run randomized (fast)
    start = time.perf_counter()
    _ = randomized_quicksort(sorted_input)
    rand_sort_time = time.perf_counter() - start
    print(f"  - Randomized QuickSort:    {rand_sort_time:.6f} seconds")
