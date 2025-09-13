I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

t = II()
n,m,k = MII()
grid = [[0]*m for _ in range(n)]
if m%2!=0:

else:
    for i in range(n):
        for j in range(m):
            