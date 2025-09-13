I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def check(mid):
    k = 2
    ans = 0
    while(k**3 <= mid):
        ans += mid//(k**3)
        k+=1
    return ans

m = II()
lo = 0
hi = 10**16
ans = hi
while(lo<=hi):
    mid = lo +(hi-lo)//2
    if(check(mid)>=m):
        ans = mid
        hi = mid-1
    else:
        lo = mid+1
if(check(ans)==m):
    print(ans)
else:
    print(-1)