I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


def solve():
    n = II()
    lis = LII()
    def dp(ind, se):
        if ind == n:
            return se
        a = dp(ind, se)
        se.add(ind)
        b = dp(ind, se)
        return (a,b)
    

t = II()
for _ in range(t):
    solve()