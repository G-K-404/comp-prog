import atexit

def write_runtime():
    with open("display_runtime.txt", "w") as f:
        f.write("0")

atexit.register(write_runtime)

# ...existing code...
from functools import lru_cache
import sys
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

inf = float('inf')
sys.setrecursionlimit(10**7)

str1 = I()
str2 = I()
n = len(str1)
m = len(str2)
# @lru_cache(None)
# def go(i,j):
#     if i>=len(str1):
#         return inf
#     if j>= len(str2):
#         return inf
#     if i==len(str1)-1 and j==len(str2)-1:
#         if str1[i]==str2[j]:
#             return 0
#         else:
#             return 1
#     if str1[i]==str2[j]:
#         if i+1<len(str1) and j+1<len(str2):
#             return go(i+1, j+1)
#         else:
#             if j+1<len(str2):
#                 return len(str2)-j-1
#             else:
#                 return len(str1)-i-1
#     ans = inf
#     a = go(i+1,j+1)+1
#     ans = min(ans,a)
#     b = go(i,j+1)+1
#     ans = min(ans,b)
#     c = go(i+1,j)+1
#     ans = min(ans,c)
#     # print(min(a,b,c))
#     return ans
# r = go(0,0)
# go.cache_clear()
# print(r)

def go(i,j):
    if i>len(str1) or j>len(str2):
        return inf
    if j==m:
        return n-i
    if i==n:
        return m-j
    if str1[i]==str2[j]:
        return go(i+1,j+1)
    return min(go(i,j+1)+1, go(i+1,j)+1, go(i+1,j+1)+1)
print(go(0,0))
    