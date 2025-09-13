I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,k,p = MII()
    if (k<-1*n*p) or (k>n*p):
        print(-1)
        return 
    if k<0:
        ans = (abs(k)//p)+(k%p!=0)
    else:
        ans = (k//p)+(k%p!=0)
    print(ans)

t = II()
for _ in range(t):
    solve()