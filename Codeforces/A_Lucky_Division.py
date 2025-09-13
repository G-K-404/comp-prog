I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


def solve():
    luck = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
    se = set(luck)
    n = II()
    if(n in se):
        print("YES")
    else:
        for x in luck:
            if(n%x == 0):
                print("YES")
                return
        print("NO")
solve()