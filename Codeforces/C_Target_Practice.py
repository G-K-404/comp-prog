I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    grid = []
    for _ in range(10):
        s = I()
        lis = list(map(str,s))
        grid.append(lis)
    ans = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j]=='X':
                if i==0 or j==0 or 9-i==0 or 9-j==0:
                    ans+=1
                elif i==1 or j==1 or 9-i==1 or 9-j ==1:
                    ans+=2
                elif i==2 or j==2 or 9-j==2 or 9-i==2:
                    ans+=3
                elif i==3 or j==3 or 9-i==3 or 9-j==3:
                    ans+=4
                elif i==4 or j==4 or 9-i==4 or 9-j==4:
                    ans+=5
    print(ans)
t = II()

for _ in range(t):
    solve()