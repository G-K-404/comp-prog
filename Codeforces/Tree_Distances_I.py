I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict
import sys

sys.setrecursionlimit(3*10**5)
inf = float('inf')



n = II()
edges = []
for _ in range(n-1):
    edges.append(LII())

adj = defaultdict(list)

for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
ind = [0]*(n+1)
pars=[-1]*(n+1)
def indp(root,par):
    ans = 0
    for x in adj[root]:
        if x!=par:
            ans = max(ans,1+indp(x,root))
            pars[x] = par
    ind[root] = ans
    return ans
a = indp(1,-1)
outd = [0]*(n+1)
def outdp(root,par):
    m1,m2 = -1,-1
    ans = 0
    for x in adj[root]:
        if x==par:
            continue
        if ind[x]>m1:
            m2 = m1
            m1 = ind[x]
        elif ind[x]>m2:
            m2 = ind[x]
    for v in adj[root]:
        ans = 0
        if v==par:
            continue
        if ind[v]==m1:
            ans = max(ans, 2+m2)
        else:
            ans = max(ans, 2+m1)
        outd[v] = max(ans, 1+outd[root])
        outdp(v,root)
    return ans
a = indp(1,-1)
b = outdp(1,-1)
    
ans = [max(ind[i],outd[i]) for i in range(len(ind))]
ans = ans[1:]
print(*ans)