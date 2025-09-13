I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
def sovle():
    n,t = LII()
    start = 10**(n-1)
    for i in range(start, min(10**(n), start+11)):
        if i%t == 0:
            return i
    return -1

print(sovle())