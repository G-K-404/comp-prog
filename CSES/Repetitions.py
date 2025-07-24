I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
s = I()
ans = 0
l = 0
for r in range(len(s)):
    k = s[r]
    while s[l]!=s[r]:
        l+=1
    ans = max(ans, r-l+1)
print(ans)