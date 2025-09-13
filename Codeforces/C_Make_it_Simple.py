I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

N,M = LII()
ans = 0
se = set()
for _ in range(M):
    v,u = LII()
    if v==u:
        ans+=1
    elif((v,u) in se or (u,v) in se):
        ans+=1
    else:
        se.add((v,u))
        se.add((u,v))
print(ans)