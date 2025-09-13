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
    cnt = 1
    lis.sort()
    ans = 1
    for i in range(n-1):
        if lis[i+1]-lis[i]>k:
            cnt = 1
            continue
        cnt+=1
        ans = max(ans,cnt)
    return n-ans

t = II()

for _ in range(t):
    print(solve())