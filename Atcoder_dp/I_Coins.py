I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(float, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
import sys
from functools import lru_cache
sys.setrecursionlimit(4*10**3)

inf = float('inf')

n = II()
probs = LII()
@lru_cache(None)
def go(i,cnt):
    if i==n:
        return int(cnt>n//2)
    take = round(go(i+1,cnt+1)*probs[i],10)
    ntake = round(go(i+1,cnt)*(1-probs[i]),10)
    round(take,10)
    round(ntake,10)
    return take+ntake
print(go(0,0))
    