I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    l,r = MII()
    ul = 0
    t = r
    ll = 0
    while(t):
        ul+=1
        t=t//10
    print(ul)
    def go(i,co,cno,lz):
        if co+cno-lz<ll:
            return 0
        if co+cno==ul:
            if cno<=3:
                return 1
            else:
                return 0
        


t = II()

for _ in range(t):
    solve()