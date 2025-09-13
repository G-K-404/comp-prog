I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
inf = float('inf')


e = II()
edges = []
for _ in range(e-1):
    edges.append(LII())
adj = defaultdict(list)
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
diam = -1
def dfs(u, p, depth):
    farthest = (depth, u)
    for v in adj[u]:
        if v != p:
            farthest = max(farthest, dfs(v, u, depth + 1))
    return farthest
a = dfs(1,-1,0)
dis,node = a
b = dfs(node,-1,0)
ans,_ = b
print(ans)