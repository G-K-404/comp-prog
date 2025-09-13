from collections import Counter
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
    c = Counter(s)
    k = (n-1)*c['1'] + c['0']
    print(k)
t = II()
for _ in range(t):
    solve()