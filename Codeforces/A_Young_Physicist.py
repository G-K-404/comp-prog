I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
sux = 0
suy = 0
suz = 0
for i in range(n):
    [x,y,z] = LII()
    sux+=x
    suy+=y
    suz+=z
if(sux == suy == suz == 0):
    print("YES")
else:
    print("NO")