I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict

inf = float('inf')

def solve():
    n = II()
    edges = LII()
    adj = defaultdict(list[int])
    for i in range(len(edges)):
        adj[edges[i]-1].append(i+1)
    ans = [0]*n
    def go(node):
        for x in adj[node]:
            go(x)
            ans[node]+=ans[x]+1
    go(0)
    print(*ans)
solve()