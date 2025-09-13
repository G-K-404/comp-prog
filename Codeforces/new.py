# Find all anagrams of a pattern in a string 
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from collections import Counter

inf = float('inf')

s = I()
p = I()
c = Counter(p)
n = len(s)
l2 = len(p)
k = Counter(s[:l2])
ans = []
cnt = 0
for x in k:
    if k[x]==c[x]:
        cnt+=1
    if cnt==l2:
        ans.append(0)
l = 0
for r in range(l2, n):
    k[s[l]]-=1
    if s[l] in c:
        if k[s[l]]<c[s[l]]:
            cnt-=1
    if k[s[l]]==0 :
        k.pop(s[l])
        
    l+=1
    if s[r] in c and s[r] not in k:
        cnt+=1
    k[s[r]]+=1
    if cnt==l2:
        ans.append(l)
print(*ans)