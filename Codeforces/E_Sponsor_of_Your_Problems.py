I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from functools import lru_cache

inf = float('inf')

def lisint(x):
    return [int(d) for d in str(x)]

def solve():
    l, r = LII()
    l_digits = lisint(l)
    r_digits = lisint(r)
    n = len(l_digits)
    @lru_cache(None)
    def go(i,tightl, tightr,lsofar, rsofar):
        if i==n:
            return lsofar+rsofar
        left = l_digits[i] if tightl else 0
        right = r_digits[i] if tightr else 9
        ans = inf
        for x in range(left, right+1):
            newtightl = tightl and (x==l_digits[i])
            newtightr = tightr and (x==r_digits[i])
            newlsofar = lsofar + int(x==l_digits[i])
            newrsofar = rsofar + int(x==r_digits[i])
            ans = min(ans, go(i+1,newtightl, newtightr, newlsofar, newrsofar))
        return ans
    r = go(0,True,True,0,0)
    go.cache_clear()
    return r

t = II()
for _ in range(t):
    print(solve())