"""
Greedy Paradigm Demo
Includes:
1. Fractional Knapsack: Greedy choice based on highest value-to-weight ratio. O(N log N) time, O(1) extra space.
2. Activity Selection Problem: Greedy choice based on earliest finish time. O(N log N) time, O(1) extra space.
"""

class Item:
    def __init__(self, value, weight, name):
        self.value = value
        self.weight = weight
        self.name = name
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    """
    Solves Fractional Knapsack problem using a Greedy approach.
    """
    # Greedy choice: Sort items by value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0
    knapsack_contents = []
    
    for item in sorted_items:
        if capacity <= 0:
            break
            
        if item.weight <= capacity:
            # Take whole item
            capacity -= item.weight
            total_value += item.value
            knapsack_contents.append((item.name, 1.0, item.value))
        else:
            # Take fraction of item
            fraction = capacity / item.weight
            val_taken = item.value * fraction
            total_value += val_taken
            knapsack_contents.append((item.name, fraction, val_taken))
            capacity = 0  # Knapsack is full
            
    return total_value, knapsack_contents

class Activity:
    def __init__(self, start, finish, name):
        self.start = start
        self.finish = finish
        self.name = name

def activity_selection(activities):
    """
    Selects maximum set of mutually compatible activities.
    """
    if not activities:
        return []
        
    # Greedy choice: Sort activities by finish time
    sorted_activities = sorted(activities, key=lambda x: x.finish)
    
    selected = [sorted_activities[0]]
    last_finish_time = sorted_activities[0].finish
    
    for act in sorted_activities[1:]:
        if act.start >= last_finish_time:
            selected.append(act)
            last_finish_time = act.finish
            
    return selected

if __name__ == "__main__":
    print("=== Greedy Paradigm Demo ===")
    
    # 1. Fractional Knapsack Test
    items = [
        Item(60, 10, "Gold Dust"),
        Item(100, 20, "Silver Ore"),
        Item(120, 30, "Copper Bars")
    ]
    capacity = 50
    max_val, contents = fractional_knapsack(capacity, items)
    print(f"\nFractional Knapsack (Capacity {capacity}):")
    print(f"Total Value: {max_val}")
    print("Items taken:")
    for name, frac, val in contents:
        print(f"  - {name}: {frac * 100:.1f}% (Value: {val:.2f})")
        
    # 2. Activity Selection Test
    activities = [
        Activity(1, 4, "A1"),
        Activity(3, 5, "A2"),
        Activity(0, 6, "A3"),
        Activity(5, 7, "A4"),
        Activity(3, 9, "A5"),
        Activity(5, 9, "A6"),
        Activity(6, 10, "A7"),
        Activity(8, 11, "A8"),
        Activity(8, 12, "A9"),
        Activity(2, 14, "A10"),
        Activity(12, 16, "A11")
    ]
    selected_activities = activity_selection(activities)
    print(f"\nActivity Selection:")
    print("Selected compatible activities (sorted by finish time):")
    for act in selected_activities:
        print(f"  - {act.name} (Start: {act.start}, Finish: {act.finish})")
