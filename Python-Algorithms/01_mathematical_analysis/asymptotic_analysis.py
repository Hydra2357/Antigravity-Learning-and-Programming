"""
Asymptotic Analysis Demonstration
Complexity:
    - O(1): Constant time operations
    - O(log N): Binary Search style halving
    - O(N): Linear scan
    - O(N log N): Efficient sorting style
    - O(N^2): Quadratic nested loops
    - O(2^N): Exponential doubling recursive calls
"""

import time
import math
import random

def constant_time(arr):
    # O(1)
    if len(arr) > 0:
        return arr[0]
    return None

def logarithmic_time(n):
    # O(log N)
    count = 0
    val = n
    while val > 1:
        val //= 2
        count += 1
    return count

def linear_time(arr):
    # O(N)
    count = 0
    for x in arr:
        count += x
    return count

def n_log_n_time(arr):
    # O(N log N) - standard merge sort or similar work
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = n_log_n_time(arr[:mid])
    right = n_log_n_time(arr[mid:])
    
    # Merge step
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

def quadratic_time(arr):
    # O(N^2)
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            count += arr[i] * arr[j]
    return count

def exponential_time(n):
    # O(2^N) - Fibonacci without memoization
    if n <= 1:
        return n
    return exponential_time(n - 1) + exponential_time(n - 2)

def profile_function(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

if __name__ == "__main__":
    print("=== Asymptotic Analysis Demo ===")
    test_sizes = [10, 100, 1000]
    
    print("\n--- O(1) Constant Time (First element lookup) ---")
    for size in test_sizes:
        arr = list(range(size))
        duration, _ = profile_function(constant_time, arr)
        print(f"N = {size:6d} | Duration: {duration:.8f} seconds")
        
    print("\n--- O(log N) Logarithmic Time (Repeated halving) ---")
    for size in [1000, 10000, 100000, 1000000]:
        duration, res = profile_function(logarithmic_time, size)
        print(f"N = {size:7d} | Steps: {res:2d} | Duration: {duration:.8f} seconds")
        
    print("\n--- O(N) Linear Time (Sum array) ---")
    for size in [1000, 10000, 100000, 1000000]:
        arr = list(range(size))
        duration, _ = profile_function(linear_time, arr)
        print(f"N = {size:7d} | Duration: {duration:.8f} seconds")

    print("\n--- O(N log N) N-Log-N Time (Merge Sort) ---")
    for size in [100, 1000, 5000]:
        arr = [random.randint(1, 1000) for _ in range(size)]
        duration, _ = profile_function(n_log_n_time, arr)
        print(f"N = {size:6d} | Duration: {duration:.8f} seconds")

    print("\n--- O(N^2) Quadratic Time (Nested loops) ---")
    for size in [100, 500, 1000]:
        arr = list(range(size))
        duration, _ = profile_function(quadratic_time, arr)
        print(f"N = {size:6d} | Duration: {duration:.8f} seconds")

    print("\n--- O(2^N) Exponential Time (Recursive Fibonacci) ---")
    for size in [10, 20, 30]:
        duration, res = profile_function(exponential_time, size)
        print(f"N = {size:2d} | Result: {res:7d} | Duration: {duration:.8f} seconds")
