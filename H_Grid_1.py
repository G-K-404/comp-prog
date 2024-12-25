I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
from functools import lru_cache 
mod = 10**9 + 7
[H,W] = LII()
maze = []
for _ in range(H):
    tem = I()
    maze.append(tem)
# def go(i,j):
#     if(j==W-1 and i<H-1):
#         if(maze[i+1][j] == '#'):
#             return 0
#         else:
#             return go(i+1,j)%mod
#     if(j<W-1 and i==H-1):
#         if(maze[i][j+1] == '#'):
#             return 0
#         else:
#             return go(i,j+1)%mod
#     if(i==H-1 and j==W-1):
#         return 1
#     if(maze[i][j+1] == '#'):
#         return go(i+1,j)%mod
#     if(maze[i+1][j] == '#'):
#         return go(i,j+1)%mod
#     else:
#         return (go(i,j+1)+go(i+1,j))%mod
# print(go(0,0))

dp = [[0]*(W+1) for _ in range(H+1)]
for i in reversed(range(H)):
    for j in reversed(range(W)):
        if(i==H-1 and j==W-1):
            dp[i][j] = 1
            continue
        if((i+1<H and maze[i+1][j] == '#') and (j+1<W and maze[i][j+1] == '#')):
            dp[i][j]=0
            continue
        elif(j+1<W and maze[i][j+1] == '#'):
            dp[i][j] = (dp[i+1][j])%mod
            continue
        elif(i+1<H and maze[i+1][j] == '#'):
            dp[i][j] = (dp[i][j+1])%mod
            continue
        
        else:
            dp[i][j] = (dp[i][j+1] + dp[i+1][j])%mod
            continue
print(dp[0][0]%mod)   
