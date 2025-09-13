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
    a = LII()
    b = LII()
    mini = inf
    c = 0
    ind = -1
    for i in range(n):
        if a[i] - b[i] < 0:
            c += 1
            ind = i
            if c > 1:
                print("NO")
                return
        else:
            mini = min(mini, a[i]-b[i])
    if(b[ind]-a[ind] > mini):
        print("NO")
        return
    print("YES")

t = II()
for _ in range(t):
    solve()

