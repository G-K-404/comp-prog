I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
grid = []
n = II()
for _ in range(n):
    grid.append(I())
mod = 10**9+7

# def go(i, j):
#     if i>=len(grid[0]):
#         return 0
#     if j>=len(grid):
#         return 0
#     if grid[i][j] == "*":
#         return 0
#     if j == len(grid)-1 and i == len(grid[0])-1:
#         return 1
#     if i == len(grid[0])-1:
#         return go(i,j+1)
#     if j == len(grid)-1:
#         return go(i+1,j)
#     return go(i,j+1)+go(i+1,j)
# print(go(0,0))

# dp = [[0]*len(grid[0]) for _ in range(len(grid))]

# for i in range(len(grid[0])-1,-1,-1):
#     for j in range(len(grid)-1,-1,-1):
#         if(i==len(grid[0])-1 and j==len(grid)-1 and grid[i][j] != "*"):
#             dp[i][j] = 1
#             continue
#         if grid[i][j] == "*":
#             dp[i][j] = 0
#             continue
#         if i==len(grid[0])-1:
#             dp[i][j] += dp[i][j+1]
#             continue
#         if j==len(grid)-1:
#             dp[i][j] += dp[i+1][j]
#             continue
#         dp[i][j] += dp[i+1][j]+dp[i][j+1]
# print(dp[0][0]%mod)
        
def go(i,j):
    if i>=n or j>=n:
        return 0
    if i==n-1 and j==n-1:
        return 1
    if grid[i][j]=='*':
        return 0
    a = go(i+1,j)%mod
    b = go(i,j+1)%mod
    return (a+b)%mod if a<inf and b<inf else 0
print(go(0,0))