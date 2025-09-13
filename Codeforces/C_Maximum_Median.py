I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def check(mid,k,arr):
    md = len(arr)//2
    ops = 0
    for i in range(md,len(arr)):
        if mid>=arr[i]:
            ops += mid-arr[i]
    return ops<=k



n,k = MII()
arr = LII()
arr.sort()
lo,hi = min(arr), k+max(arr)
ans = lo
while(lo<=hi):
    mid = (lo+hi)//2
    if check(mid,k,arr):
        ans = mid
        lo = mid+1
    else:
        hi = mid-1
print(ans)