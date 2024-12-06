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
    stones = LII()
    dp = [inf]*n
    dp[0] = 0
    for i in range(1,n):
        dp[i] = min(dp[i], dp[i-1]+abs(stones[i-1]-stones[i]))
        if(i>1):
            dp[i] = min(dp[i], dp[i-2]+abs(stones[i-2]-stones[i]))
    return dp[-1]

print(solve())
