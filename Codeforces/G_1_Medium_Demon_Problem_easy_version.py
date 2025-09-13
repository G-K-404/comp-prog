I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

t = II()
for _ in range(t):
    n = II()
    x = LII()
    k = x[0]
    l1 = x[1]
    r1 = x[2]
    l2 = x[3]
    r2 = x[4]

    kvalues = set()
    kmax = r2/l1
    kmin = l2/r1

    m = k
    i = 1
    while m <= kmin:
        m = m * k

    while(m <= kmax):
        kvalues.insert(m)
        m = m * k
    
    result = 0
    
    for x in range(l1 , r1 + 1):
        for y in range(l2 , r2 + 1):
         if (x * y) in kvalues:
            result += 1
    print(result)


    