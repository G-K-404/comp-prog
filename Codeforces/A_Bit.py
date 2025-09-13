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
    x = 0
    for _ in range(n):
        s = I()
        if s[:2]=='++' or s[1:]=='++':
            x+=1
        elif s[:2]=='--' or s[1:]=='--':
            x-=1
    print(x)
solve()