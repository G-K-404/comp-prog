I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from bisect import bisect_right

inf = float('inf')

def check(num,c,pos):
    cx = 1
    last = pos[0]
    for i in range(1,len(pos)):
        if pos[i]-last>=num:
            dis = pos[i]-last
            last = pos[i]
            cx+=1
            if c==cx:
                return True
    return False



def solve():
    n, c = MII()
    pos = []
    for _ in range(n):
        pos.append(II())
    pos.sort()
    lo,hi = 0,pos[-1]-pos[0]
    ans = n
    while(lo<=hi):
        mid = (lo+hi)//2
        if check(mid,c,pos):
            ans = mid
            lo = mid+1
        else:
            hi = mid-1
    print(ans)

t = II()

for _ in range(t):
    solve()