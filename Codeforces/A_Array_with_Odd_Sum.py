I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def sovle():
    n = II()
    lis = LII()
    odcnt = 0
    for x in lis:
        if x%2 != 0:
            odcnt+=1
    evcnt = n-odcnt
    if n%2 != 0:
        return "YES" if (odcnt!=0) else "NO"
    else:
        return "YES" if (evcnt!=0 and odcnt!=0) else "NO"

t = II()
for _ in range(t):
    print(sovle())