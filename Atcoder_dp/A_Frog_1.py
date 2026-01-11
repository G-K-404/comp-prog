from functools import lru_cache
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
    sth = LII()
    # @lru_cache(None)
    # def go(i):
    #     if i>=n:
    #         return inf
    #     if i==n-1:
    #         return 0
    #     a = inf
    #     b = inf
    #     if i+1<n:
    #         a = abs(sth[i+1]-sth[i])+go(i+1)
    #     if i+2<n:
    #         b = abs(sth[i+2]-sth[i])+go(i+2)
    #     return min(a,b)
    # r = go(0)
    # go.cache_clear()
    # return r
    dp = [inf]*n
    for i in range(n-1,-1,-1):
        if i==n-1:
            dp[i] = 0
            continue
        a = inf
        b = inf
        if i+1<n:
            a = abs(sth[i]-sth[i+1])+dp[i+1]
        if i+2<n:
            b = abs(sth[i+2]-sth[i])+dp[i+2]
        dp[i] = min(a,b)
        continue
    return (dp[0])
        

print(solve())

