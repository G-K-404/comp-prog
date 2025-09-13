I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
s = I()
[h,y] = LII()

def check(mid):
    xdis = 0
    ydis = 0
    for x in s:
        if(x=='R'):
            xdis+=1
        if(x=='L'):
            xdis-=1
        if(x=='U'):
            ydis+=1
        if(x=='D'):
            ydis-=1
    if(xdis==h and ydis==y):
        return True
    maxind = -1
    minind = n+1
    while()

lo = 0
hi = n
ans = hi
while(lo<=hi):
    mid = lo +(hi-lo)//2
    if(check(mid)):
        ans = mid
        hi = mid-1
    else:
        lo = mid+1