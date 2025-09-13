I   = lambda: input().rstrip()
II  = lambda: int(input())
MII = lambda: map(int, input().split())
LII = lambda: list(map(int, input().split()))

from heapq import heappush, heappop

def solve():
    n, p = MII()
    a    = LII()
    b    = LII()

    sharers = []
    unact = []
    for j in range(n):
        heappush(unact, (b[j], -a[j], j))

    total = 0
    cnt   = 0

    while cnt < n:
        direct_cost = p

        if sharers:
            share_cost, cap = sharers[0]
        else:
            share_cost, cap = float('inf'), 0

        if direct_cost <= share_cost:
            total += direct_cost
        else:
            total += share_cost
            heappop(sharers)
            if cap - 1 > 0:
                heappush(sharers, (share_cost, cap - 1))

        bj, nega, j = heappop(unact)
        cnt += 1
        heappush(sharers, (b[j], a[j]))

    print(total)


t = II()
for _ in range(t):
    solve()
