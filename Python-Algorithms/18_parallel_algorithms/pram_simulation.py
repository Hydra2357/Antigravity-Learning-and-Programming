"""
PRAM Machine Simulation - Parallel Reduction and Prefix Sum (Scan)
PRAM (Parallel Random Access Machine) is a theoretical model for parallel algorithms where
multiple processors share a common memory.
This file simulates:
1. Parallel Reduction (Summing an array):
   - Combines elements in binary tree fashion.
   - Time Complexity: O(log N) parallel steps using O(N) processors.
2. Parallel Prefix Sum (Blelloch Scan):
   - Computes running sum of an array.
   - Consists of an Up-Sweep (reduction) phase and a Down-Sweep phase.
   - Time Complexity: O(log N) parallel steps.
"""

def parallel_reduction(arr):
    """
    Simulates a PRAM reduction summing all elements in an array.
    Modifies array in-place step-by-step.
    """
    a = list(arr)
    n = len(a)
    print(f"Initial array: {a}")
    
    step = 1
    # Run log2(N) steps
    while step < n:
        print(f"Step (stride={step}):")
        # In a real PRAM, all operations in this loop run concurrently
        for i in range(0, n, 2 * step):
            if i + step < n:
                print(f"  Processor sums index {i} and {i + step}: {a[i]} + {a[i + step]} = {a[i] + a[i + step]}")
                a[i] += a[i + step]
        step *= 2
        print(f"  Array state: {a}\n")
        
    return a[0]

def parallel_prefix_sum(arr):
    """
    Simulates Blelloch Parallel Prefix Sum (exclusive scan).
    Returns prefix sums.
    """
    # Pad array to next power of 2 for clean binary tree simulation
    n = len(arr)
    next_power_of_2 = 1
    while next_power_of_2 < n:
        next_power_of_2 *= 2
        
    a = list(arr) + [0] * (next_power_of_2 - n)
    size = next_power_of_2
    
    print(f"Padded array for scan: {a}")
    
    # 1. Up-Sweep (Reduction) Phase
    # Tree traversal bottom-to-top
    stride = 1
    while stride < size:
        for i in range(0, size, 2 * stride):
            a[i + 2 * stride - 1] += a[i + stride - 1]
        stride *= 2
        
    print(f"State after Up-Sweep:  {a}")
    
    # Clear the last element (exclusive scan seed)
    a[-1] = 0
    
    # 2. Down-Sweep Phase
    # Tree traversal top-to-bottom
    stride = size // 2
    while stride > 0:
        for i in range(0, size, 2 * stride):
            # Swap left child, set right child to left + right
            temp = a[i + stride - 1]
            a[i + stride - 1] = a[i + 2 * stride - 1]
            a[i + 2 * stride - 1] += temp
        stride //= 2
        
    # Trim to original size
    return a[:n]

if __name__ == "__main__":
    print("=== PRAM Parallel Algorithms Simulator ===")
    
    test_arr = [3, 1, 7, 0, 4, 1, 6, 3]
    
    print("1. Parallel Reduction (Sum):")
    total_sum = parallel_reduction(test_arr)
    print(f"Final Sum: {total_sum} (Expected: 25)")
    
    print("\n" + "="*40 + "\n")
    
    print("2. Parallel Prefix Sum (Exclusive Scan):")
    scan_res = parallel_prefix_sum(test_arr)
    print(f"Original: {test_arr}")
    print(f"Scan Res: {scan_res} (Expected: [0, 3, 4, 11, 11, 15, 16, 22])")
