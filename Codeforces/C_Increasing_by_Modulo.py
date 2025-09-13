I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
 
 
inf = float('inf')
 
[n,m] = LII()
lis = LII()
 
def check(mid):
    ans = 0
    prev = 0
    for i in range(n):
        if(prev<=lis[i]):
            ans=m-lis[i]+prev
            if(ans>mid):
                prev = lis[i]
        else:
            if(prev-lis[i] > mid):
                return False
    return True
 
lo = 0
hi = 10**6
ans = hi
while(lo<=hi):
    mid = lo + (hi-lo)//2
    if(check(mid)):
        ans = mid
        hi = mid-1
    else:
        lo = mid+1
print(ans)