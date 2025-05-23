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
coins.sort()
sums = set([])
lis = []
@lru_cache(None)
def go(i, su):
    if i == n:
        if su != 0:
            if su not in sums:
                lis.append(su)
            sums.add(su)
        return
    go(i + 1, su + coins[i])
    go(i + 1, su)

go(0, 0)
go.cache_clear()
print(len(sums))
print(" ".join(map(str, sorted(lis))))