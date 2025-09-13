I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


def solve():
    n,w = MII()
    a = LII()
    ans = all(a[i] <= a[i + 1] for i in range(n - 1))
    if ans:
        print("YES")
        return
    if w>1:
        print("YES")
        return
    else:
        print("NO")
        return

t = II()

for _ in range(t):
    solve()