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
    lowbon = n//2 + (n%2 != 0)
    p1 = (lowbon//m) + (lowbon%m != 0)
    p1 = p1*m
    return p1 if p1<=n else -1
print(solve())

