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
edges = [LII() for _ in range(n-1)]

adj = [[] for _ in range(n+1)]
for x in edges:
    u,v = x
    adj[u].append(v)
    adj[v].append(u)
children = [[] for _ in range(n+1)]
def dfs(node, parent):
    for x in adj[node]:
        if x!=parent:
            children[node].append(x)
            dfs(x,node)
dfs(1,0)


MOD = (10**9)+7
@lru_cache(None)
def go(take, node):
    if not children[node]:
        return 1
    res = 1
    if take:
        for x in children[node]:
            res = res * go(0, x) % MOD
    else:
        for x in children[node]:
            res = res * (go(0, x) + go(1, x)) % MOD
    return res
print(go(0,1)+go(1,1))