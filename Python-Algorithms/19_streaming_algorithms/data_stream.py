"""
Data Streaming Algorithms Demo
Streaming algorithms process data that arrives in a continuous stream, using limited memory (often sublinear/logarithmic space).
Includes:
1. Reservoir Sampling: Randomly samples k elements from a stream of unknown/infinite length.
   - Each element in the stream has an equal k/N probability of being chosen.
2. Count-Min Sketch: Sublinear space frequency table.
   - Estimates occurrences of items using multiple hash functions.
3. HyperLogLog Cardinality Estimator: Estimates count of unique elements.
   - Uses hash prefixes (finding max trailing/leading zeros) to approximate distinct elements.
"""

import random
import hashlib
import math

# --- 1. Reservoir Sampling ---
def reservoir_sampling(stream, k):
    """
    Selects k items from stream.
    Time Complexity: O(N)
    Space Complexity: O(k)
    """
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            # Pick a random index from 0 to i
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir

# --- 2. Count-Min Sketch ---
class CountMinSketch:
    def __init__(self, width, depth):
        """
        width (w): columns in table (reduces error amount)
        depth (d): rows (hash functions) (increases confidence probability)
        """
        self.w = width
        self.d = depth
        self.table = [[0] * width for _ in range(depth)]

    def _hash(self, item, i):
        """Simple hash function parameterized by index i."""
        hash_str = f"{item}_{i}".encode('utf-8')
        val = int(hashlib.md5(hash_str).hexdigest(), 16)
        return val % self.w

    def add(self, item, count=1):
        for i in range(self.d):
            h_idx = self._hash(item, i)
            self.table[i][h_idx] += count

    def estimate(self, item):
        """Returns the estimated frequency (overestimate bound)."""
        estimates = []
        for i in range(self.d):
            h_idx = self._hash(item, i)
            estimates.append(self.table[i][h_idx])
        return min(estimates)  # Frequency is bound by minimum count

# --- 3. HyperLogLog Cardinality Estimator ---
class HyperLogLog:
    def __init__(self, p=6):
        """
        p: precision parameter (number of registers = 2^p)
        """
        self.p = p
        self.m = 1 << p  # number of registers
        self.registers = [0] * self.m
        
        # Alpha constant calculation for correction
        if self.m == 16:
            self.alpha = 0.673
        elif self.m == 32:
            self.alpha = 0.697
        elif self.m == 64:
            self.alpha = 0.709
        else:
            self.alpha = 0.7213 / (1.0 + 1.079 / self.m)

    def add(self, item):
        hash_str = str(item).encode('utf-8')
        h = int(hashlib.sha1(hash_str).hexdigest(), 16)
        
        # Use first p bits to select register index
        idx = h & (self.m - 1)
        # Remaining bits are used to find rank (number of leading zeros + 1)
        w = h >> self.p
        
        # Count leading zeros of w in binary form
        zeros = 0
        if w > 0:
            binary_w = bin(w)[2:]
            zeros = len(binary_w) - len(binary_w.rstrip('0'))
        rank = zeros + 1
        
        self.registers[idx] = max(self.registers[idx], rank)

    def estimate_cardinality(self):
        """Estimates count of distinct items using harmonic mean of registers."""
        # Harmonic mean calculation
        sum_val = sum(2.0 ** -val for val in self.registers)
        estimate = self.alpha * (self.m ** 2) / sum_val
        
        # Small range correction
        if estimate <= 2.5 * self.m:
            zeros = self.registers.count(0)
            if zeros > 0:
                estimate = self.m * math.log(self.m / zeros)
                
        return int(estimate)

if __name__ == "__main__":
    print("=== Data Streaming Algorithms Demo ===")
    
    # Generate mock stream of items
    stream_size = 1000
    mock_stream = [f"user_{random.randint(1, 100)}" for _ in range(stream_size)]
    
    # 1. Reservoir Sampling
    print("\n1. Reservoir Sampling (k=5):")
    sample = reservoir_sampling(mock_stream, 5)
    print(f"  Random sample of 5 items: {sample}")
    
    # 2. Count-Min Sketch
    print("\n2. Count-Min Sketch Frequency Estimator:")
    cms = CountMinSketch(width=50, depth=4)
    # Count actual frequencies to compare
    actual_freqs = {}
    for item in mock_stream:
        cms.add(item)
        actual_freqs[item] = actual_freqs.get(item, 0) + 1
        
    test_items = ["user_10", "user_50", "user_99", "non_existent"]
    for item in test_items:
        act = actual_freqs.get(item, 0)
        est = cms.estimate(item)
        print(f"  Item: {item:<12} | Actual: {act:3d} | Estimated: {est:3d} (diff: {est - act:2d})")
        
    # 3. HyperLogLog
    print("\n3. HyperLogLog Cardinality Estimator:")
    hll = HyperLogLog(p=6)  # 64 registers
    unique_items = set()
    for item in mock_stream:
        hll.add(item)
        unique_items.add(item)
        
    actual_distinct = len(unique_items)
    est_distinct = hll.estimate_cardinality()
    error_pct = abs(est_distinct - actual_distinct) / actual_distinct * 100
    print(f"  Actual Distinct Elements:    {actual_distinct}")
    print(f"  HyperLogLog Estimated:       {est_distinct}")
    print(f"  Estimation Error Percentage: {error_pct:.2f}%")
