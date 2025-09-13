I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    points = LII()
    dist = 100
    for i in range(11):
        curdist = 0
        for j in range(len(points)):
            curdist += abs(i-points[j])
        dist = min(dist, curdist)
    print(dist)
t = II()
for _ in range(t):
    solve()