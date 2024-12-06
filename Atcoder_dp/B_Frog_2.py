I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    [n,k] = LII()
    stones = LII()
    dp = [inf]*n
    dp[0] = 0
    for i in range(1, n):
        dp[i] = min(dp[i], dp[i-1]+abs(stones[i]-stones[i-1]))
        if(i>1):
            for j in range(2, min(i+1,k+1)):
                dp[i] = min(dp[i], dp[i-j]+abs(stones[i]-stones[i-j]))
    return dp[-1]

print(solve())