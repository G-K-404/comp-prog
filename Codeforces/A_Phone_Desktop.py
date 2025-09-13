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
    no1 = li[0]
    no4 = li[1]
    n4 = 2
    n1 = 7
    c = 0
    while(no1>0 or no4>0):
        if(no4>n4):
            no4-=n4
            no1-=min(n1, no1)
        else:
            no1-=min(15-(4*no4), no1)
            no4 = 0
        c+=1
    print(c)



t = II()
for _ in range(t):
    solve()