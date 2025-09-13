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
    ans = 0
    cnt = 0
    flag = False
    kix = -1
    for i,x in enumerate(lis):
        if flag and i-kix>=2:
            flag = False
        if not flag and x==0:
            cnt+=1
        if x==1:
            cnt = 0
        if cnt==k:
            ans+=1
            cnt = 0
            flag = True
            kix = i
    print(ans)
t = II()
for _ in range(t):
    solve()