I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
MOD = 10**9+7
n,q,k = MII()
arr = LII()
pref = [0]
for i,x in enumerate(arr):
    pref.append(pref[-1]+x*k**(i))
for _ in range(q):
    l,r = MII()
    ans = (pref[r]-pref[l-1])//(k**(l-1))
    ans %= MOD
    print(ans)

