I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n = II()
    lis = []
    st = ""
    for _ in range(n):
        lis.append(I())
    for i in range(n-1, -1, -1):
        for j in range(len(lis[0])):
            if(lis[i][j] == '#'):
                st+=str(j+1)
                st+=" "
    print(st)

t = II()
for _ in range(t):
    solve()