from functools import lru_cache
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
import sys
sys.setrecursionlimit(10**5)

inf = float('inf')

n,ke = MII()
x = LII()
mal = max(x)
j = min(x)
s = set(x)
@lru_cache(None)
def go(i, k):
    if i >= ke:
        return k ^ 1
    for move in x:
        if i + move <= ke:
            if go(i + move, k ^ 1) == k:
                return k
    return k ^ 1
if n == 1 and x[0] == 1:
    print('First' if ke % 2 == 1 else 'Second')
else:
    print('First' if go(0, 0) == 0 else 'Second')

