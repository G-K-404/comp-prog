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
    ans = []
    ans.append(lis[0])
    l = 1
    for i in range(1,len(lis)):
        if lis[i]>=ans[-1]:
            l+=1
            ans.append(lis[i])
        else:
            l+=2
            ans.append(lis[i])
            ans.append(lis[i])
    print(l)
    print(*ans)


t = II()

for _ in range(t):
    solve()