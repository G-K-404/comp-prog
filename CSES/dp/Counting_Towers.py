import sys
# from functools import lru_cache
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

inf = float('inf')

def solve():
    MOD1 = 10**9 + 7
    n = II()

    def go(i,l):
        if i==n:
            memo[(i,l)] = 1
            return 1
        if (i,l) in memo:
            return memo[(i,l)]
        memo[(i,l)] = go(i + 1, 1) + go(i + 1, 2) #future adds
        if l==1:
            memo[(i,l)]+=go(i + 1,1)*3
        if l==2:
            memo[(i,l)]+=go(i + 1,2)
        return memo[(i,l)]%MOD1
    for i in range(n,-1,-1):
        for j in range(1,3):
            go(i,j)
    r = go(0,0)
    return r

t = II()
for _ in range(t):
    memo = {}
    print(solve())

