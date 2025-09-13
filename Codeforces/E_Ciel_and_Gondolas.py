I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


n,k = MII()
animousity = []
for _ in range(n):
    lis = LII()
    animousity.append(lis)
pref = [[0]*n for _ in range(n)]
for i in range(len(animousity)):
    for j in range(len(animousity[0])):
        pref[i][j]+=animousity[i][j]+pref[i][j-1]
print(pref)
cost = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        cost[i][j] = cost[i][j-1] + sum(animousity[j][x] for x in range(i, j))

print(cost)
def go(l,r,c):
    if c>k:
        return inf
    if c==k:
        return 0 
    if l==r:
        return 0
    ans = inf
    for m in range(l,r):
        ans=min(ans,+go(l,m,c+1)+go(m+1,r,c+1))
    return ans
print(go(0,n-1,0))