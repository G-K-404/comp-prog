I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    li = LII()
    li1=[]
    li2=[]
    li1.append(li[0])
    li1.append(li[1])
    li2.append(li[2])
    li2.append(li[3])
    flag = False
    boole = False
    tem = max(li)
    lis = []
    lise = []
    if(tem in li1):
        lis = li2
        lise = li1
    else:
        lis = li1
        lise = li2
    it = tem+1
    if((max(lis)%12 < 6 and min(lis)%12 < 6) or (max(lise) > 6 and min(lise) > 6)):
        boole = True
    if(boole):
        tem = min(li)
        lis1 = []
        lise1 = []
        if(tem in li1):
            lis1 = li2
            lise1 = li1
        else:
            lis1 = li1
            lise1 = li2
        tra = max(lise1)
        if(tra == 12):
            tem = tra
        for i in range(tem+1, 12+tem+1):
            if(i>12):
                i = i%12
            if(i in lise1):
                break
            elif(i in lis1):
                flag = True
                break
    else:
        while(it!= tem):
            if(it>12):
                it = it%12
            if(it in lise):
                break
            elif(it in lis):
                flag = True
                break
            else:
                it+=1
    if(flag):
        print("YES")
    else:
        print("NO")

t = II()
for _ in range(t):
    solve()