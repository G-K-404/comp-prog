I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,k = MII()
    a = LII()
    b = LII()
    su = -1
    if b.count(-1) < n:
        for i, x in enumerate(b):
            if x!=-1:
                if su !=-1 and su!=a[i]+x:
                    return 0
                su = a[i]+x
        for i, x in enumerate(b):
            if a[i]>su or su-a[i]>k:
                return 0
        return 1
    else:
        return max(0,(min(a)+k-max(a)+1))


t = II()
for _ in range(t):
    print(solve())