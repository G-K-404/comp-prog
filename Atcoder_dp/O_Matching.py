I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

from functools import lru_cache

inf = float('inf')

n = II()
MOD = 10**9+7
a = [LII() for _ in range(n)]

@lru_cache(None)
def go(i,mask):
    if i==n:
        return 1 if mask==(1<<n)-1 else 0
    res = 0
    for j in range(n):
        if (not mask&1<<j ) and a[i][j]:
            res += go(i+1,mask|1<<j)
            res%=MOD
    return res%MOD
print(go(0,0))