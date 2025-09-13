I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

ing = I()
curr = LII()
cost = LII()
poss = II()

burc = ing.count('B')
sauc = ing.count('S')
chec = ing.count('C')


def check(num):
    burp = max(0,(num*burc-curr[0])*cost[0])
    saup = max(0, (num*sauc-curr[1])*cost[1])
    chep = max(0, (num*chec - curr[2])*cost[2])
    return (burp+saup+chep) <= poss
lo = 0
hi = poss+200
ans = 0
while(lo<=hi):
    mid = lo +(hi-lo)//2
    if(check(mid)):
        ans = mid
        lo = mid+1
    else:
        hi = mid-1
print(ans)