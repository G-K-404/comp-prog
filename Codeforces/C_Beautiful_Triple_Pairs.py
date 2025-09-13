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
    dic = {}
    ans = 0
    for i in range(n-2):
        currtrip = (lis[i], lis[i+1], lis[i+2])
        rand = []
        rand.append((0,lis[i+1], lis[i+2]))
        rand.append((lis[i], 0, lis[i+2]))
        rand.append((lis[i], lis[i+1], 0))
        for rans in rand:
            ans += dic.get(rans,0) - dic.get(currtrip,0)
            dic[rans] = dic.get(rans,0)+1
        dic[currtrip] = dic.get(currtrip,0)+1
    print(ans)
    

t = II()
for _ in range(t):
    solve()