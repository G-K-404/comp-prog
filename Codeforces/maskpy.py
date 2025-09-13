I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from math import sqrt
from functools import lru_cache
inf = float('inf')

def solve():
    n = II()
    players = []
    for _ in range(2*n):
        _,x,y = LI()
        x = int(x)
        y = int(y)
        players.append((x,y))
    @lru_cache(None)
    def go(mask):
        if mask==(1<<2*n)-1:
            return 0
        a = inf
        for x in range(2*n):
            if (1<<x)&mask:
                continue
            for y in range(2*n):
                if x==y:
                    continue
                if (1<<y)&mask:
                    continue
                curdist = sqrt((players[x][0]-players[y][0])**2 + (players[x][1]-players[y][1])**2)
                a = min(a,curdist+go(mask|(1<<x)|(1<<y)))
        return a
    return round(go(0),2)
t = II()

for i in range(t):
    print("Case 1: {}".format(solve()))