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
    for i in range(n):
        temp = LII()
        items.append(temp)
    dp = [[0]*(w+1) for i in range(n+1)]
    netval = -1
    for i in range(n):
        for sw in range(1,w+1):
            if(sw - items[i][0] >= 0):
                dp[i+1][sw] = max(dp[i+1][sw], dp[i][sw - items[i][0]] + items[i][1])
            dp[i+1][sw] = max(dp[i+1][sw], dp[i][sw])
    print(dp[n][w])
solve()