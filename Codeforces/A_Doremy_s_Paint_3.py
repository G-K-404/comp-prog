I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

from collections import Counter
inf = float('inf')

def solve():
    n = II()
    lis = LII()
    c = Counter(lis)
    if len(c)>2:
        print("NO")
        return
    if len(c)==2:
        diff = 0
        cnt = 0
        for x in c:
            if cnt%2:
                diff+=c[x]
            else:
                diff-=c[x]
            cnt+=1
        if abs(diff)<=1:
            print("YES")
        else:
            print("NO")
        return
    else:
        print("YES")
        return

t = II()
for _ in range(t):
    solve()