I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,q = MII()
    lis = LII()
    pref = [0]
    for x in lis:
        pref.append(x+pref[-1])
    for _ in range(q):
        l,r,k = MII()
        num = pref[-1]-(pref[r]-pref[l-1])+(r-l+1)*k
        print("YES" if num%2 else "NO")

t = II()

for _ in range(t):
    solve()