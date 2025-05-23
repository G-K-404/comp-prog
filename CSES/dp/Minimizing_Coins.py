I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

[n,t] = LII()
coins = LII()
# def go(curamt):
#     if curamt>t:
#         return inf
#     if curamt==t:
#         return 0
#     ans = inf
#     for x in coins:
#         ans = min(ans, go(curamt+x)+1)
#     return ans
# print(go(0) if go(0)!=inf else -1)

dp = [inf]*(t+1)
for amt in range(t,-1,-1):
    if amt==t:
        dp[amt] = 0
        continue
    for x in coins:
        if amt+x > t:
            continue
        dp[amt] = min(dp[amt], dp[amt+x]+1)
print(dp[0] if dp[0]!=inf else -1)

# def go(cu):
#     if cu>t:
#         return inf
#     if cu==t:
#         return 0
#     ans = inf
#     for x in coins:
#         ans=min(ans,go(cu+x)+1)
#     return ans if ans<inf else -1
# print(go(0))