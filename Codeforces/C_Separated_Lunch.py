I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    deps = II()
    groupdis = LII()
    groupdis.sort()
    n = deps//2
    sum1 = 0
    for i in range(n-1):
        sum1+=groupdis[i]
    sum1+=groupdis[-1]
    sum2 = 0
    j = n-1
    while(j<deps-1):
        sum2+=groupdis[j]
        j+=1
    mini = inf
    ind = n-1
    mintem = 0
    while(ind<deps-1):
        mintem = max(sum1,sum2)
        mini = min(mini,mintem)
        sum1+=groupdis[ind]
        sum2-=groupdis[ind]
        ind+=1
    print(mini)

solve()
