I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from heapq import heappop,heappush
from collections import defaultdict
inf = float('inf')

n,m = MII()
adj = defaultdict(list)
hp = []
for _ in range(m):
    u,v,x = MII()
    adj[u].append((v,x))
score = [-inf]*(n+1)
hp.append((0,1))
while hp:
    dis,node = heappop(hp)
    dis*=-1
    for v,w in adj[node]:
        if dis+w >score[v]:
            score[v] = dis+w
            heappush(hp,(-score[v],v))
print(score[n])
