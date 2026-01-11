I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def forma(y,x):
    if x>y:
        if x%2:
            k = x**2
        else:
            k = (x-1)**2+1
        if y!=1:
            print(k+((y-1) if not x%2 else 1-y))
            return
        elif y==1:
            print(k)
            return
        
    else:
        if not y%2:
            k = y**2
        else:
            k = (y-1)**2+1
        if x!=1:
            print(k+((x-1) if y%2 else 1-x))
            return
        elif x==1:
            print(k)
            return 

t = II()
for _ in range(t):
    x,y = MII()
    forma(x,y)