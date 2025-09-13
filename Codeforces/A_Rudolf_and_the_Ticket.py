I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

t = II()
for _ in range(t):
    [n, m, k] = LII()
    b = LII()
    c = LII()
    ways = 0
    for x in b:
        for y in c:
            if(x+y <=k):
                ways+=1
    print(ways)