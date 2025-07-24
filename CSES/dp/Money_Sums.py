from functools import lru_cache
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

inf = float('inf')


n = II()
coins = LII()
from functools import lru_cache

sums = set()

@lru_cache(maxsize=None)
def go(i, su):
    if i == n:
        if su > 0:
            sums.add(su)
        return
    go(i + 1, su + coins[i])
    go(i + 1, su)

go(0, 0)
ans = sorted(sums)
print(len(ans))
print(' '.join(map(str, ans)))
