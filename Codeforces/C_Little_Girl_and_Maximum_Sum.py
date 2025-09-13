I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

ans = 0
n,q = MII()
arr = LII()
arr.sort(reverse=True)
pref = [0]*n
for _ in range(q):
    l,r = MII()
    pref[l-1]+=1
    if r<n:
        pref[r]-=1
for i in range(1,len(pref)):
    pref[i] = pref[i-1]+pref[i]
pref.sort(reverse=True)
for i in range(n):
    ans += arr[i]*pref[i]
print(ans)