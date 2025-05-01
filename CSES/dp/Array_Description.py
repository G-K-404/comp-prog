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

[n,m] = LII()
arr = LII()
mod = 10**9+7

# def go(ind, prev):
#     if(ind == n):
#         return 1
#     if(ind, prev) in memo:
#         return memo[(ind,prev)]
#     memo[(ind,prev)] = 0
#     if arr[ind]!=0:
#         if prev==-1 or abs(arr[ind]-prev)<=1:
#             memo[(ind,prev)]+= go(ind+1, arr[ind])
#         else:
#             return 0
#     else:
#         for i in range(1,m+1):
#             if(prev == -1 or abs(i-prev)<=1):
#                 memo[(ind,prev)]+=go(ind+1, i)
#     return memo[(ind,prev)]

# memo = {}
# go(0,-1)    
# print(memo[(0,-1)])

def go(i,prev):
    if i==n:
        return 1
    ans = 0
    if arr[i]!=0:
        if prev==-1 or abs(arr[i]-prev)<=1:
            ans+=go(i+1, arr[i]) 
        else:
            return 0
    if arr[i] == 0:
        for x in range(1,m+1):
            ans+=go(i+1,x)
    return ans
print(go(0,-1)%mod)

    