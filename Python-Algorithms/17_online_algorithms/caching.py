"""
Online Caching Algorithms & Competitive Analysis
An online algorithm processes its input piece-by-piece in a serial fashion (without knowledge of the future).
This script implements standard online caching policies:
- FIFO (First-In, First-Out)
- LRU (Least Recently Used)
- LFU (Least Frequently Used)
And compares them to:
- Belady's MIN (Optimal Offline Cache): Evicts the page that will not be requested for the longest time in the future.
We analyze their empirical competitive ratio: Misses(Online) / Misses(MIN).
"""

import random

# --- Online Cache Strategies ---

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.misses = 0

    def request(self, page, future_requests=None):
        if page in self.cache:
            return True  # Hit
        self.misses += 1
        if len(self.cache) < self.capacity:
            self.cache.append(page)
        else:
            self.cache.pop(0)  # Evict first in
            self.cache.append(page)
        return False  # Miss

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.misses = 0

    def request(self, page, future_requests=None):
        if page in self.cache:
            # Move to end (most recently used)
            self.cache.remove(page)
            self.cache.append(page)
            return True
        self.misses += 1
        if len(self.cache) < self.capacity:
            self.cache.append(page)
        else:
            self.cache.pop(0)  # Evict least recently used (first in list)
            self.cache.append(page)
        return False

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # page -> frequency
        self.misses = 0

    def request(self, page, future_requests=None):
        if page in self.cache:
            self.cache[page] += 1
            return True
        self.misses += 1
        if len(self.cache) < self.capacity:
            self.cache[page] = 1
        else:
            # Find page with minimum frequency
            lfu_page = min(self.cache, key=self.cache.get)
            del self.cache[lfu_page]
            self.cache[page] = 1
        return False

# --- Offline Optimal Cache ---

class BeladyMinCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.misses = 0

    def request(self, page, future_requests, current_idx):
        """
        Optimal offline cache: requires knowledge of future_requests.
        """
        if page in self.cache:
            return True
        self.misses += 1
        if len(self.cache) < self.capacity:
            self.cache.append(page)
        else:
            # Find the page in cache whose next use is furthest in the future
            furthest_idx = -1
            page_to_evict = None
            
            for p in self.cache:
                # Find next occurrence of p in future_requests[current_idx + 1:]
                try:
                    next_use = future_requests.index(p, current_idx + 1)
                except ValueError:
                    next_use = float('inf')  # Not used again
                    
                if next_use > furthest_idx:
                    furthest_idx = next_use
                    page_to_evict = p
                    
            self.cache.remove(page_to_evict)
            self.cache.append(page)
        return False

if __name__ == "__main__":
    print("=== Online Caching & Competitive Ratio Demo ===")
    
    # Generate a request stream of pages
    random.seed(42)
    stream_len = 100
    num_distinct_pages = 10
    requests = [random.randint(1, num_distinct_pages) for _ in range(stream_len)]
    
    cache_capacity = 3
    print(f"Stream Length: {stream_len} | Distinct Pages: {num_distinct_pages} | Cache Capacity: {cache_capacity}")
    
    # Instantiate caches
    fifo = FIFOCache(cache_capacity)
    lru = LRUCache(cache_capacity)
    lfu = LFUCache(cache_capacity)
    min_opt = BeladyMinCache(cache_capacity)
    
    # Run simulation
    for i, page in enumerate(requests):
        fifo.request(page)
        lru.request(page)
        lfu.request(page)
        # MIN requires remaining stream starting from current index
        min_opt.request(page, requests, i)
        
    print("\nSimulation Results (Cache Misses):")
    print(f"  - Belady's MIN (Optimal Offline): {min_opt.misses}")
    print(f"  - FIFO (Online):                 {fifo.misses} | Empirical Competitive Ratio: {fifo.misses / min_opt.misses:.3f}")
    print(f"  - LRU (Online):                  {lru.misses} | Empirical Competitive Ratio: {lru.misses / min_opt.misses:.3f}")
    print(f"  - LFU (Online):                  {lfu.misses} | Empirical Competitive Ratio: {lfu.misses / min_opt.misses:.3f}")
    
    print("\nNote: Theoretical worst-case competitive ratio for FIFO and LRU is k (cache capacity = 3).")
