I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    flag = False
    dim = LII()
    n = dim[0]
    m = dim[1]
    matrix = []
    for i in range(m):
        temp = LII()
        matrix.append(temp)
    for i in range(n):
        for j in range(m):
            if(i==0 and j==0):
                if(matrix[i][j]>matrix[i+1][j+1] and matrix[i][j]>matrix[i][j+1] and matrix[i][j]>matrix[i+1][j]):
                    matrix[i][j]-=1
                    flag = True
            if(i==n-1 and j==0):
                if(matrix[i][j]>matrix[i-1][j+1] and matrix[i][j]>matrix[i][j+1] and matrix[i][j]>matrix[i-1][j]):
                    matrix[i][j]-=1
                    flag = True
            if(i==0 and j==m-1):
                if(matrix[i][j]>matrix[i+1][j+1] and matrix[i][j]>matrix[i][j+1] and matrix[i][j]>matrix[i+1][j]):
                    matrix[i][j]-=1
                    flag = True

t= II()
for _ in range(t):
    solve()