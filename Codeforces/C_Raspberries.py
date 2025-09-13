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
    lis = LII()
    if k!=4:
        ans = inf
        for x in lis:
            if x%k==0:
                print(0)
                return
            ans = min(ans, abs(k-x%k))
        print(ans)
        return
    else:
        cnt = 0
        for x in lis:
            if x%2==0:
                cnt+=1
        ans = max(0,2-cnt)
        for x in lis:
            if x%k==0:
                print(0)
                return
            ans = min(ans, abs(k-x%k))
        print(ans)
        return

t = II()

for _ in range(t):
    solve()