I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    [m, a, b, c] = LII()
    x = min(m,a)
    y = min(m,b)
    res = min(x+y+c, 2*m)
    print(res)

t = II()
for _ in range(t):
    solve()