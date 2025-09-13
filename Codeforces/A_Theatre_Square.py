I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    [n,m,a] = LII()
    minc = 0
    na = (n%a != 0) + n//a
    ma = (((m-a)%a != 0) + (m-a)//a)*na
    minc = na+ma
    print(minc)
    return

solve()