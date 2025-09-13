I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

s = I()
vow = set(['a','e','i','o','u','y'])
res = ""
for x in s:
    if x.lower() in vow:
        continue
    else:
        res+='.'
        res+=x.lower()
print(res)
