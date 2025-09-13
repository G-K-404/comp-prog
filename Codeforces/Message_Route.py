I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import deque,defaultdict

inf = float('inf')


n,m = MII()
q = deque([(1,1,[1])])
vis = set()
adj = defaultdict(list)
for _ in range(m):
    u,v = MII()
    adj[u].append(v)
    adj[v].append(u)
while q:
    co,dist,path = q.popleft()
    if co==n:
        print(dist)
        print(*path)
        break
    for x in adj[co]:
        if x not in vis:
            q.append((x,dist+1,path + [x]))
            vis.add(x)
if co!=n:
    print("IMPOSSIBLE")