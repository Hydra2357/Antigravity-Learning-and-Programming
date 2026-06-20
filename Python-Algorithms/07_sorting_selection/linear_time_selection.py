"""
Linear-Time Selection (Median of Medians)
A deterministic algorithm to find the k-th smallest element in an unsorted list.
Guarantees linear running time in the worst case by finding a good pivot.
Time Complexity: O(N) worst-case.
Space Complexity: O(N) recursion stack and copies.
"""

def median_of_medians_select(arr, k):
    """
    Finds the k-th smallest element (0-indexed) in arr.
    """
    if k < 0 or k >= len(arr):
        raise ValueError("k is out of bounds")
        
    return select(arr, 0, len(arr) - 1, k)

def select(arr, low, high, k):
    if low == high:
        return arr[low]
        
    # 1. Find pivot using median of medians
    pivot_val = get_pivot(arr, low, high)
    
    # 2. Partition around pivot_val
    p_idx = partition(arr, low, high, pivot_val)
    
    # 3. Recurse based on pivot position
    if p_idx == k:
        return arr[p_idx]
    elif p_idx > k:
        return select(arr, low, p_idx - 1, k)
    else:
        return select(arr, p_idx + 1, high, k)

def get_pivot(arr, low, high):
    """
    Divides arr[low..high] into groups of 5, finds their medians,
    and recursively finds the median of those medians.
    """
    n = high - low + 1
    if n <= 5:
        # Sort small subarray and return median
        sub = sorted(arr[low : high + 1])
        return sub[len(sub) // 2]
        
    medians = []
    # Divide into groups of 5 and find medians
    for i in range(low, high + 1, 5):
        group_end = min(i + 4, high)
        group_sorted = sorted(arr[i : group_end + 1])
        medians.append(group_sorted[len(group_sorted) // 2])
        
    # Recursively find the median of the medians
    return select(medians, 0, len(medians) - 1, len(medians) // 2)

def partition(arr, low, high, pivot_val):
    # Find index of pivot_val and swap it to the end
    for i in range(low, high + 1):
        if arr[i] == pivot_val:
            arr[i], arr[high] = arr[high], arr[i]
            break
            
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    print("=== Deterministic Linear Selection (Median of Medians) Demo ===")
    
    test_arr = [12, 3, 5, 7, 4, 19, 26, 2, 100, -10, 88, 45, 1, 0, 11]
    # Sorted: [-10, 0, 1, 2, 3, 4, 5, 7, 11, 12, 19, 19, 26, 45, 88, 100]
    print(f"Array: {test_arr}")
    print(f"Sorted: {sorted(test_arr)}")
    
    for k in range(len(test_arr)):
        # Make a copy of list to prevent mutating original list across runs
        val = median_of_medians_select(list(test_arr), k)
        print(f"{k:2d}-th smallest element: {val}")
