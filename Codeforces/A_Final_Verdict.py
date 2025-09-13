I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
def solve():
    n,x = MII()
    lis = LII()
    su = sum(lis)
    if su//x == n:
        if su%x==0:
            print("YES")
        else:
            print("NO")
    else:
            print("NO")
    return

t = II()
for _ in range(t):
    solve()