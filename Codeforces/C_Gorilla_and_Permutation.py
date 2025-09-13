I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    lis = LII()
    n = lis[0]
    m = lis[1]
    k = lis[2]
    res = []
    for i in range(n-m):
        res.append(n-i)
    for i in range(1,m+1):
        res.append(i)
    st = ' '.join(map(str, res))
    print(st)

t= II()

for _ in range(t):
    solve()