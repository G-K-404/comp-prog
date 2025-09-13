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
    se = set(lis)
    def go(i,prev,su):
        if i>=n:
            return inf
        if i==n-1:
            if su not in se:
                if su>0:
                    return su
                



t = II()
for _ in range(t):
    solve()