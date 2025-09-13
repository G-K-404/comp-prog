I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n, m = MII()
    setA = set()
    setB = set()
    for i in range(n):
        row = LII()
        for j, color in enumerate(row):
            if (i + j) & 1:
                setB.add(color)
            else:
                setA.add(color)
    if setA & setB:
        ans = len(setA) + len(setB) - 2
        print(ans)
    else:
        ans = len(setA) + len(setB) - 1
        print(ans)
    
t = II()
for _ in range(t):
    solve()