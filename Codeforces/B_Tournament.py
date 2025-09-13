I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,j,k = MII()
    lis = LII()
    if k>1:
        print("YES")
    else:
        print("YES" if lis[j-1]==max(lis) else "NO")
t = II()

for _ in range(t):
    solve()