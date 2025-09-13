I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import Counter

inf = float('inf')

def solve():
    n  = II()
    arr = LII()
    c = Counter(arr)
    l = []
    su = len(arr)
    r = [su+1]
    for x in range(n):
        if x>0 and c[x-1]==0:
            break
        else:
            l.append(c[x])
            r.append(r[-1]-1)
    r = r[1:]
    diff = [0]*(n+2)
    for i in range(len(l)):
        diff[l[i]]+=1
        if r[i]<n:
            diff[r[i]+1]-=1
    for i in range(1,len(diff)):
        diff[i]+=diff[i-1]
    diff[0]=1
    diff.pop()
    print(*diff)


t = II()

for _ in range(t):
    solve()