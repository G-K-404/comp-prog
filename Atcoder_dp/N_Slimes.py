I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
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