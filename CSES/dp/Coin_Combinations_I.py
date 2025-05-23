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


# def go(curamt):
#     if curamt>t:
#         return 0
#     if curamt == t:
#         return 1
#     ans = 0
#     for x in coins:
#         ans += go(curamt+x)
#         ans %= (10**9+7)
#     return ans
# r = go(0)

# print(r%(10**9+7))

mod = 10**9+7
# dp = [0]*(t+1)
# for i in range(t,-1,-1):
#     if i==t:
#         dp[i] = 1
#         continue
#     for x in coins:
#         if i+x <= t:
#             dp[i] += dp[i+x]
#             dp[i] %= mod
# print(dp[0]%mod)

# def go(cu):
#     if cu>t:
#         return 0
#     if cu==t:
#         return 1
#     ans = 0
#     for x in coins:
#         ans+=go(cu+x)
#     return ans%mod
# print(go(0))