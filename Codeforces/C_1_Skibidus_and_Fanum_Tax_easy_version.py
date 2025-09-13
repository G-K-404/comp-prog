I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,m = LII()
    lis = LII()
    b = II()
    if len(lis) == 1:
        print("YES")
        return
    lis[0] = min(lis[0], b-lis[0])
    for i in range(1, len(lis)):
        if lis[i]<lis[i-1]:
            if b-lis[i] >= lis[i-1]:
                lis[i] = b-lis[i]
            else:
                print("NO")
                return
        else:
            if b-lis[i]>=lis[i-1]:
                lis[i] = min(lis[i], b-lis[i])
    print("YES")

t = II()
for _ in range(t):
    solve()