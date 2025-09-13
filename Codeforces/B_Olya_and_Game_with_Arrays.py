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
    arrs = II()
    mats = []
    for _ in range(arrs):
        n = II()
        mats.append(LII())
    dic = defaultdict(int)
    for i in range(len(mats)):
        mats[i].sort()
    tmp = inf
    idx = -1
    nm = inf
    for i,x in enumerate(mats):
        if x[1]<tmp:
            idx = i
            dic[i] = x[1]
            tmp = x[1]
        nm = min(nm,x[0])
    ans = 0
    n = len(mats)
    for i in range(len(mats)):
        if i==idx%n:
            ans+=nm
        else:
            ans+=mats[i][1]
    print(ans)
    

t = II()

for _ in range(t):
    solve()