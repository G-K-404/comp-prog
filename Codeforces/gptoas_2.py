I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n,q = MII()
diff = [0]*(n)
for _ in range(q):
    l,r = MII()
    diff[l-1]+=1
    diff[r]-=1
for i in range(1,n):
    diff[i]+=diff[i-1]
ans = 0
for x in diff:
    if x==q:
        ans+=1
print(ans)
