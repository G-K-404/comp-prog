I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import deque,defaultdict

inf = float('inf')

n,m = MII()

grid = []

for _ in range(n):
    x = I()
    tmp = []
    for y in x:
        tmp.append(y)
    grid.append(tmp)

q = deque([])
vis = set()
start = (-1,-1)
time = defaultdict(lambda: float('inf'))
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'M':
            q.append((i,j,0))
            vis.add((i,j))
        if grid[i][j] == 'A':
            start = (i,j,0,'')
            continue

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
while q:
    x,y,t = q.popleft()
    for dx,dy in dirs:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]=='.' and (nx,ny) not in vis:
            time[(nx,ny)] = min(time[(nx,ny)], t+1)
            q.append((nx,ny,t+1))
            vis.add((nx,ny))
q = deque([start])
while q:
    x,y,t,path = q.popleft()
    if x==0 or y==0 or x==n-1 or y==m-1:
        print("YES")
        print(len(path))
        print(path)
        exit()
    for dx,dy in dirs:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]=='.' and t+1<time[(nx,ny)]:
            move = ''
            if dx==0 and dy==1:
                move = 'R'
            elif dx==0 and dy==-1:
                move = 'L'
            elif dx==1 and dy==0:
                move = 'D'
            elif dx==-1 and dy==0:
                move = 'U'
            q.append((nx,ny,t+1,path+move))
            vis.add((nx,ny))
print("NO")
