I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from functools import lru_cache


inf = float('inf')

n,m = MII()
fa = LII()
sa = LII()

@lru_cache(None)
def go(i,j):
    if i==n or j==m:
        return 0
    c = 0
    if fa[i]==sa[j]:
        c = go(i+1,j+1)+1
    c=max(c,go(i+1,j))
    c = max(c,go(i,j+1))
    return c

print(go(0,0))

@lru_cache(None)
def go2(i,j):
    if i==n or j==m:
        return ''
    c = ''
    if fa[i]==sa[j]:
        c = str(fa[i]) +' '+ go2(i+1,j+1)
    else:
        if go(i+1,j)>go(i,j+1):
            c = go2(i+1,j)
        else:
            c = go2(i,j+1)
    return c

print(go2(0,0))