from functools import lru_cache

I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

inf = float('inf')

def solve():
    se = set()
    for i in range(8):
        s = I()
        for j in range(8):
            if s[j] == '*':
                se.add((i, j))

    def check(row, col, queens):
        if (row, col) in se:
            return False
        for i in range(row):
            prow = i
            pcol = queens[i]
            if pcol == col or abs(col - pcol) == abs(i - row):
                return False
        return True

    @lru_cache(None)  # Use `lru_cache` instead of `cache`
    def go(level, queens):
        if level == 8:
            return 1
        ans = 0
        for i in range(8):
            if check(level, i, queens):
                new_queens = queens[:level] + (i,) + queens[level + 1:]
                ans += go(level + 1, new_queens)
        return ans

    # Initialize queens as a tuple of -1 (immutable state for caching)
    initial_queens = (-1,) * 8
    result = go(0, initial_queens)
    go.cache_clear()  # Clear the cache after solving
    print(result)

for _ in range(1):
    solve()
