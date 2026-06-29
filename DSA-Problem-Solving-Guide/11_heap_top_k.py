"""
Pattern 11: Heap / Priority Queue (Top K)
==========================================
Use when: Need Top K largest/smallest, streaming median, or priority ordering.
Time:  O(n log k)   Space: O(k)

Problems: Kth Largest Element, Top K Frequent Elements,
          K Closest Points to Origin, Merge K Sorted Lists,
          Find Median from Data Stream, Task Scheduler
"""

import heapq
from collections import Counter


# ── Example 1: Kth Largest Element ───────────────────────────────────────────
def find_kth_largest(nums, k):
    """Kth largest element in unsorted array. O(n log k)"""
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


# ── Example 2: Top K Frequent Elements ──────────────────────────────────────
def top_k_frequent(nums, k):
    """K most frequent elements. O(n log k)"""
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)


# ── Example 3: K Closest Points to Origin ────────────────────────────────────
def k_closest(points, k):
    """K points closest to origin. O(n log k)"""
    # Use max-heap of size k (negate distance for max-heap behavior)
    heap = []
    for x, y in points:
        dist = -(x*x + y*y)
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]


# ── Example 4: Merge K Sorted Lists ─────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

def merge_k_sorted_lists(lists):
    """Merge k sorted linked lists into one. O(n log k)"""
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, node)
    dummy = ListNode()
    curr = dummy
    while heap:
        node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, node.next)
    return dummy.next


# ── Example 5: Find Median from Data Stream ───────────────────────────────────
class MedianFinder:
    """
    Two-heap approach: max-heap for lower half, min-heap for upper half.
    Add: O(log n)    Find Median: O(1)
    """
    def __init__(self):
        self.low = []   # max-heap (negate values)
        self.high = []  # min-heap

    def add_num(self, num):
        heapq.heappush(self.low, -num)
        # Balance: largest in low must be <= smallest in high
        if self.low and self.high and -self.low[0] > self.high[0]:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        # Keep sizes equal or low has one more
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0


if __name__ == "__main__":
    print("=== Heap / Top K Demo ===\n")

    print("Kth Largest k=2 in [3,2,1,5,6,4] →", find_kth_largest([3,2,1,5,6,4], 2))
    print("Top 2 Frequent in [1,1,1,2,2,3] →", top_k_frequent([1,1,1,2,2,3], 2))
    print("K=2 Closest points →", k_closest([[1,3],[-2,2],[5,8],[0,1]], 2))

    # Merge K lists: [1->4->5], [1->3->4], [2->6]
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    merged = merge_k_sorted_lists([l1, l2, l3])
    vals = []
    while merged:
        vals.append(merged.val)
        merged = merged.next
    print("Merge K Sorted Lists →", vals)

    mf = MedianFinder()
    for n in [1, 2, 3, 4, 5]:
        mf.add_num(n)
    print("Median of [1,2,3,4,5] →", mf.find_median())
