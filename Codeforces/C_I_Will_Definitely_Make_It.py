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
    for _ in range(t):
        n, k = MII()
        lis = LII()
        cur = lis[k-1]
        nlis = [x for x in lis if x > cur]
        if not nlis:
            print("YES")
            continue

        nlis.sort()
        water = 0
        flag = True

        for x in nlis:
            dt = x - cur
            if water + dt > cur:
                flag = False
                break
            water += dt
            cur = x

        print("YES" if flag else "NO")
solve()
