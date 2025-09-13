from functools import lru_cache
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


n,x = MII()
wt = LII()
@lru_cache(None)
def go(curr_weight,mask):
    if mask == (1<<n)-1:
            return 1
    a = inf
    for j in range(n):
        if 1<<j & mask:
            continue
        else:
            if curr_weight+wt[j]<=x:
                a = min(a, go(curr_weight+wt[j], mask|1<<j))
            else:
                a = min(a,1+go(wt[j], mask|1<<j))
    return a

print(go(0,0)) 