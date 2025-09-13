I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,m = LII()
    lists = []
    for i in range(n):
        lists.append(LII())
    mins = []
    for x in lists:
        mins.append(min(x))
    minl = min(mins)
    fl = []
    for x in lists:
        if(minl == min(x)):
            fl.append(x)
    

t = II()
for _ in range(t):
    solve()