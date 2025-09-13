I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
s = I()
pref = 0
su = 0
prev = 0
first = False
for x in s:
    if x == '1':
        pref+=su+prev-1 if prev!=0 else su
        prev = pref
        su = 0
        first = True
    else:
        if first:
            su+=1
print(prev)