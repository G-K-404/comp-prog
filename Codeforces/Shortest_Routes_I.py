I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict
from heapq import heappop, heappush

inf = float('inf')

n,m = MII()

adj = defaultdict(list)
for _ in range(m):
    u,v,w = MII()
    adj[u].append((v,w))
hp = []
heappush(hp,(0,1))
dist = [inf]*(n+1)
dist[1] = 0
while hp:
    dis,node = heappop(hp)
    for v,w in adj[node]:
        if dist[v]>dis+w:
            dist[v] = dis+w
            heappush(hp,(dist[v],v))
print(*dist[1:])