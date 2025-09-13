I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

[n,k] = LII()

def check(mid):
    
lo = 0
hi = 10**12
ans = 0
while(lo<=hi):
    mid = lo+(hi-lo)//2
    if(check(mid)):
        ans = mid
        hi = mid-1
    else:
        lo = mid+1
print(ans)