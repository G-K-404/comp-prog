I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import deque

inf = float('inf')

def bfs(i,j,vi,end):
    q = deque([(i,j,'')])
    vis.add((i,j))
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    while q:
        x,y,ans = q.popleft()
        if (x,y) == end:
            return ans
        for dx, dy in dirs:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in vi and (grid[nx][ny]=='.' or grid[nx][ny]=='B'):
                move = ''
                if dx==0 and dy==1:
                    move+='R'
                elif dx==0 and dy==-1:
                    move+='L'
                elif dx==1 and dy==0:
                    move+='D'
                else:
                    move+='U'
                q.append((nx,ny,ans+move))
                vi.add((nx,ny))
    return ''

n,m = MII()

grid = []

for _ in range(n):
    x = I()
    tmp = []
    for y in x:
        tmp.append(y)
    grid.append(tmp)
vis = set()
ans = ""
end = (-1,-1)
for i in range(n):
    for j in range(m):
        if grid[i][j]=='B':
            end = (i,j)
            break
for i in range(n):
    for j in range(m):
        if grid[i][j]=='A' and (i,j) not in vis:
            t = bfs(i,j,vis,end)
            if len(t)<len(ans) or ans=='':
                ans = t
if len(ans)!=0:
    print("YES")
    print(len(ans))
    print(ans)
else:
    print("NO")
        