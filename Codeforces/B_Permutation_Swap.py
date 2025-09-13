I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import defaultdict
from math import gcd
inf = float('inf')

def solve():
    n = II()
    lis = LII()
    diffs = []
    for i,x in enumerate(lis):
        diffs.append(abs(i-x+1))
    ans = 0
    for x in diffs:
        ans = gcd(ans,x)
    return ans

t = II()

for _ in range(t):
    print(solve())