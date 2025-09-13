I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,l = MII()
    doors = LII()
    zero1 = 0
    zero2 = 0
    fir = True
    for i,x in enumerate(doors):
        if x==1:
            if fir:
                zero1 = i
                fir = False
            zero2 = i
    print("YES" if (zero2-zero1)<=(l-1) else "No")

t = II()

for _ in range(t):
    solve()