from collections import deque
from functools import lru_cache
import sys
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

sys.setrecursionlimit(100000)

inf = float('inf')



n,m = MII()
g = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = MII()
    g[x].append(y)

@lru_cache(None)
def dfs(node):
    if not g[node]:
        return 0
    a = 0
    for x in g[node]:
        a = max(a,1+dfs(x))
    return a
    
    

ans = 0
for x in range(1,n+1):
    ans=max(ans,dfs(x))

print(ans)

