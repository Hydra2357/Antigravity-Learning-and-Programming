"""
Amortized Analysis Demo - Dynamic Array simulation.
Demonstrates that while a single insertion in a dynamic array can take O(N) time (due to capacity expansion),
a sequence of N insertions takes O(N) time in total, giving an amortized cost of O(1) per operation.
We compare this against a "bad" resizing strategy (e.g., incremental resize by constant +1)
which has an amortized cost of O(N).
"""

class DynamicArray:
    def __init__(self, growth_factor=2):
        self.capacity = 1
        self.size = 0
        self.growth_factor = growth_factor
        self.elements = [None] * self.capacity

    def push(self):
        """
        Inserts an element. Returns the 'cost' of the operation.
        Cost is measured as:
        - 1 for the write itself.
        - If expansion occurs, we add the cost of copying existing elements (size).
        """
        cost = 1
        if self.size == self.capacity:
            # Resize needed
            old_capacity = self.capacity
            self.capacity = int(old_capacity * self.growth_factor)
            
            # Simulate copy cost
            cost += self.size
            
            # Real allocate & copy
            new_elements = [None] * self.capacity
            for i in range(self.size):
                new_elements[i] = self.elements[i]
            self.elements = new_elements
            
        self.elements[self.size] = 1
        self.size += 1
        return cost

class IncrementalArray:
    """
    An array that expands its capacity by +1 every time it gets full.
    This leads to quadratic total time and O(N) amortized time.
    """
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.elements = [None] * self.capacity

    def push(self):
        cost = 1
        if self.size == self.capacity:
            # Resize by +1
            self.capacity += 1
            cost += self.size
            new_elements = [None] * self.capacity
            for i in range(self.size):
                new_elements[i] = self.elements[i]
            self.elements = new_elements
        self.elements[self.size] = 1
        self.size += 1
        return cost

if __name__ == "__main__":
    print("=== Amortized Analysis Simulation ===")
    
    n_ops = 32
    
    print(f"\n1. Doubling Dynamic Array (Growth Factor = 2):")
    arr_double = DynamicArray(growth_factor=2)
    total_cost_double = 0
    print(f"{'Op #':<6} | {'New Size':<8} | {'New Cap':<8} | {'Op Cost':<8} | {'Cumul Cost':<10} | {'Amortized Cost':<14}")
    print("-" * 65)
    for i in range(1, n_ops + 1):
        cost = arr_double.push()
        total_cost_double += cost
        amortized = total_cost_double / i
        print(f"{i:<6d} | {arr_double.size:<8d} | {arr_double.capacity:<8d} | {cost:<8d} | {total_cost_double:<10d} | {amortized:<14.3f}")

    print(f"\nTotal cost for {n_ops} inserts: {total_cost_double}. Amortized cost: {total_cost_double / n_ops:.3f} per operation (Constant O(1)).")

    print(f"\n2. Incremental Resizing Array (Growth Factor = +1):")
    arr_incremental = IncrementalArray()
    total_cost_inc = 0
    print(f"{'Op #':<6} | {'New Size':<8} | {'New Cap':<8} | {'Op Cost':<8} | {'Cumul Cost':<10} | {'Amortized Cost':<14}")
    print("-" * 65)
    for i in range(1, n_ops + 1):
        cost = arr_incremental.push()
        total_cost_inc += cost
        amortized = total_cost_inc / i
        print(f"{i:<6d} | {arr_incremental.size:<8d} | {arr_incremental.capacity:<8d} | {cost:<8d} | {total_cost_inc:<10d} | {amortized:<14.3f}")

    print(f"\nTotal cost for {n_ops} inserts: {total_cost_inc}. Amortized cost: {total_cost_inc / n_ops:.3f} per operation (Linear O(N)).")
