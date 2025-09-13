I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
def solve():
    n,x = MII()
    lis = LII()
    lis.sort()
    if (min(lis)<x and max(lis)<x) or (min(lis)>x and max(lis)>x):
        return max(abs(min(lis)-x), abs(max(lis)-x))
    else:
        temp = min(abs(min(lis)-x), abs(max(lis)-x))
        ans = 2*temp + max(abs(min(lis)-x), abs(max(lis)-x))
        return ans

t = II()

for _ in range(t):
    print(solve())