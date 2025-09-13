I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


n,m,q = MII()
dist = [[inf]*n for _ in range(n)]
for _ in range(m):
    u,v,w = MII()
    dist[u-1][v-1] = min(dist[u-1][v-1],w)
    dist[v-1][u-1] = min(dist[u-1][v-1],w)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
            else:
                dist[i][j] = 0
for _ in range(q):
    u,v = MII()
    if dist[u-1][v-1]<inf:
        print(dist[u-1][v-1])
    else:
        print(-1)