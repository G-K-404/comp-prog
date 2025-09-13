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
    height_map = []
    for _ in range(n):
        height_map.append(LII())
    A = LII()
    B = LII()
    @lru_cache(None)
    def go(i,x):
        if i==n:
            return 0
        ans = inf
        prev = [y+x for y in height_map[i-1]]
        curr = [d+1 for d in height_map[i]]
        ok = True
        for g in range(len(prev)):
            if prev[g]==curr[g]:
                ok = False
                break
        if ok:
            ans = min(ans, go(i+1, 1)+A[i])
        curr = [d for d in height_map[i]]
        ok = True
        for g in range(len(prev)):
            if prev[g]==curr[g]:
                ok = False
                break
        if ok:
            ans = min(ans, go(i+1,0))
        return ans
    @lru_cache(None)
    def go2(i,x):
        if i==n:
            return 0
        ans = inf
        prev = [height_map[y][i-1]+x for y in range(n)]
        curr = [height_map[y][i]+1 for y in range(n)]
        ok = True
        for j in range(len(prev)):
            if prev[j]==curr[j]:
                ok = False
                break
        if ok:
            ans = min(ans, go2(i+1, 1)+B[i])
        curr = [height_map[y][i] for y in range(n)]
        ok = True
        for j in range(len(prev)):
            if prev[j]==curr[j]:
                ok = False
                break
        if ok:
            ans = min(ans, go2(i+1,0))
        return ans
    for i in range(n,-1,-1):
        for j in range(2):
            go(i,j)
            go2(i,j)
    ans1 = min(go(1,0), A[0]+go(1,1))
    ans2 = min(go2(1,0), B[0]+go2(1,1))
    go.cache_clear()
    go2.cache_clear()
    return ans1+ans2 if ans1+ans2 <inf else -1





t = II()

for _ in range(t):
    print(solve())