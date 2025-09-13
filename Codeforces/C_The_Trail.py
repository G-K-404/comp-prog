I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    [n,m] = LII()
    path = I()
    altgrid = []
    for i in range(n):
        altgrid.append(LII())
    coords = (0,0)
    for x in path:
        if x == 'R':
            tempsu = 0
            for i in range(n):
                tempsu+=altgrid[i][coords[1]]
            altgrid[coords[0]][coords[1]] = -1*tempsu
            coords = (coords[0],coords[1]+1)
        
        else:
            tempsu = 0
            for i in range(m):
                tempsu+=altgrid[coords[0]][i]
            altgrid[coords[0]][coords[1]] = -1*tempsu
            coords = (coords[0]+1,coords[1])
    altgrid[coords[0]][coords[1]] = -sum(altgrid[coords[0]])
    for i in range(n):
        print(*altgrid[i])
    return

t = II()
for _ in range(t):
    solve()