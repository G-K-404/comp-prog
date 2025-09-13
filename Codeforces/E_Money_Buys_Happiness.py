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
    n = li[0]
    s = li[1]
    li1 = []
    currmon = 0
    maxhapi = 0
    for x in range(n):
        temp = LII()
        if(currmon >= temp[0]):
            maxhapi += temp[1]
            currmon -= temp[0]
        currmon += s
    print(maxhapi)

t = II()
for _ in range(t):
    solve()