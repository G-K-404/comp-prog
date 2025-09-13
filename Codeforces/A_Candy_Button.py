I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    lis = LII()
    dela = lis[1]
    times = LII()
    count = 0
    first = True
    prev = times[0]
    for x in times:
        if(first or prev+dela <= x):
            prev = x
            cur = x
            count += 1
            first = False
    return count

print(solve())