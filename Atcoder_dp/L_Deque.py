from functools import lru_cache

I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
a = LII()

@lru_cache(None)
def go(turn, l, r):
    if l > r:
        return 0
    ans = max(a[l] - go(turn ^ 1, l + 1, r), a[r] - go(turn ^ 1, l, r - 1))
    return ans

print(go(1, 0, n - 1))

