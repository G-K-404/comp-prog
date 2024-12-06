I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    [n, w] = LII()
    items = []
    for _ in range(n):
        temp = LII()
        items.append(temp)
    valsum = 0
    for x in items:
        valsum+=x[1]
    dp = [[inf]*(valsum+1) for _ in range(n+1)]
    dp[0][0] =0
    for i in range(n):
        for j in range(valsum+1):
            if(j - items[i][1]>=0):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-items[i][1]]+items[i][0])
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
    res = 0
    for j in range(1,valsum+1):
        if(dp[n][j] <= w):
            res = j
    print(res)
solve()
    