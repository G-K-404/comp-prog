from collections import deque
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from math import floor, log2

inf = float('inf')

n = II()
cost = LII()
minWeit = II()
ans = 0
for i in range(len(cost)):
    if (1<<i) & minWeit:
        ans+=cost[i]
print(ans)