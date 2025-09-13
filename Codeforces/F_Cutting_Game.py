I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    abnm = LII()
    a = abnm[0]
    b = abnm[1]
    n = abnm[2]
    m = abnm[3]
    coords = []
    for x in range(n):
        temp = LII()
        coords.append(temp)
    coords.sort()
    coordsl = sorted(coords,key=lambda x: x[1])
    sA = 0
    sB = 0
    for i in range(m):
        temp = LI()
        k = int(temp[1])
        if(temp[0] == 'U'):
            cons = coords[0:k+1]
            if(i%2==0):
                sA+=len(cons)
            else:
                sB+=len(cons)
        elif(temp[0] == 'D'):
            cons = coords[k-1:]
            print(cons)
            if(i%2==0):
                sA+=len(cons)
            else:
                sB+=len(cons)
        elif(temp[0] == 'L'):
            cons = coordsl[0:k+1]
            if(i%2==0):
                sA+=len(cons)
            else:
                sB+=len(cons)
        elif(temp[0] == 'R'):
            cons = coordsl[k-1:]
            if(i%2==0):
                sA+=len(cons)
            else:
                sB+=len(cons)
    print(sA, sB)

        
        

t = II()
for _ in range(t):
    solve()