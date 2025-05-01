I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
 
 
inf = float('inf')
 
t = II()
# def go(sum):
#     if sum>t:
#         return 0
#     if sum==t:
#         return 1
#     ans = 0
#     for i in range(1,7):
#         ans += go(sum+i)
#     return ans
# print(go(0))
dp = [0]*(t + 1)
for su in range(t,-1,-1):
    if su==t:
        dp[su] = 1
        continue
    for i in range(1,7):
        if su+i<=t: 
            dp[su]+=dp[su + i]
            dp[su] = dp[su]%(10**9+7)
print(dp[0]%(10**9+7))

# def go(k):
#     if k>t:
#         return 0
#     if k==t:
#         return 1
#     ans = 0
#     for x in range(1,7):
#         ans += go(k+x)
#     return ans

# print(go(0))