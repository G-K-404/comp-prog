I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    a,b = MII()
    kx,ky = MII()
    qx,qy = MII()
    dirs = [(a,-b), (-a,b), (a,b), (-a,-b), (b,-a), (-b,a), (b,a), (-b,-a)]
    vis = set()
    ans = 0
    for dx, dy in dirs:
        nx = kx+dx
        ny = ky+dy
        for h,k in dirs:
            if nx+h==qx and ny+k==qy and (nx,ny) not in vis:
                ans+=1
                vis.add((nx,ny))
                break
    print(ans)
t = II()

for _ in range(t):
    solve()