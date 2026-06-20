"""
Push-Relabel Maximum Flow Algorithm
Computes the maximum flow in a flow network.
Maintains a 'preflow' and uses 'push' and 'relabel' operations to adjust flow heights.
Active vertices (excess > 0, height < V) are maintained in a queue.
Time Complexity: O(V^3) or O(V^2 * E) depending on active vertex selection (FIFO).
Space Complexity: O(V + E)
"""

from collections import deque

class PushRelabel:
    def __init__(self, size):
        self.size = size
        self.capacity = [[0] * size for _ in range(size)]
        self.flow = [[0] * size for _ in range(size)]
        self.height = [0] * size
        self.excess = [0] * size

    def add_edge(self, u, v, cap):
        self.capacity[u][v] = cap

    def _push(self, u, v):
        """Pushes excess flow from u to v if possible."""
        send = min(self.excess[u], self.capacity[u][v] - self.flow[u][v])
        self.flow[u][v] += send
        self.flow[v][u] -= send
        self.excess[u] -= send
        self.excess[v] += send

    def _relabel(self, u):
        """Increases height of active node u so it can push flow."""
        min_height = float('inf')
        for v in range(self.size):
            if self.capacity[u][v] - self.flow[u][v] > 0:
                min_height = min(min_height, self.height[v])
        if min_height != float('inf'):
            self.height[u] = min_height + 1

    def max_flow(self, source, sink):
        # Step 1: Initialize height and excess
        self.height[source] = self.size
        self.excess[source] = float('inf')
        
        # Push initial preflow from source to neighbors
        for v in range(self.size):
            if self.capacity[source][v] > 0:
                self._push(source, v)
                
        # Queue to track active vertices (vertices with excess > 0, excluding source and sink)
        active_queue = deque()
        in_queue = [False] * self.size
        
        for i in range(self.size):
            if i != source and i != sink and self.excess[i] > 0:
                active_queue.append(i)
                in_queue[i] = True
                
        # Step 2: Push and Relabel loop
        while active_queue:
            u = active_queue.popleft()
            in_queue[u] = False
            
            # Try to push flow from u to its neighbors
            for v in range(self.size):
                if self.excess[u] == 0:
                    break
                    
                # Push condition: excess > 0, residual capacity > 0, height[u] == height[v] + 1
                if self.capacity[u][v] - self.flow[u][v] > 0 and self.height[u] == self.height[v] + 1:
                    self._push(u, v)
                    # Add newly active vertex v to queue
                    if v != source and v != sink and self.excess[v] > 0 and not in_queue[v]:
                        active_queue.append(v)
                        in_queue[v] = True
                        
            # If u is still active (excess > 0), relabel it and put it back in queue
            if self.excess[u] > 0:
                self._relabel(u)
                active_queue.append(u)
                in_queue[u] = True
                
        # The max flow is the total flow leaving source (or arriving at sink)
        return sum(self.flow[source])

if __name__ == "__main__":
    print("=== Push-Relabel Max Flow Demo ===")
    
    # 6 vertices flow network
    pr = PushRelabel(6)
    pr.add_edge(0, 1, 16)
    pr.add_edge(0, 2, 13)
    pr.add_edge(1, 2, 10)
    pr.add_edge(1, 3, 12)
    pr.add_edge(2, 1, 4)
    pr.add_edge(2, 4, 14)
    pr.add_edge(3, 2, 9)
    pr.add_edge(3, 5, 20)
    pr.add_edge(4, 3, 7)
    pr.add_edge(4, 5, 4)
    
    source = 0
    sink = 5
    max_flow = pr.max_flow(source, sink)
    print(f"Maximum Flow (Push-Relabel): {max_flow} (Expected: 23)")
