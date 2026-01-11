I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()

grid = [['']*n for _ in range(n)]
for i in range(n):
    s = I()
    for j in range(n):
        grid[i][j] = s[j]


def go(i,j):
    if i>=n or j>=n:
        return ''
    # print(i,j)
    if i==n-1 and j==n-1:
        return grid[i][j]
    # print(grid[i][j]+go(i+1,j), go(i+1,j))
    a = go(i+1,j)+go(i,j+1)
    b = go(i+1,j)+go(i,j+1)
    if i+1<=n:
        a = grid[i][j]+go(i+1,j)
    if j+1<=n:
        b = grid[i][j]+go(i,j+1)
    return min(a,b)
print(go(0,0))