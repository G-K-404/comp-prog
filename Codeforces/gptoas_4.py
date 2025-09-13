I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict
from functools import lru_cache
inf = float('inf')

n = II()
lis = LI()
dic = defaultdict(int)
for i,x in enumerate(lis):
    dic[x] = i
m = II()
adj = defaultdict(list)
for i in range(m):
    x = LI()
    for y in x:
        adj[i].append(dic[y])
@lru_cache(None)
def go(i,mask):
    if mask==(1<<n)-1:
        return 0
    if i==m:
        return inf
    ans = inf
    ans = min(ans, go(i+1,mask))
    nmask = mask
    for x in adj[i]:
        nmask = nmask|(1<<x)
    ans = min(ans, 1+go(i+1,nmask))
    return ans
@lru_cache(None)
def go2(i,mask):
    if mask==(1<<n)-1:
        return []
    if i==m:
        return None
    nmask = mask
    for x in adj[i]:
        nmask = nmask|(1<<x)
    if go(i+1,mask)<=1+go(i+1,nmask):    
        return go2(i+1,mask)
    rest = go2(i+1,nmask)
    if rest is not None:
        return [i]+rest
    return rest
print(*go2(0,0))