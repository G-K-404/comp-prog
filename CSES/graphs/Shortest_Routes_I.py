from heapq import heappop, heappush
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


n,m = MII()
g = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,c = MII()
    g[x].append((y,c))

dis = [inf]*(n+1)

hp = []
dis[1] = 0
heappush(hp, (0, 1))
while(hp):
    dist, cur = heappop(hp)
    for x in g[cur]:
        if dist+x[1]<dis[x[0]]:
            dis[x[0]] = dist+x[1]
            heappush(hp, (dis[x[0]],x[0]))
dis = dis[1:]
print(*dis)
