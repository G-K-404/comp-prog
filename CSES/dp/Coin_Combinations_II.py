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
mod = 10**9+7
# def go(ind, curramt):
#     if curramt>t:
#         return 0
#     if curramt == t:
#         return 1
#     ans = 0
#     for i in range(ind, len(coins)):
#         ans += go(i, curramt+coins[i])
#         ans%=mod
#     return ans
# r = go(0,0)%mod
# print(r)

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