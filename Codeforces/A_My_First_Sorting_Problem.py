I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    li = LII()
    if(li[0]>li[1]):
        print(li[1], li[0])
    else:
        print(li[0], li[1])

t = II()
for _ in range(t):
    solve()