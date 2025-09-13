I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

s = I()
ans = 1
prev = ""
count = 0
for x in s:
    if(x==prev):
        count+=1
        ans = max(ans,count)
    else:
        count = 1
        prev = x
print(ans)