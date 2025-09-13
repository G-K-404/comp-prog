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
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            print(1)
            return
    print(len(s))

t = II()
for _ in range(t):
    solve()