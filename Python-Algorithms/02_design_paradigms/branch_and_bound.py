"""
Branch and Bound Paradigm Demo
Includes:
- 0/1 Knapsack using Branch and Bound (Best-First Search with Priority Queue)
Time Complexity: O(2^N) in the worst case, but typically much faster than backtracking due to aggressive pruning.
Space Complexity: O(2^N) space for queue.
"""

import heapq

class Item:
    def __init__(self, value, weight, idx):
        self.value = value
        self.weight = weight
        self.idx = idx
        self.ratio = value / weight

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level    # Level in decision tree
        self.profit = profit  # Cumulative profit
        self.weight = weight  # Cumulative weight
        self.bound = bound    # Upper bound of max profit in subtree

    # Define comparison operator for priority queue (min-heap in python).
    # Since we want to explore nodes with high bounds first, we store negative bounds.
    def __lt__(self, other):
        return self.bound > other.bound  # Max-heap based on bound

def calculate_bound(node, n, capacity, items):
    """
    Calculates upper bound of profit in subtree under node using greedy fractional knapsack.
    """
    if node.weight >= capacity:
        return 0
        
    profit_bound = node.profit
    total_weight = node.weight
    j = node.level + 1
    
    # Greedy fractional knapsack starting from next item
    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1
        
    # If there are items left, take fractional part of the next item
    if j < n:
        profit_bound += (capacity - total_weight) * items[j].ratio
        
    return profit_bound

def knapsack_branch_and_bound(capacity, weights, values):
    n = len(values)
    items = [Item(values[i], weights[i], i) for i in range(n)]
    
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    pq = []
    
    # Dummy root node
    u = Node(level=-1, profit=0, weight=0, bound=0.0)
    u.bound = calculate_bound(u, n, capacity, items)
    
    heapq.heappush(pq, u)
    max_profit = 0
    
    while pq:
        # Extract node with maximum bound
        u = heapq.heappop(pq)
        
        # If bound is better than max_profit so far, explore
        if u.bound > max_profit:
            # Create left child (item included)
            next_level = u.level + 1
            if next_level < n:
                # Node with next item included
                left_weight = u.weight + items[next_level].weight
                left_profit = u.profit + items[next_level].value
                
                left_node = Node(
                    level=next_level,
                    profit=left_profit,
                    weight=left_weight,
                    bound=0.0
                )
                
                if left_node.weight <= capacity and left_node.profit > max_profit:
                    max_profit = left_node.profit
                    
                left_node.bound = calculate_bound(left_node, n, capacity, items)
                
                # Push left child to queue if its bound is promising
                if left_node.bound > max_profit:
                    heapq.heappush(pq, left_node)
                    
                # Create right child (item excluded)
                right_node = Node(
                    level=next_level,
                    profit=u.profit,
                    weight=u.weight,
                    bound=0.0
                )
                right_node.bound = calculate_bound(right_node, n, capacity, items)
                
                # Push right child if its bound is promising
                if right_node.bound > max_profit:
                    heapq.heappush(pq, right_node)
                    
    return max_profit

if __name__ == "__main__":
    print("=== Branch and Bound Knapsack ===")
    
    # Test case
    values = [40, 50, 100, 95, 30]
    weights = [2, 3.14, 1.98, 5, 3]
    capacity = 10
    
    max_val = knapsack_branch_and_bound(capacity, weights, values)
    print(f"Items: Values={values}, Weights={weights}")
    print(f"Knapsack capacity: {capacity}")
    print(f"Maximum Profit (Branch & Bound): {max_val}")
