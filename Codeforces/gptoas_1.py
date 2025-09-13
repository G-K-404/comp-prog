I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
lis = LII()
l = 0
n = len(lis)
cnt = 0
ans = 0
for r in range(n):
    cnt += 1 - lis[r]
    while cnt > 1:
        cnt -= 1 - lis[l]
        l += 1
    ans = max(ans, r - l + 1)
print(ans if ans < n else ans - 1)
