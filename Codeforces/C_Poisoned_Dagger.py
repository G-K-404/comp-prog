I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    [n,hp] = LII()
    attsec = LII()

    def check(mid):
        dam = 0
        for i in range(len(attsec)-1):
            dam+=min(attsec[i+1]-attsec[i], mid)
        dam+=mid
        return dam>=hp
        

    lo = 1
    hi = hp
    ans = hp
    while(lo<=hi):
        mid = lo + (hi-lo)//2
        if(check(mid)):
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
    print(ans)


t = II()
for _ in range(t):
    solve()