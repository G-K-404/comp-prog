I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    lis1 = LII()
    lis2 = LII()
    maxi = -inf
    maxindex = 0
    for i in range(len(lis2)):
        if(maxi<lis2[i]):
            maxi = lis2[i]
            maxindex = i
    numops = 0
    for i in range(len(lis2)):
        if(i!=maxindex):
            numops += 2*(lis2[i]-1)+1
    print(numops)

t= II()
for _ in range(t):
    solve()