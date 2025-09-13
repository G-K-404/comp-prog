I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
n,t = MII()
arr = LII()
ans = 0
l = 0
currt = 0
for r in range(n):
    currt+=arr[r]
    while currt>t:
        currt-=arr[l]
        l+=1
    ans = max(ans,r-l+1)
print(ans)