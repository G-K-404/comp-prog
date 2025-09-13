import heapq
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
inf = float('inf')
def solve():
    t = II()
    results = []
    for _ in range(t):
        n,k = MII()
        lis = []
        for _ in range(n):
            l,r,real = MII()
            lis.append((l, r, real))
        lis.sort()
        hp = []
        idx = 0
        curr = k
        while True:
            while idx < n and lis[idx][0] <= curr:
                l, r, real = lis[idx]
                if curr <= r:
                    heapq.heappush(hp, (-real, r))
                idx += 1
            while hp and curr > hp[0][1]:  
                heapq.heappop(hp)
            if not hp:
                break
            curr = -heapq.heappop(hp)[0]
        results.append(str(curr))
    print('\n'.join(results))
solve()