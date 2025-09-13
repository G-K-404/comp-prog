I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    time = I()
    req = int(time[0]+time[1])
    ans=""
    if(req>=12):
        flag = True
    else:
        flag = False
    if(req > 12):
        if(req-12 >= 10):
            ans+=str(abs(req-12))
        else:
            ans+=str(0) + str(req-12)
    elif(req == 0):
        ans+=str(12)
    else:
        if(req >= 10):
            ans+=str(req)
        else:
            ans+=str(0) + str(req)
    ans+= ":"
    ans+= time[3] + time[4]
    if(flag):
        ans+= " PM"
    else:
        ans+= " AM"
    print(ans)

t = II()
for _ in range(t):
    solve()