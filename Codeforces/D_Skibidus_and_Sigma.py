I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n, m = LII()
    lis = []
    for _ in range(n):
        lis.append(LII())
    lis.sort()
    lis2 = []
    for i,x in enumerate(lis):
        lis2.append((sum(x),i))
    lis2.sort()
    lis2 = lis2[::-1]
    ans = 0
    fac = n*m
    for i in range(n):
        for j in range(m):
            ans += lis[lis2[i][1]][j]*fac
            fac-=1
    print(ans)
t = II()
for _ in range(t):
    solve()