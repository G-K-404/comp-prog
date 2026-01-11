I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict

inf = float('inf')

n = II()
adj = defaultdict(list[int])
for x in range(n-1):
    u,v = MII()
    u-=1
    v-=1
    adj[u].append(v)
    adj[v].append(u)
inmatch = set()
def go(node, parent):
    if node in inmatch:
        return
    for x in adj[node]:
        if x!=parent:
            go(x, node)
            if x in inmatch or node in inmatch:
                continue
            inmatch.add(x)
            inmatch.add(node)
go(0,-1)
print(len(inmatch)//2)