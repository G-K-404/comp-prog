I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import deque

inf = float('inf')

n,m = MII()

grid = []

for _ in range(n):
    x = I()
    t = []
    for y in x:
        t.append(y)
    grid.append(t)
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(x,y,vi):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in vi and grid[nx][ny]=='.':
                q.append((nx,ny))
                vi.add((nx,ny))

vis = set()
ans = 0
for i in range(n):
    for j in range(m):
        if (i,j) in vis or grid[i][j]=='#':
            continue
        bfs(i,j,vis)
        ans+=1
print(ans)