I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,k = MII()
    if k%2==1:
        return [n]*(n - 1) + [n - 1]
    else:
        return [n-1 if i!=n-2 else n for i in range(n)]

t = II()
for _ in range(t):
    print(*solve())