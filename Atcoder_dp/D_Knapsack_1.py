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
    dp = [[0]*(w+1) for _ in range(n+1)]
    netval = -1
    for i in range(n):
        for s_w in range(1,w+1):
            if(s_w - items[i][0] >= 0):
                dp[i+1][s_w] = max(dp[i+1][s_w], dp[i][s_w - items[i][0]] + items[i][1])
            dp[i+1][s_w] = max(dp[i+1][s_w], dp[i][s_w])
    print(dp[n][w])
solve()