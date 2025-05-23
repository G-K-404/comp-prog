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
lis = []
for i in range(n):
    lis.append(LII())
lis.sort()
@lru_cache
def go(i, lastday):
    if i>=n:
        return 0
    if i == n-1:
        return lis[i][2] if lastday<lis[i][0] else 0
    a = go(i+1, lastday)
    b = 0
    if lis[i][0]>lastday:
        b = go(i+1, lis[i][1])+lis[i][2]
    ans = max(a,b)
    return ans
r = go(0,-1)
go.cache_clear()
print(r)

    