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
    n,k = MII()
    lis = LII()
    c = defaultdict(int)
    c1 = 0
    for x in range(n):
        for sh in range(64):
            if lis[x]&(1<<sh):
                c1+=1
            else:
                c[sh]+=1
    # print(c1,c)
    c = {x:c[x] for x in sorted(list(c.keys()))}
    for x in c:
        for _ in range(c[x]):
            if (1<<x)<=k:
                c1+=1
                k-=(1<<x)
                # print(k,x)
            else:
                break
    print(c1)


t = II()

for _ in range(t):
    solve()