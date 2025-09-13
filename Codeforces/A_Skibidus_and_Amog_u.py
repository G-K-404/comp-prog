I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    s = I()
    l = len(s)
    if l>2:
        s = s[:l-2]+'i'
    else:
        if s == "us":
            s = 'i'
    print(s)
t = II()
for _ in range(t):
    solve()