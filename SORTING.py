"""
Comprehensive Collection of Sorting and Searching Algorithms in Python.

This module provides clean, detailed, and optimized implementations of major
sorting and searching algorithms, complete with time/space complexity analysis,
stability indicators, and a performance benchmarking suite.

Table of Contents:
------------------
I. SORTING ALGORITHMS
   1. Bubble Sort
   2. Selection Sort
   3. Insertion Sort
   4. Merge Sort
   5. Quick Sort (Lomuto & Hoare partitioning)
   6. Heap Sort
   7. Shell Sort
   8. Counting Sort (Integer-based)
   9. Radix Sort (LSD-based)
   10. Bucket Sort

II. SEARCHING ALGORITHMS
   1. Linear Search
   2. Binary Search (Iterative & Recursive)
   3. Ternary Search (Iterative & Recursive)
   4. Jump Search
   5. Interpolation Search
   6. Exponential Search

III. BENCHMARK & DEMO RUNNER
"""

from typing import List, Any, Union, Optional
import math
import random
import time


# =====================================================================
# I. SORTING ALGORITHMS
# =====================================================================

def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Bubble Sort: Compares adjacent elements and swaps them if they are in the wrong order.
    
    Complexity:
        - Time: Best O(n) [already sorted], Average O(n^2), Worst O(n^2)
        - Space: O(1) [In-place]
        - Stable: Yes
    """
    n = len(arr)
    # Make a copy to avoid mutating the input array directly in place if desired,
    # but traditionally sorting is done in-place. We mutate in-place and return.
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then array is sorted
        if not swapped:
            break
    return arr


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Selection Sort: Repeatedly finds the minimum element from the unsorted part
    and puts it at the beginning.
    
    Complexity:
        - Time: Best O(n^2), Average O(n^2), Worst O(n^2)
        - Space: O(1) [In-place]
        - Stable: No (can be made stable, but standard implementation is unstable)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: List[Any]) -> List[Any]:
    """
    Insertion Sort: Builds the final sorted array one item at a time by inserting
    each new element into its proper position within the already sorted part.
    
    Complexity:
        - Time: Best O(n) [already sorted], Average O(n^2), Worst O(n^2)
        - Space: O(1) [In-place]
        - Stable: Yes
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Merge Sort: A Divide and Conquer algorithm. It divides the input array into two halves,
    calls itself for the two halves, and then merges the two sorted halves.
    
    Complexity:
        - Time: Best O(n log n), Average O(n log n), Worst O(n log n)
        - Space: O(n) [Auxiliary space for merging]
        - Stable: Yes
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return _merge(left_half, right_half)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    """Helper function to merge two sorted arrays."""
    merged = []
    i = j = 0

    # Merge elements back in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr: List[Any]) -> List[Any]:
    """
    Quick Sort wrapper using a standard out-of-place recursive approach.
    For in-place operations, see `quick_sort_inplace`.
    
    Complexity:
        - Time: Best O(n log n), Average O(n log n), Worst O(n^2) [when pivot choice is poor]
        - Space: O(log n) stack space (O(n) worst case)
        - Stable: No
    """
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (middle element in this case to avoid worst-case for sorted inputs)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr: List[Any], low: int = 0, high: int = -1) -> List[Any]:
    """
    In-place Quick Sort implementation using Hoare's partitioning scheme.
    
    Complexity:
        - Time: Best O(n log n), Average O(n log n), Worst O(n^2)
        - Space: O(log n) recursion stack [In-place mutation of arr]
        - Stable: No
    """
    if high == -1:
        high = len(arr) - 1
        
    if low < high:
        # p_idx is partitioning index, arr[p_idx] is now at right place
        p_idx = _hoare_partition(arr, low, high)
        quick_sort_inplace(arr, low, p_idx)
        quick_sort_inplace(arr, p_idx + 1, high)
    return arr


def _hoare_partition(arr: List[Any], low: int, high: int) -> int:
    """Helper partition function utilizing Hoare's partitioning scheme."""
    pivot = arr[low + (high - low) // 2]
    i = low - 1
    j = high + 1
    
    while True:
        # Find leftmost element greater than or equal to pivot
        i += 1
        while arr[i] < pivot:
            i += 1
            
        # Find rightmost element smaller than or equal to pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        # If two indices met or crossed, return partition point
        if i >= j:
            return j
            
        arr[i], arr[j] = arr[j], arr[i]


def heap_sort(arr: List[Any]) -> List[Any]:
    """
    Heap Sort: Comparison-based sorting algorithm based on Binary Heap data structure.
    It builds a Max-Heap and repeatedly extracts the maximum element.
    
    Complexity:
        - Time: Best O(n log n), Average O(n log n), Worst O(n log n)
        - Space: O(1) [In-place]
        - Stable: No
    """
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we start from there and go backwards.
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        _heapify(arr, i, 0)
        
    return arr


def _heapify(arr: List[Any], n: int, i: int) -> None:
    """Helper to restore Max-Heap property for subtree rooted at index i."""
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left child = 2*i + 1
    r = 2 * i + 2  # right child = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than the largest so far
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        _heapify(arr, n, largest)


def shell_sort(arr: List[Any]) -> List[Any]:
    """
    Shell Sort: An extension of insertion sort that allows the exchange of far apart elements.
    It uses a gap sequence to sort sub-lists.
    
    Complexity:
        - Time: Best O(n log n), Average O(n^(3/2)) or O(n^2) depending on gap sequence, Worst O(n^2)
        - Space: O(1) [In-place]
        - Stable: No
    """
    n = len(arr)
    gap = n // 2

    # Start with a big gap, then reduce the gap
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # put temp (the original arr[i]) in its correct location
            arr[j] = temp
        gap //= 2
    return arr


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort: A non-comparison-based sorting algorithm that works by counting
    the number of objects having distinct key values.
    Note: Requires integer elements and is highly efficient for small value ranges.
    
    Complexity:
        - Time: O(n + k) where n is size and k is the range of inputs [min to max]
        - Space: O(n + k)
        - Stable: Yes
    """
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1
    
    # Initialize count array and output array
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # Store count of each character
    for num in arr:
        count_arr[num - min_val] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Build the output character array (backwards to preserve stability)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    # Copy output array back to arr
    for i in range(len(arr)):
        arr[i] = output_arr[i]
        
    return arr


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort: Non-comparison-based integer sorting algorithm.
    Sorts input keys digit by digit starting from least significant digit (LSD) to most.
    Uses Counting Sort as a stable sorting subroutine.
    
    Complexity:
        - Time: O(d * (n + k)) where d is digit count, n is element count, k is radix (10)
        - Space: O(n + k)
        - Stable: Yes
    """
    if not arr:
        return arr

    # Support negative numbers by shifting all elements if minimum is negative
    min_val = min(arr)
    shift = 0
    if min_val < 0:
        shift = -min_val
        for i in range(len(arr)):
            arr[i] += shift

    # Find the maximum number to know number of digits
    max_val = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_val // exp > 0:
        _counting_sort_for_radix(arr, exp)
        exp *= 10

    # Shift numbers back to original values if we shifted them earlier
    if shift > 0:
        for i in range(len(arr)):
            arr[i] -= shift
            
    return arr


def _counting_sort_for_radix(arr: List[int], exp: int) -> None:
    """Helper stable counting sort algorithm based on the digit represented by exp."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array backwards to keep sorting stable
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]


def bucket_sort(arr: List[float]) -> List[float]:
    """
    Bucket Sort: Divides elements into several groups (buckets) and then sorts
    each bucket individually (e.g. using Insertion Sort), and merges them.
    Suitable for floating-point numbers uniformly distributed in range [0, 1).
    
    Complexity:
        - Time: Best O(n + k), Average O(n + k), Worst O(n^2) where k is bucket count
        - Space: O(n + k)
        - Stable: Yes (if underlying sorting algorithm is stable)
    """
    if not arr:
        return arr

    # Create empty buckets
    bucket_count = len(arr)
    buckets: List[List[float]] = [[] for _ in range(bucket_count)]

    # Put array elements in different buckets based on their values
    # Assumes values are in [0, 1) range.
    # For general range, normalise the data first.
    min_val, max_val = min(arr), max(arr)
    val_range = max_val - min_val
    
    if val_range == 0:
        return arr

    for num in arr:
        # Normalize to [0, 0.9999...]
        normalized = (num - min_val) / val_range
        # Scale to match bucket count index
        bucket_idx = int(normalized * (bucket_count - 1))
        buckets[bucket_idx].append(num)

    # Sort individual buckets and concatenate
    k = 0
    for i in range(bucket_count):
        insertion_sort(buckets[i])
        for num in buckets[i]:
            arr[k] = num
            k += 1
            
    return arr


# =====================================================================
# II. SEARCHING ALGORITHMS
# =====================================================================

def linear_search(arr: List[Any], target: Any) -> int:
    """
    Linear Search: Checks every element sequentially until target is found or list ends.
    
    Complexity:
        - Time: Best O(1), Average O(n), Worst O(n)
        - Space: O(1)
    
    Returns:
        - Index of target if found, otherwise -1.
    """
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1


def binary_search(arr: List[Any], target: Any) -> int:
    """
    Binary Search (Iterative): Finds the position of target value within a sorted array
    by repeatedly dividing search interval in half.
    Note: Requires a sorted array.
    
    Complexity:
        - Time: Best O(1), Average O(log n), Worst O(log n)
        - Space: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


def binary_search_recursive(arr: List[Any], target: Any, low: int = 0, high: int = -1) -> int:
    """
    Binary Search (Recursive implementation).
    Note: Requires a sorted array.
    
    Complexity:
        - Time: Best O(1), Average O(log n), Worst O(log n)
        - Space: O(log n) recursion stack
    """
    if high == -1:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def ternary_search(arr: List[Any], target: Any) -> int:
    """
    Ternary Search (Iterative): Divides sorted array into three parts using mid1 and mid2,
    reducing search space by 2/3 at each step.
    Note: Requires a sorted array.
    
    Complexity:
        - Time: Best O(1), Average O(log3 n), Worst O(log3 n)
        - Space: O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Find two partition midpoints
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            # Target is in the first third
            high = mid1 - 1
        elif target > arr[mid2]:
            # Target is in the third third
            low = mid2 + 1
        else:
            # Target is in the middle third
            low = mid1 + 1
            high = mid2 - 1
            
    return -1


def ternary_search_recursive(arr: List[Any], target: Any, low: int = 0, high: int = -1) -> int:
    """
    Ternary Search (Recursive implementation).
    Note: Requires a sorted array.
    
    Complexity:
        - Time: Best O(1), Average O(log3 n), Worst O(log3 n)
        - Space: O(log3 n) recursion stack
    """
    if high == -1:
        high = len(arr) - 1

    if low > high:
        return -1

    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search_recursive(arr, target, low, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, target, mid2 + 1, high)
    else:
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)


def jump_search(arr: List[Any], target: Any) -> int:
    """
    Jump Search: Searches in a sorted array by jumping ahead by fixed steps
    (typically sqrt(n)) and then performing a linear search backwards.
    Note: Requires a sorted array.
    
    Complexity:
        - Time: Best O(1), Average O(sqrt(n)), Worst O(sqrt(n))
        - Space: O(1)
    """
    n = len(arr)
    if n == 0:
        return -1

    step = int(math.isqrt(n))
    prev = 0

    # Finding the block where element is present (if it is present)
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.isqrt(n))
        if prev >= n:
            return -1

    # Doing a linear search for target in block beginning with prev
    while arr[prev] < target:
        prev += 1
        # If we reached next block or end of array, element is not present
        if prev == min(step, n):
            return -1

    # If element is found
    if arr[prev] == target:
        return prev

    return -1


def interpolation_search(arr: List[Union[int, float]], target: Union[int, float]) -> int:
    """
    Interpolation Search: An improvement over Binary Search for instances where values
    in a sorted array are uniformly distributed. Estimating target's likely position
    using interpolation formula.
    Note: Requires a sorted, uniformly-distributed numeric array.
    
    Complexity:
        - Time: Best O(1), Average O(log(log n)), Worst O(n) (e.g. exponential distribution)
        - Space: O(1)
    """
    low = 0
    high = len(arr) - 1

    # Since array is sorted, target must be in range defined by corner points
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Probing the position using interpolation formula
        # pos = low + [ (x - arr[low]) * (high - low) / (arr[high] - arr[low]) ]
        pos = low + int(((float(target - arr[low]) * (high - low)) / (arr[high] - arr[low])))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


def exponential_search(arr: List[Any], target: Any) -> int:
    """
    Exponential Search: Finds range where target may exist by exponentially increasing
    indexes (1, 2, 4, 8...), then performs binary search in that range.
    Highly efficient for large, unbounded/infinite arrays.
    Note: Requires a sorted array.
    
    Complexity:
        - Time: Best O(1), Average O(log i) where i is target index, Worst O(log n)
        - Space: O(1) (or O(log n) if recursive binary search is used)
    """
    n = len(arr)
    if n == 0:
        return -1
        
    if arr[0] == target:
        return 0

    # Find range for binary search by repeated doubling
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2

    # Call binary search for the found range
    return binary_search_recursive(arr, target, i // 2, min(i, n - 1))


# =====================================================================
# III. BENCHMARK & DEMO RUNNER
# =====================================================================

def run_sorting_demo():
    print("\n" + "="*60)
    print("           I. RUNNING SORTING ALGORITHMS BENCHMARK")
    print("="*60)
    
    # Generate random test cases
    size = 1000
    original_arr = [random.randint(-1000, 1000) for _ in range(size)]
    float_arr = [random.random() for _ in range(size)] # specific for bucket sort
    
    sorting_algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort (Out-of-place)", quick_sort),
        ("Quick Sort (In-place)", quick_sort_inplace),
        ("Heap Sort", heap_sort),
        ("Shell Sort", shell_sort),
        ("Counting Sort", counting_sort),
        ("Radix Sort", radix_sort)
    ]
    
    for name, func in sorting_algorithms:
        # Copy to avoid side-effects from in-place algorithms
        test_arr = list(original_arr)
        
        start_time = time.perf_counter()
        sorted_arr = func(test_arr)
        end_time = time.perf_counter()
        
        duration = (end_time - start_time) * 1000 # ms
        
        # Verify correctness
        is_correct = (sorted_arr == sorted(original_arr))
        status = "PASSED" if is_correct else "FAILED"
        
        print(f" -> {name:<30} | Time: {duration:8.3f} ms | Status: {status}")
        
    # Bucket Sort Separate Test (since it expects range [0, 1))
    test_float = list(float_arr)
    start_time = time.perf_counter()
    sorted_float = bucket_sort(test_float)
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000
    is_correct = (sorted_float == sorted(float_arr))
    status = "PASSED" if is_correct else "FAILED"
    print(f" -> {"Bucket Sort (Floats [0, 1))":<30} | Time: {duration:8.3f} ms | Status: {status}")


def run_searching_demo():
    print("\n" + "="*60)
    print("          II. RUNNING SEARCHING ALGORITHMS DEMO")
    print("="*60)
    
    # Set up data (must be sorted for most searching algos)
    arr = sorted([random.randint(1, 10000) for _ in range(5000)])
    
    # Pick a random element from array to search for
    target = random.choice(arr)
    actual_idx = arr.index(target)
    
    print(f"Target Value to Find: {target} (Actual Index in Sorted List: {actual_idx})")
    print("-" * 60)
    
    searching_algorithms = [
        ("Linear Search", lambda a, t: linear_search(a, t)),
        ("Binary Search (Iterative)", lambda a, t: binary_search(a, t)),
        ("Binary Search (Recursive)", lambda a, t: binary_search_recursive(a, t)),
        ("Ternary Search (Iterative)", lambda a, t: ternary_search(a, t)),
        ("Ternary Search (Recursive)", lambda a, t: ternary_search_recursive(a, t)),
        ("Jump Search", lambda a, t: jump_search(a, t)),
        ("Interpolation Search", lambda a, t: interpolation_search(a, t)),
        ("Exponential Search", lambda a, t: exponential_search(a, t))
    ]
    
    for name, search_fn in searching_algorithms:
        start_time = time.perf_counter()
        found_idx = search_fn(arr, target)
        end_time = time.perf_counter()
        
        duration = (end_time - start_time) * 1000000 # microseconds
        
        # Verify index correctness (handle multiple occurrences correctly by verifying element matches)
        matches = (arr[found_idx] == target) if found_idx != -1 else False
        status = "PASSED" if matches else "FAILED"
        
        print(f" -> {name:<30} | Found at Index: {found_idx:<5} | Time: {duration:8.3f} us | Status: {status}")


if __name__ == "__main__":
    print("="*60)
    print("         SORTING AND SEARCHING ALGORITHMS LIBRARY")
    print("="*60)
    run_sorting_demo()
    run_searching_demo()
