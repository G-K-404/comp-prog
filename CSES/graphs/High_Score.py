from heapq import heappush, heappop
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


n,m = MII()
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y,z = MII()
    adj[x].append((y,z))
dis = [-inf]*(n+1)
dis[1] = 0
hp = []
heappush(hp, (0,1))
while(hp):
    dist, ro = heappop(hp)
    for x in adj[ro]:
        if -dist+x[1] >dis[x[0]]:
            dis[x[0]] = -dist+x[1]
            heappush(hp, (-(dis[x[0]]), x[0]))
print(dis[n])