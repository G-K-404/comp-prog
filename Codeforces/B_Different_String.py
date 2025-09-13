I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    st = I()
    ch = st[0]
    te = 0
    flag = False
    for i in range(len(st)):
        if(st[i]!=ch):
            flag = True
            te = i
            break
    res = ""
    tex = -1
    c = 0
    for i in range(len(st)):
        if(i == te):
            res += st[tex]
        elif(i!=te and c==0):
            res+=st[te]
            tex = i
            c+=1
        else:
            res+=st[i]
    if(flag):
        print("YES")
        print(res)
    else:
        print("NO")

t = II()
for _ in range(t):
    solve()