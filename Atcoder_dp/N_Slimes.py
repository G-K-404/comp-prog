<<<<<<< HEAD
import sys
sys.setrecursionlimit(10000)

I = lambda: input()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))
=======
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

>>>>>>> 2f6612852ebc014714fb29b63627e467478aa78c

inf = float('inf')

n = II()
<<<<<<< HEAD
slimes = LII()

# Compute prefix sums
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + slimes[i]

def get_sum(i, j):
    return pref[j + 1] - pref[i]

dp = [[-1] * n for _ in range(n)]

def rec(i, j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    min_cost = inf
    for k in range(i, j):
        cost = rec(i, k) + rec(k + 1, j) + get_sum(i, j)
        if cost < min_cost:
            min_cost = cost

    dp[i][j] = min_cost
    return min_cost

print(rec(0, n - 1))
=======
s = LII()

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + s[i]

def get_sum(l, r):
    return prefix[r + 1] - prefix[l]

from functools import lru_cache

@lru_cache(None)
def go(l, r):
    if l == r:
        return 0
    res = inf
    for k in range(l, r):
        res = min(res, go(l, k) + go(k + 1, r) + get_sum(l, r))
    return res

print(go(0, n - 1))
>>>>>>> 2f6612852ebc014714fb29b63627e467478aa78c
