from collections import defaultdict

I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n,m,q = MII()
adj = defaultdict(dict)
for _ in range(m):
    a,b,c = MII()
    adj[a][b] = min(c,adj[a].get(b,inf))
    adj[b][a] = min(c,adj[b].get(a,inf))
print()
dis = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dis[i][i] = 0

for k in range(1,n+1):
    for s in range(1,n+1):
        if k in adj[s]:
            dis[s][k] = min(dis[s][k], adj[s][k]) 


for k in range(1,n+1):
    for s in range(1,n+1):
        for d in range(1,n+1):
            if dis[s][k]<inf and dis[k][d]<inf:
                dis[s][d] = min(dis[s][d], dis[k][d]+dis[s][k])

for _ in range(q):
    n,m = MII()
    print(dis[n][m] if dis[n][m]<inf else -1)