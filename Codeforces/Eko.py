I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def check(mid,trees,m):
    wcol = 0
    for x in trees:
        wcol+= x-mid if x>=mid else 0
    return wcol>=m


n,m = MII()
trees = LII()
ans = 0
lo,hi = 0,max(trees)
while(lo<=hi):
    mid = (lo+hi)//2
    if check(mid,trees,m):
        ans = mid
        lo = mid+1
    else:
        hi = mid-1
print(ans)