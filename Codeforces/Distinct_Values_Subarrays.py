I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
nums = LII()
s = set()
r = 0
l = 0
ans = 0
for r in range(n):
    while nums[r] in s:
        s.discard(nums[l])
        l+=1
    s.add(nums[r])
    ans+=r-l+1
print(ans)


