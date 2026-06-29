# 🧠 DSA Problem-Solving Cheat Sheet

> A complete reference guide to recognize patterns, pick the right algorithm, and think like a problem solver.
> Each pattern has a dedicated Python implementation file with multiple worked examples.

---

## 📁 File Index

| # | File | Pattern | When to Use |
|---|------|---------|-------------|
| 01 | [01_hashing_frequency.py](./01_hashing_frequency.py) | Hashing / Frequency Map | Count, lookup, anagram |
| 02 | [02_two_pointer.py](./02_two_pointer.py) | Two Pointer | Pair/triplet in sorted data |
| 03 | [03_sliding_window.py](./03_sliding_window.py) | Sliding Window | Contiguous subarray/substring |
| 04 | [04_prefix_sum.py](./04_prefix_sum.py) | Prefix Sum | Repeated range queries |
| 05 | [05_binary_search.py](./05_binary_search.py) | Binary Search | Fastest search in sorted/monotonic |
| 06 | [06_backtracking.py](./06_backtracking.py) | Backtracking | All possibilities / combinations |
| 07 | [07_dynamic_programming.py](./07_dynamic_programming.py) | Dynamic Programming | Overlapping subproblems |
| 08 | [08_monotonic_stack.py](./08_monotonic_stack.py) | Monotonic Stack | Nearest greater/smaller element |
| 09 | [09_bfs_dijkstra.py](./09_bfs_dijkstra.py) | BFS / Dijkstra | Shortest path in graphs |
| 10 | [10_union_find.py](./10_union_find.py) | Union Find | Connectivity / cycle detection |
| 11 | [11_heap_top_k.py](./11_heap_top_k.py) | Heap / Top K | K largest/smallest elements |
| 12 | [12_sorting_greedy.py](./12_sorting_greedy.py) | Sorting + Greedy | Ordering with local optimal choice |
| 13 | [13_tree_dp.py](./13_tree_dp.py) | Tree DP | DP problems on tree structures |

---

## 📥 STEP 1 — Identify the Input Type

Before anything else, ask: **what kind of data am I working with?**

| Input Type      | Common Techniques                                    |
|-----------------|------------------------------------------------------|
| **Array**       | Two Pointer, Sliding Window, Prefix Sum, Sorting     |
| **String**      | Hashing, Sliding Window, Two Pointer, Trie           |
| **Linked List** | Two Pointer (fast/slow), Reversal, Dummy node        |
| **Tree**        | DFS, BFS, Recursion, Tree DP                         |
| **Graph**       | BFS, DFS, Dijkstra, Union Find, Topological Sort     |

---

## 🔍 STEP 2 — Identify the Problem Pattern

Match your problem's **goal** to the right technique:

---

### 🔢 Need **count** or **frequency**?
> **→ Hashing / Frequency Map** — [`01_hashing_frequency.py`](./01_hashing_frequency.py)

Use a `dict` or `Counter` to track occurrences.

```python
from collections import Counter
freq = Counter(nums)
```

**Examples:** Anagram check, Two Sum, Most frequent element

---

### 👫 Need a **pair** with some condition?
> **→ Two Pointer** — [`02_two_pointer.py`](./02_two_pointer.py)

Use two indices (`left`, `right`) moving inward or in the same direction.

```python
left, right = 0, len(arr) - 1
while left < right:
    # process
    left += 1
    right -= 1
```

**Examples:** Two Sum (sorted), Container With Most Water, Palindrome check

---

### 📏 Need a **continuous subarray/substring** range?
> **→ Sliding Window** — [`03_sliding_window.py`](./03_sliding_window.py)

Maintain a window `[l, r]` and expand/shrink based on conditions.

```python
l = 0
for r in range(len(arr)):
    # expand window
    while <condition violated>:
        l += 1  # shrink window
```

**Examples:** Longest substring without repeating chars, Max sum subarray of size K

---

### 🔁 Need **repeated range queries** (sum, min, max)?
> **→ Prefix Sum** — [`04_prefix_sum.py`](./04_prefix_sum.py)

Precompute cumulative values to answer range queries in O(1).

```python
prefix = [0] * (len(arr) + 1)
for i, v in enumerate(arr):
    prefix[i+1] = prefix[i] + v
# Range sum [l, r]: prefix[r+1] - prefix[l]
```

**Examples:** Range sum query, Subarray sum equals K

---

### ⚡ Need the **fastest search** in sorted data?
> **→ Binary Search** — [`05_binary_search.py`](./05_binary_search.py)

Eliminate half the search space each step — O(log n).

```python
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: lo = mid + 1
    else: hi = mid - 1
```

**Examples:** Search in rotated array, Find peak element, Koko eating bananas

---

### 🌳 Need **all possibilities** / combinations / permutations?
> **→ Backtracking** — [`06_backtracking.py`](./06_backtracking.py)

Explore all paths recursively, and **undo** choices (backtrack) when a path fails.

```python
def backtrack(start, path):
    if <base case>:
        result.append(path[:])
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()  # undo
```

**Examples:** Subsets, Permutations, N-Queens, Sudoku Solver

---

### 📐 Need **optimal substructure** (overlapping subproblems)?
> **→ Dynamic Programming** — [`07_dynamic_programming.py`](./07_dynamic_programming.py)

Break the problem into smaller subproblems, store results to avoid recomputation.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i):
    if i == 0: return base_case
    return max(dp(i-1), dp(i-2)) + cost[i]
```

**Examples:** Fibonacci, Coin Change, Knapsack, Longest Common Subsequence

---

### 📊 Need **nearest greater or smaller** element?
> **→ Monotonic Stack** — [`08_monotonic_stack.py`](./08_monotonic_stack.py)

Maintain a stack that is always sorted (ascending or descending).

```python
stack = []
for i, val in enumerate(arr):
    while stack and arr[stack[-1]] < val:
        idx = stack.pop()
        # arr[idx]s next greater = val
    stack.append(i)
```

**Examples:** Next Greater Element, Largest Rectangle in Histogram, Daily Temperatures

---

### 🗺️ Need **shortest path** in a graph?
> **→ BFS / Dijkstra** — [`09_bfs_dijkstra.py`](./09_bfs_dijkstra.py)

```python
# BFS — unweighted shortest path
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

**Examples:** Word Ladder, Shortest path in grid, Network delay time

---

### 🔗 Need **connectivity** between nodes / components?
> **→ Union Find** — [`10_union_find.py`](./10_union_find.py)

```python
parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py: return False
    parent[py] = px
    return True
```

**Examples:** Number of Connected Components, Redundant Connection, Accounts Merge

---

### 🏆 Need **Top K** elements?
> **→ Heap (Priority Queue)** — [`11_heap_top_k.py`](./11_heap_top_k.py)

```python
import heapq

heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
# heap now contains K largest
```

**Examples:** Kth Largest Element, Top K Frequent Words, Merge K Sorted Lists

---

### 📋 Need **ordering** with a greedy choice?
> **→ Sorting + Greedy** — [`12_sorting_greedy.py`](./12_sorting_greedy.py)

```python
intervals.sort(key=lambda x: x[1])  # sort by end time
end = float('-inf')
count = 0
for start, finish in intervals:
    if start >= end:
        count += 1
        end = finish
```

**Examples:** Interval scheduling, Jump Game, Merge Intervals, Gas Station

---

### 🌲 Need **DP on a Tree** structure?
> **→ Tree DP** — [`13_tree_dp.py`](./13_tree_dp.py)

Post-order DFS — solve children first, combine at the parent.

```python
def dfs(node, parent):
    dp[node] = [0, node.weight]
    for child in node.neighbors:
        if child != parent:
            dfs(child, node)
            dp[node][0] += max(dp[child][0], dp[child][1])  # node excluded
            dp[node][1] += dp[child][0]                      # node included -> child excluded
```

**Examples:** Max Weight Independent Set, House Robber III, Diameter of Binary Tree

---

## 🤔 STEP 3 — The Problem-Solving Thinking Checklist

When stuck, go through these questions **in order**:

| # | Question                   | If Yes →                                     |
|---|----------------------------|----------------------------------------------|
| 1 | **Brute force?**           | Code it first to understand the problem      |
| 2 | **Can I cache?**           | Memoization / DP to eliminate redundant work |
| 3 | **Can I sort?**            | Unlocks Binary Search, Two Pointer, Greedy   |
| 4 | **Can I use map/set?**     | O(1) lookup → replace nested loops          |
| 5 | **Can I move pointers?**   | Two Pointer or Sliding Window                |
| 6 | **Can I preprocess?**      | Prefix Sum, lookup tables, adjacency lists   |
| 7 | **Is there recurrence?**   | DP — define state and transition             |
| 8 | **Can I greedily choose?** | Greedy — prove local = global optimum        |

---

## 🗂️ Quick Pattern Reference Card

```
INPUT TYPE
├── Array / String   → Two Pointer, Sliding Window, Prefix Sum, Hashing
├── Linked List      → Fast/Slow Pointer, Reversal
├── Tree             → DFS, BFS, Recursion, Tree DP
└── Graph            → BFS, DFS, Dijkstra, Union Find

PROBLEM GOAL
├── Count / Frequency       → Hashing             (01)
├── Pair with condition     → Two Pointer          (02)
├── Continuous subrange     → Sliding Window       (03)
├── Range query (repeated)  → Prefix Sum           (04)
├── Fastest search          → Binary Search        (05)
├── All possibilities       → Backtracking         (06)
├── Optimal substructure    → Dynamic Programming  (07)
├── Nearest greater/smaller → Monotonic Stack      (08)
├── Shortest path           → BFS / Dijkstra       (09)
├── Connectivity            → Union Find           (10)
├── Top K                   → Heap                 (11)
├── Ordering + Greedy       → Sort + Greedy        (12)
└── DP on tree              → Tree DP              (13)

STUCK? ASK IN ORDER:
1. Brute force?         → Understand the problem
2. Can I cache?         → DP / Memoization
3. Can I sort?          → Unlock Two Pointer / Binary Search
4. Can I use map/set?   → O(1) lookups
5. Can I move ptrs?     → Two Pointer / Sliding Window
6. Can I preprocess?    → Prefix Sum / Build graph
7. Is there recurrence? → Define DP state + transition
8. Can I greedily pick? → Greedy
```

---

## ⏱️ Time & Space Complexity Reference

| # | Algorithm          | Time Complexity          | Space Complexity    |
|---|--------------------|--------------------------|---------------------|
| 01 | Hashing           | O(n)                     | O(n)                |
| 02 | Two Pointer       | O(n)                     | O(1)                |
| 03 | Sliding Window    | O(n)                     | O(k)                |
| 04 | Prefix Sum        | O(n) build, O(1) query   | O(n)                |
| 05 | Binary Search     | O(log n)                 | O(1)                |
| 06 | Backtracking      | O(2^n) or O(n!)          | O(n)                |
| 07 | Dynamic Prog.     | O(n²) or O(n·m)          | O(n) or O(n·m)      |
| 08 | Monotonic Stack   | O(n)                     | O(n)                |
| 09 | BFS / DFS         | O(V + E)                 | O(V)                |
| 09 | Dijkstra          | O((V + E) log V)         | O(V)                |
| 10 | Union Find        | O(α(n)) ≈ O(1)           | O(n)                |
| 11 | Heap (Top K)      | O(n log k)               | O(k)                |
| 12 | Sorting + Greedy  | O(n log n)               | O(1) or O(n)        |
| 13 | Tree DP           | O(N)                     | O(N)                |

---

*"First make it work. Then make it fast. Then make it elegant."*
