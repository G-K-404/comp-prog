I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    lis = LII()
    lis1 = LII()
    siz = lis[0]
    c = lis[1]
    d = lis[2]
    hm = min(lis1)
    ind = lis1.index(hm)
    lis2 = list(lis1)
    flag = True
    temp = lis1[0]
    lis1[0] = hm
    lis1[ind] = temp
    for i in range(siz*(siz-1)):
        tem = lis1[i] + d
        if(tem) in lis1:
            lis1[lis1.index(tem)] = lis1[i+1]
            lis1[i+1] = tem
        i+=1
    for i in range(siz*(siz-1)):
        te = lis1[i] + c
        if(te) in lis1:
            lis1[lis1.index(te)] = lis1[i+siz]
            lis1[i+siz] = te
    for i in range(0, siz*(siz-2), siz):
        curr = lis1[i]
        for j in range(i, i+siz -1):
            if(lis1[j] + d != lis1[j+1]):
                flag = False
    for i in range(0, siz*(siz-1)):
        if(lis1[i] + c != lis1[i+siz]):
            flag = False

    print(lis1)
    
    
    if(flag):
        print("YES")
    else:
        print("No")

      
              
        
t=II()
for _ in range(t):
    solve()