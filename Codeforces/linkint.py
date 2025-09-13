I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from functools import lru_cache

inf = float('inf')

matrix = []
n = II()
for _ in range(n):
    matrix.append(LII())

@lru_cache(None)
def go(i,prev):
    if i==n:
        return 0
    a = inf
    if prev!=0:
        a = min(a,matrix[i][0]+go(i+1,0))
    if prev!=1:
        a = min(a, matrix[i][1]+go(i+1,1))
    if prev!=2:
        a = min(a, matrix[i][2]+go(i+1,2))
    return a
print(go(0,-1))