from collections import Counter
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n = II()
    lis = LII()
    c = Counter(lis)
    l,r = -1,-1
    new = -1
    fin = []
    print(c)
    for i,x in enumerate(lis):
        print(x)
        if c[x] > 1 and x!=new:
            print("lol")
            l = i
            new = x
        if new == x and i!=l:
            r = i
            fin.append((l,r))
    dif = -1
    ou = -1
    print(fin)
    for i,x in enumerate(fin):
        if x[1]-x[0]>dif:
            dif = x[1]-x[0]
            ou = i
    if ou<=0:
        print(0)
    else:
        print(l+1, r+1)
    

t = II()
for _ in range(t):
    solve()