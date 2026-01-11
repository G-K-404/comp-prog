I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
ans = []
ans.append(1)
ans.append(6)
for i in range(3,n):
    tmp =0
    boundcells = 2*(i)+2*(i-2)
    tmp+=boundcells*(boundcells-2)//2
    if i**2 - boundcells>1:
        tmp+=