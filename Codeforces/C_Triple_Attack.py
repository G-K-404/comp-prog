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
    a = LII()
    t = 0
    last = 0
    for x in a:
        if(last == 1):
            if(x>1):
                t+=2
                last = t%3
                if(x>4):
                    x-=4
                else:
                    continue
            else:
                t+=x
                last = t%3
                continue
        elif(last == 2):
            t+=1
            last = t%3
            if(x>3):
                x-=3
            else:
                continue
        t+=x%5 + 3*(x//5)
        last = t%3
    print(t)
        
solve()