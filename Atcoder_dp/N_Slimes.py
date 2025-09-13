import sys
sys.setrecursionlimit(10000)

I = lambda: input()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

inf = float('inf')

n = II()
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
