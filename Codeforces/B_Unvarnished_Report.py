I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    sty = I()
    repsty = I()
    ind = 0
    fag = False
    le = max(len(sty),len(repsty))
    if(len(sty)>len(repsty)):
        big = sty
        smol = repsty
    else:
        big = repsty
        smol = sty
    for i in range(le):
        ind+=1
        if(len(smol)>i and big[i] == smol[i]):
            continue
        else:
            
            fag = True
            break
    if(fag):
        print(ind)
    else:
        print(0)
solve()