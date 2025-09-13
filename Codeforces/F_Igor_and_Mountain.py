I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,m,d = MII()
    grid = [LII() for _ in range(n)]
    MOD = 998244353
    def go(i,j):
        

t = II()

for _ in range(t):
    solve()