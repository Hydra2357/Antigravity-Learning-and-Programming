"""
Pattern 09: BFS / Dijkstra
===========================
Use when: Shortest path in unweighted (BFS) or weighted (Dijkstra) graphs.
BFS Time:      O(V + E)          Space: O(V)
Dijkstra Time: O((V+E) log V)   Space: O(V)

Problems: Word Ladder, Shortest Path in Grid, Network Delay Time,
          Rotting Oranges, Walls and Gates, Cheapest Flights Within K Stops
"""

from collections import deque
import heapq


# ── Example 1: BFS Shortest Path (unweighted graph) ─────────────────────────
def bfs_shortest_path(graph, start, end):
    """Shortest path between start and end in an unweighted graph."""
    if start == end:
        return [start]
    visited = {start}
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == end:
                    return new_path
                visited.add(neighbor)
                queue.append(new_path)
    return []   # no path


# ── Example 2: BFS Level Order (grid shortest path) ─────────────────────────
def shortest_path_grid(grid):
    """Shortest path from top-left to bottom-right in a binary grid. O(m*n)"""
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    queue = deque([(0, 0, 1)])   # (row, col, distance)
    visited = {(0, 0)}
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while queue:
        r, c, dist = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1


# ── Example 3: Rotting Oranges (Multi-source BFS) ───────────────────────────
def oranges_rotting(grid):
    """Minutes until all oranges rot. -1 if impossible. O(m*n)"""
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while queue:
        r, c, time = queue.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                minutes = time + 1
                queue.append((nr, nc, time + 1))
    return minutes if fresh == 0 else -1


# ── Example 4: Dijkstra — Network Delay Time ─────────────────────────────────
def network_delay_time(times, n, k):
    """Min time for signal from k to reach all nodes. O((V+E) log V)"""
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]   # (cost, node)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    max_dist = max(dist.values())
    return max_dist if max_dist < float("inf") else -1


# ── Example 5: Word Ladder (BFS on implicit graph) ───────────────────────────
def word_ladder(begin_word, end_word, word_list):
    """Min transformations from begin to end (change 1 letter). O(n*m^2)"""
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    return 0


if __name__ == "__main__":
    print("=== BFS / Dijkstra Demo ===\n")

    graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [6], 5: [6], 6: []}
    print("BFS Shortest Path 1→6 →", bfs_shortest_path(graph, 1, 6))

    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print("Grid Shortest Path →", shortest_path_grid(grid))

    oranges = [[2,1,1],[1,1,0],[0,1,1]]
    print("Rotting Oranges →", oranges_rotting(oranges))

    times = [[2,1,1],[2,3,1],[3,4,1]]
    print("Network Delay n=4, k=2 →", network_delay_time(times, 4, 2))

    words = ["hot","dot","dog","lot","log","cog"]
    print("Word Ladder hit→cog →", word_ladder("hit", "cog", words))
