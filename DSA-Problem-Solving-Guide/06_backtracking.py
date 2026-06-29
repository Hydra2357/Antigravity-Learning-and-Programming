"""
Pattern 06: Backtracking
=========================
Use when: Need all possibilities — combinations, permutations, or placements.
Time:  O(2^n) or O(n!)   Space: O(n) recursion depth

Problems: Subsets, Permutations, Combinations, N-Queens, Sudoku Solver,
          Word Search, Letter Combinations of Phone Number
"""


# ── Example 1: All Subsets ───────────────────────────────────────────────────
def subsets(nums):
    """Generate all subsets (power set). O(2^n)"""
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


# ── Example 2: All Permutations ──────────────────────────────────────────────
def permutations(nums):
    """Generate all unique permutations. O(n!)"""
    result = []
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return result


# ── Example 3: Combination Sum ───────────────────────────────────────────────
def combination_sum(candidates, target):
    """Find all combinations that sum to target (can reuse elements). O(2^t)"""
    result = []
    candidates.sort()
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    backtrack(0, [], target)
    return result


# ── Example 4: N-Queens ──────────────────────────────────────────────────────
def solve_n_queens(n):
    """Return all solutions for the N-Queens problem. O(n!)"""
    result = []
    cols = set()
    pos_diag = set()   # r + c
    neg_diag = set()   # r - c

    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row][col] = "Q"
            backtrack(row + 1)
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            board[row][col] = "."

    backtrack(0)
    return result


# ── Example 5: Word Search in Grid ───────────────────────────────────────────
def word_search(board, word):
    """Check if word exists in grid (adjacent cells). O(m*n * 4^L)"""
    rows, cols = len(board), len(board[0])

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        temp, board[r][c] = board[r][c], "#"
        found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    print("=== Backtracking Demo ===\n")

    print("Subsets [1,2,3] →", subsets([1, 2, 3]))
    print("Permutations [1,2,3] →", permutations([1, 2, 3]))
    print("Combination Sum [2,3,6,7] target=7 →", combination_sum([2, 3, 6, 7], 7))
    print("N-Queens n=4 solutions →", len(solve_n_queens(4)), "solutions")
    grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print("Word Search 'ABCCED' →", word_search(grid, "ABCCED"))
