from collections import defaultdict
import sys
sys.setrecursionlimit(1 << 20)

I = lambda: input()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

MOD = 10**9 + 7

def dfs(node, parent):
    res = 1
    color = m - 2 if parent != -1 else m - 1
    cnt = 0
    for child in adj[node]:
        if child == parent:
            continue
        if color - cnt <= 0:
            return 0
        res = res * (color - cnt) % MOD
        res = res * dfs(child, node) % MOD
        cnt += 1
    return res

m = II()
gnod = II()
gfrom = LII()
gto = LII()
adj = defaultdict(list)
for x in range(len(gfrom)):
    adj[gfrom[x]].append(gto[x])
    adj[gto[x]].append(gfrom[x])

ans = m * dfs(1, -1) % MOD
print(ans)