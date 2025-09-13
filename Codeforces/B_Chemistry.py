I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

from collections import Counter
inf = float('inf')


def solve():
    n,k = MII()
    s = I()
    c = Counter(s)
    cnt = 0
    for x in c:
        if c[x]%2:
            cnt+=1
        if cnt>k+1:
            print("NO")
            return
    print("YES")


t = II()
for _ in range(t):
    solve()