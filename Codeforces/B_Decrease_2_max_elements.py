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
    lis = LII()
    lis = sorted(lis, reverse = True)
    steps = 0
    while(n>1):
        lis[0]-=1
        lis[1]-=1
        if(lis[0] == 0 or lis[1] == 0):
            if(lis[0] == 0 and lis[1] == 0):
                n-=2
            else:
                n-=1
        lis = sorted(lis, reverse = True)
        steps+=1
    print(steps)
solve()