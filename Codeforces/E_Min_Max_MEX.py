I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,k = MII()
    lis = LII()
    lo,hi = 0,n
    ans = 0
    def check(mid):
        if mid == 0:
            return True
        cnt = 0
        vis = set()
        mex = 0
        for i,x in enumerate(lis):
            vis.add(x)
            while mex in vis:
                mex+=1
            if mex==mid:
                cnt+=1
                vis = set()
                mex = 0
        return cnt==k
    while(lo<=hi):
        mid = (lo+hi)//2
        if check(mid):
            ans = mid
            lo = mid+1
        else:
            hi = mid-1
    print(ans)

t = II()

for _ in range(t):
    solve()