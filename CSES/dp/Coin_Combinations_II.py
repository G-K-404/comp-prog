from functools import lru_cache
import sys
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

sys.setrecursionlimit(10**7)

inf = float('inf')

[n,t] = LII()
coins = LII()
MOD = 10**9+7
# @lru_cache(None)
# def go(i, curramt):
#     if curramt>t:
#         return 0
#     if curramt == t:
#         return 1
#     if i==n:
#         return 0
#     ans = 0
#     ans+=go(i,curramt+coins[i])
#     ans+=go(i+1,curramt)
#     return ans
# r = go(0,0)%MOD
# go.cache_clear()
# print(r)

# dp = [[0]*(t+1) for _ in range(n+1)]
# for i in reversed(range(n)):
#     for j in reversed(range(t+1)):
#         if j==t:
#             dp[i][j] = 1
#             continue
#         ans = 0
#         if j+coins[i]<=t:
#             ans=(ans+dp[i][j+coins[i]])%MOD
#         ans=(ans+dp[i+1][j])%MOD
#         dp[i][j] = ans
# print(dp[0][0]%MOD)


            

# dp = [0]*(t+1)

# for i in range(t,-1,-1):
#     if i==t:
#         dp[i] = 1
#         continue
#     for x in coins:
#         if i+x<=t:
#             dp[i] += dp[i]
# coins.sort()
# def go(prev, cu):
#     if cu>t:
#         return 0
#     if cu==t:
#         return 1
#     ans = 0
#     for x in coins:
#         if x<prev:
#             continue
#         ans+=go(x, cu+x)
#     return ans%mod
# print(go(-1,0))