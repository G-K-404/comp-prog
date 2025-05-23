import sys
import math
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

sys.setrecursionlimit(10**7)
inf = float('inf')

n = II()

# def go(cur):
#     if cur<0:
#         return inf
#     if cur==0:
#         return 0
#     ans = inf
#     t = cur
#     tc = 0
#     while(t>0):
#         t=t//10
#         tc+=1
#     # print(tc, cur)
#     for x in range(1,tc+1):
#         if cur%(10**x)//(10**(x-1)):
#             ans = min(ans, go(cur-(cur%(10**x)//(10**(x-1))))+1)
#     return ans
# print(go(0)) 

# dp = [inf]*(n+1)
# for i in range(n+1):
#     if(i==0):
#         dp[i] = 0
#         continue
#     temp = i
#     while temp:
#         digit = temp%10
#         temp = temp//10
#         if i>=digit:
#             dp[i] = min(dp[i], 1+dp[i-digit])
# print(dp[n])


# dp = [inf] * (n + 1)
# dp[0] = 0 

# for i in range(1, n + 1):
#     temp = i
#     while temp > 0:
#         digit = temp % 10  
#         temp //= 10       
#         if digit > 0:      
#             dp[i] = min(dp[i], dp[i - digit] + 1)
# print(dp[n])


def go(cu):
    if cu<0:
        return inf
    if cu==0:
        return 0
    ans = inf
    t = cu
    while(t>0):
        k = t%10
        if k!=0:
            ans= min(ans, go(cu-k) + 1) 
        t = t//10
    return ans
print(go(n))