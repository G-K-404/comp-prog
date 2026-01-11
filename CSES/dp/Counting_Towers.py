I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from functools import lru_cache

inf = float('inf')


def solve():
    n = II()
    def go(h):
        if h==n:
            return 1
        b = 0
        for x in range(1,n):
            if x+h<=n:
                b+=2*go(h+x)
        return b+2
    print(go(0))

t = II()

for _ in range(t):
    solve()