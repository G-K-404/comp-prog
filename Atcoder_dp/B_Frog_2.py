I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

# def solve():
#     [n,k] = LII()
#     stones = LII()
#     dp = [inf]*n
#     dp[0] = 0
#     for i in range(1, n):
#         dp[i] = min(dp[i], dp[i-1]+abs(stones[i]-stones[i-1]))
#         if(i>1):
#             for j in range(2, min(i+1,k+1)):
#                 dp[i] = min(dp[i], dp[i-j]+abs(stones[i]-stones[i-j]))
#     return dp[-1]

# print(solve())

def solve():
    n,k = MII()
    sth = LII()
    # def go(i):
    #     if i>=n:
    #         return inf
    #     if i==n-1:
    #         return 0
    #     ans = inf
    #     for l in range(1,k+1):
    #         if(i+l<n):
    #             ans = min(ans, abs(sth[i+l]-sth[i])+go(i+l))
    #     return ans
    # return go(0)
    dp = [inf]*n
    for i in range(n-1, -1, -1):
        if i==n-1:
            dp[i]=0
            continue
        for l in range(1,k+1):
            if(i+l<n):
                dp[i] = min(dp[i], abs(sth[i+l]-sth[i])+dp[i+l])
    return dp[0]
print(solve())