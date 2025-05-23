I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


# def solve():
#     n = II()
#     a = []
#     for _ in range(n):
#         tem = LII()
#         a.append(tem)
#     dp = [[-inf] * 3 for _ in range(n+1)]
#     dp[0] = [0,0,0]
#     for i in range(n):
#         for j in range(3):
#             for k in range(3):
#                 if(j==k):
#                     continue
#                 dp[i+1][k] = max(dp[i+1][k], dp[i][j]+a[i][k])
#     return max(dp[n])
# print(solve())

def solve():
    n =II()
    act = []
    for _ in range(n):
        act.append(LII())
    # def go(i,prev):
    #     if i>=n:
    #         return 0
    #     if i==n-1:
    #         asn = 0
    #         for j in range(3):
    #             if(prev==j):
    #                 continue
    #             asn = max(asn, act[i][j])
    #         return asn
    #     ans = 0
    #     for k in range(3):
    #         if (k==prev):
    #             continue
    #         ans = max(ans, act[i][k]+go(i+1,k))
    #     return ans
    # return go(0,-1)
    dp = [[0] * 3 for _ in range(n)]
    
    dp[n-1][0] = act[n-1][0]
    dp[n-1][1] = act[n-1][1]
    dp[n-1][2] = act[n-1][2]
    
    for i in range(n-2, -1, -1):
        dp[i][0] = act[i][0] + max(dp[i+1][1], dp[i+1][2])  
        dp[i][1] = act[i][1] + max(dp[i+1][0], dp[i+1][2])  
        dp[i][2] = act[i][2] + max(dp[i+1][0], dp[i+1][1])  
    
    return max(dp[0])

print(solve())