I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
lis= LII()

cur = lis[0]
ans = 0
for x in range(1,n):
    if lis[x]<lis[x-1]:
        ans+=lis[x-1]-lis[x]
        lis[x] = lis[x-1]
print(ans)