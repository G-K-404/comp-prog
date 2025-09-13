I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict

inf = float('inf')

n,k = MII()
edges = []
for _ in range(n-1):
    edges.append(LII())
adj = defaultdict(list)

for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)

indp = [[0]*(k+1) for _ in range(n)]

def indp(root,par):
    ans = 0
    for x in adj[root]:
        if x==par:
            continue
        

