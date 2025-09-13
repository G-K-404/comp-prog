I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    a,b,n = MII()
    tools = LII()
    time = b-1
    tem = 1
    for x in tools:
        tem = min(a,tem+x)
        time+=tem-1
        tem=1
    print(time+1)
t = II()

for _ in range(t):
    solve()