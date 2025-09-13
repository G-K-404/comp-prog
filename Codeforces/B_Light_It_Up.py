I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LII = lambda: list(map(int, input().split()))

n, m = MII()
a = LII()
a = [0]+a+[m]
flag = True
on = [0]
off = [0]

for i in range(len(a)-1):
    diff = a[i+1]-a[i]
    if flag:
        on.append(on[-1]+diff)
        off.append(off[-1])
    else:
        on.append(on[-1])
        off.append(off[-1]+diff)
    flag = not flag
ans = on[-1]
for i in range(len(a)-1):
    insert = a[i]+1
    if a[i+1]-a[i]<2:
        continue
    preon = on[i]
    if i%2:
        newtotal = preon
        newtotal+=a[i+1]-insert
        newtotal+=off[-1]-off[i+1]
    else:
        newtotal = preon
        newtotal-=1
        newtotal+=off[-1]-off[i+1]
    ans = max(ans,newtotal)
print(ans)