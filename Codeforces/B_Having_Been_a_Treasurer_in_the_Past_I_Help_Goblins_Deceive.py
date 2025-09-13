I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


def solve():
    n = II()
    s = I()

    h = s.count('-')
    u = s.count('_')

    if h < 2 or u == 0:
        print(0)
        return

    h1 = h // 2
    h2 = h - h1

    print(h1 *u * h2)

t = int(input().strip())
for _ in range(t):
    solve()
