"""
Pattern 12: Sorting + Greedy
==============================
Use when: Optimal solution can be built by always making the locally best choice.
Sort first to establish order, then greedily choose.
Time:  O(n log n)   Space: O(1) or O(n)

Problems: Interval Scheduling, Jump Game, Merge Intervals,
          Gas Station, Assign Cookies, Task Scheduler, Candy
"""


# ── Example 1: Merge Intervals ───────────────────────────────────────────────
def merge_intervals(intervals):
    """Merge all overlapping intervals. O(n log n)"""
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# ── Example 2: Non-overlapping Intervals (min removals) ─────────────────────
def erase_overlap_intervals(intervals):
    """Min number of intervals to remove so rest don't overlap. O(n log n)"""
    intervals.sort(key=lambda x: x[1])   # sort by end time
    end = float("-inf")
    count = 0
    for start, finish in intervals:
        if start >= end:
            end = finish
        else:
            count += 1   # remove this interval
    return count


# ── Example 3: Jump Game ─────────────────────────────────────────────────────
def can_jump(nums):
    """Can you reach the last index? O(n)"""
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True


# ── Example 4: Jump Game II (min jumps) ─────────────────────────────────────
def jump_game_ii(nums):
    """Minimum jumps to reach the last index. O(n)"""
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


# ── Example 5: Gas Station ───────────────────────────────────────────────────
def can_complete_circuit(gas, cost):
    """Find starting gas station to complete circuit. O(n)"""
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start


# ── Example 6: Assign Cookies ────────────────────────────────────────────────
def find_content_children(greed, size):
    """Max children satisfied. greed[i] = min cookie size child i needs. O(n log n)"""
    greed.sort()
    size.sort()
    child = cookie = 0
    while child < len(greed) and cookie < len(size):
        if size[cookie] >= greed[child]:
            child += 1
        cookie += 1
    return child


# ── Example 7: Candy Distribution ────────────────────────────────────────────
def candy(ratings):
    """Min candies: each child >= 1, higher-rated neighbor gets more. O(n)"""
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)


if __name__ == "__main__":
    print("=== Sorting + Greedy Demo ===\n")

    print("Merge Intervals [[1,3],[2,6],[8,10],[15,18]] →",
          merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print("Erase Overlap [[1,2],[2,3],[3,4],[1,3]] →",
          erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))
    print("Can Jump [2,3,1,1,4] →", can_jump([2,3,1,1,4]))
    print("Can Jump [3,2,1,0,4] →", can_jump([3,2,1,0,4]))
    print("Min Jumps [2,3,1,1,4] →", jump_game_ii([2,3,1,1,4]))
    print("Gas Station gas=[1,2,3,4,5] cost=[3,4,5,1,2] →",
          can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))
    print("Assign Cookies greed=[1,2,3] size=[1,1] →",
          find_content_children([1,2,3], [1,1]))
    print("Candy ratings=[1,0,2] →", candy([1,0,2]))
