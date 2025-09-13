I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

[ingg, magg] = LII()
ings = LII()
curr = LII()

def check(num):
    reqmagg = 0
    for i in range(len(ings)):
        reqmagg += max(0, num*ings[i]-curr[i])
    return reqmagg<=magg

lo = 0
hi = 2000
ans = 0
while(lo<=hi):
    mid = lo + (hi-lo)//2
    if(check(mid)):
        ans = mid
        lo = mid+1
    else:
        hi = mid-1
print(ans)