# Programming Library

This repository contains a comprehensive suite of algorithmic reference implementations in Python, featuring performance benchmarks, specialized advanced data structures, and optimization paradigms.

---

## 📂 Repository Structure

The codebase is organized into two primary libraries:
1. **[Python-Algorithms](./Python-Algorithms)**: A structured collection of advanced algorithms across 25 distinct mathematical and computer science areas.
2. **[SORTING.py](./SORTING.py)**: A standalone educational benchmarking suite implementing 13 sorting and 6 searching algorithms.

---

## 📚 Advanced Python Algorithms Library (`Python-Algorithms`)

This subdirectory contains fully self-contained Python files representing standard and advanced algorithmic concepts. Each file is thoroughly documented with asymptotic time/space complexities and contains an executable demo inside its `if __name__ == "__main__":` block.

### 25 Algorithmic Areas Included

| Folder / Area | Included Topics / Algorithms |
| :--- | :--- |
| **01. Mathematical Analysis** | Asymptotic profiling, Recurrence Master Theorem solver, Amortized array resize, Probabilistic Secretary/Birthday paradox simulations |
| **02. Design Paradigms** | Divide & Conquer (Merge Sort/Binary Search), Greedy, DP, Backtracking (N-Queens), Branch & Bound (0/1 Knapsack) |
| **03. Randomized Algorithms** | Randomized QuickSort, Randomized Selection (QuickSelect), Monte Carlo Pi, Las Vegas N-Queens |
| **04. Advanced Trees** | AVL Trees, Red-Black Trees, B-Trees, Splay Trees, Link-Cut Trees (dynamic forest connectivity) |
| **05. Advanced Heaps** | Binomial Heaps, Fibonacci Heaps (mergeable heaps) |
| **06. Disjoint Structures** | Disjoint Set Union (DSU / Union-Find) with Rank & Path Compression |
| **07. Sorting & Selection** | Median of Medians (deterministic linear-time selection), Randomized sorting comparison |
| **08. Graph Algorithms** | BFS, DFS, Topological Sort (Kahn's & DFS), Strongly Connected Components (Tarjan & Kosaraju), MST (Kruskal & Prim) |
| **09. Shortest Path** | Dijkstra SSSP, Bellman-Ford (with negative cycle detection), Floyd-Warshall APSP |
| **10. Network Flow** | Ford-Fulkerson (DFS-based), Edmonds-Karp (BFS-based), Push-Relabel (FIFO active queue) |
| **11. Matching Problems** | Hopcroft-Karp Bipartite Matching, Edmonds' Blossom Algorithm (general matching), MV Phase-based matching |
| **12. Advanced DP** | Longest Increasing Subsequence ($O(N \log N)$), Space-optimized Knapsack, Matrix Chain Multiplication, Tree DP |
| **13. String Algorithms** | Knuth-Morris-Pratt (KMP), Rabin-Karp (rolling hash), Trie, Suffix Array & LCP Array (Kasai) |
| **14. Computational Geometry** | Graham Scan & Jarvis March (Convex Hull), Sweep Line Closest Pair, Divide & Conquer Closest Pair |
| **15. Complexity Theory** | NP verifier vs NP-hard exponential solver demonstration using Subset Sum |
| **16. Approximation Algorithms** | Greedy Set Cover, 2-approx Vertex Cover, 2-approx Metric TSP, Christofides 1.5-approx TSP |
| **17. Online Algorithms** | LRU/FIFO/LFU caching vs Optimal Offline MIN, Ski Rental randomized/deterministic competitive ratio |
| **18. Parallel Algorithms** | PRAM Parallel Reduction & Blelloch prefix sum (Scan), Parallel Merge Sort & Brent's Theorem |
| **19. Streaming Algorithms** | Reservoir Sampling, Count-Min Sketch frequency estimator, HyperLogLog cardinality estimator |
| **20. Massive Data Algorithms** | Sublinear Sortedness Tester, Sublinear Connected Components count estimator |
| **21. Parameterized Algorithms** | Fixed-Parameter Tractable (FPT) Vertex Cover ($O(2^k \cdot V + E)$) |
| **22. Algorithmic Game Theory** | Vickrey Auction (second-price sealed-bid), Gale-Shapley Stable Marriage |
| **23. Linear Programming** | Primal Simplex tableau solver, Primal-to-Dual LP converter (Strong Duality verifier) |
| **24. Advanced Graph Topics** | Karger's Randomized Min-Cut, Local Search Max-Cut, Backtracking Max Independent Set, Welsh-Powell Coloring |
| **25. Specialized Topics** | Radix-2 Cooley-Tukey FFT & polynomial multiplication, Strassen's matrix multiplication |

### Running the Verification Suite
All algorithms can be verified at once by running the central test script:
```bash
cd Python-Algorithms
python verify_all.py
```

---

## 📊 Sorting and Searching Benchmarking Library (`SORTING.py`)

A comprehensive, educational, and performance-benchmarked library implementing standard sorting and searching algorithms.

### Run the Benchmarks
```bash
python SORTING.py
```

### 1. Sorting Algorithms Complexity
| Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Stable? | In-Place? | Category |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes | Comparison |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Yes | Comparison |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes | Comparison |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No | Comparison |
| **Quick Sort (Out-of-place)** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(n)$ | No | No | Comparison |
| **Quick Sort (In-place)** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No | Yes | Comparison |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No | Yes | Comparison |
| **Shell Sort** | $O(n \log n)$ | $O(n^{1.5})$ | $O(n^2)$ | $O(1)$ | No | Yes | Comparison |
| **Counting Sort** | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | Yes | No | Non-Comparison |
| **Radix Sort** | $O(d(n + k))$ | $O(d(n + k))$ | $O(d(n + k))$ | $O(n + k)$ | Yes | No | Non-Comparison |
| **Bucket Sort** | $O(n + k)$ | $O(n + k)$ | $O(n^2)$ | $O(n + k)$ | Yes | No | Distribution |
| **Tree Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(n)$ | Yes | No | Tree-based |
| **TimSort** | $O(n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No | Hybrid |
| **Block Sort** | $O(n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(\sqrt{n})$ | Yes | Yes | Hybrid |

*Note: $k$ represents the range of values (min to max), $d$ represents the number of digits, and $n$ represents the number of elements.*

### 2. Searching Algorithms Complexity
| Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Requires Sorted? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | No |
| **Binary Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | Yes |
| **Ternary Search** | $O(1)$ | $O(\log_3 n)$ | $O(\log_3 n)$ | $O(1)$ | Yes |
| **Jump Search** | $O(1)$ | $O(\sqrt{n})$ | $O(\sqrt{n})$ | $O(1)$ | Yes |
| **Interpolation Search**| $O(1)$ | $O(\log(\log n))$ | $O(n)$ | $O(1)$ | Yes (Uniformly Distributed) |
| **Exponential Search** | $O(1)$ | $O(\log i)$ | $O(\log n)$ | $O(1)$ | Yes |

*Note: $i$ is the target's index.*

---

## 🔍 Detailed Explanations: Sorting and Searching

### I. Sorting Algorithms

#### 1. Bubble Sort
Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. An optimization flag (`swapped`) terminates execution early if no swaps occur during a pass, making it $O(n)$ for sorted arrays.

#### 2. Selection Sort
Divides the input list into two parts: a sorted sublist built up from left to right, and an unsorted sublist. It repeatedly finds the smallest element in the unsorted sublist and swaps it into the leftmost unsorted position.

#### 3. Insertion Sort
Builds the final sorted list one element at a time by consuming one input element per repetition and placing it in its correct position relative to the already sorted portion. Highly efficient for small datasets or nearly sorted arrays.

#### 4. Merge Sort
A classic divide-and-conquer algorithm. It recursively divides the array into halves, sorts them, and then merges them back together. It guarantees stable $O(n \log n)$ performance but requires $O(n)$ extra helper space.

#### 5. Quick Sort (In-Place & Out-of-Place)
Picks an element as a pivot and partitions the array around it.
- **Out-of-place**: Intuitive Python implementation creating new list filters for elements smaller, equal, and larger than the pivot.
- **In-place**: Uses **Hoare's partitioning scheme** to swap elements relative to a midpoint pivot directly in memory, optimizing space to recursion stack depth $O(\log n)$.

#### 6. Heap Sort
Converts the array into a Max-Heap structure, then repeatedly extracts the maximum element from the root and restores the heap property. Operates strictly in-place with guaranteed $O(n \log n)$ complexity.

#### 7. Shell Sort
An optimization of Insertion Sort that allows the swap of far-apart elements. By using a gap sequence (halving the gap on each iteration), elements move quickly towards their final sorted positions.

#### 8. Counting Sort
A non-comparison sort that tracks the frequencies of each unique value in a counting array, computing each value's final output index. Exceptionally fast ($O(n+k)$) for dense integer datasets.

#### 9. Radix Sort
Sorts numbers digit-by-digit (starting from the least significant digit to the most significant digit) using Counting Sort as a stable sorting sub-routine. Features native support for negative values by shifting offsets.

#### 10. Bucket Sort
Distributes elements into multiple buckets, sorts each bucket individually using Insertion Sort, and concatenates the results. Expects floating-point numbers distributed uniformly in the range $[0, 1)$.

#### 11. Tree Sort
Builds a Binary Search Tree (BST) from the inputs. Traverses the BST in-order to write sorted elements back to the list. Duplicate values are handled using node counters to retain stability.

#### 12. TimSort
Python's standard sorting method. It partitions the array into chunks ("runs"), sorts individual runs using Insertion Sort, and merges adjacent runs using Merge Sort. 

#### 13. Block Sort
A stable hybrid sorting algorithm that groups elements into blocks of size $\sqrt{n}$, sorts them, and merges them using block rotations and index permutations.

---

### II. Searching Algorithms

#### 1. Linear Search
Checks every element of the array sequentially from start to end until a match is found.

#### 2. Binary Search (Iterative & Recursive)
Quickly searches a sorted array by comparing the target with the middle element. It halves the search space at each iteration.

#### 3. Ternary Search (Iterative & Recursive)
Divides the search space into three parts using two midpoints (`mid1`, `mid2`). Reduces the search space to $1/3$ each step.

#### 4. Jump Search
Combines linear search with skipping blocks. It jumps ahead by fixed steps of $\sqrt{n}$ until it finds a block containing the target, then executes a linear search backward.

#### 5. Interpolation Search
An optimized search for sorted, uniformly distributed datasets. Instead of blindly choosing the middle index, it estimates the target's location using a linear interpolation formula.

#### 6. Exponential Search
Quickly finds the range in which the target must reside by exponentially doubling indices (1, 2, 4, 8, ...). Once the range is found, it performs a binary search within that subset.
