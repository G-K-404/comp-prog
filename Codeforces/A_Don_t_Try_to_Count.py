I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n, m = MII()
    x = I()
    s = I()
    ans = 0
    while(ans<=5):
        if s in x:
            print(ans)
            return
        x += x
        ans+=1
    print(-1)
    return
t = II()

for _ in range(t):
    solve()