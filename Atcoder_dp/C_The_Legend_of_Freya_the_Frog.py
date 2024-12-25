I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    [a, b, k] = LII()
    steps = 0
    if(b==0 and a==0):
        print(0)
        return
    if(b>a):
        if(k%b == 0):
            steps += 2*k//b 
        else:
            steps += 2*(k//b +1)
    else:
        if(k%a == 0):
            if(k/a <= 1):
                steps += 2*k//a
            else:
                steps += 2*k//a -1
        else:
            if(k/a <= 1):
                steps += 2*k//a
            else:
                steps += 2*(k//a +1)
    
    print(steps)

t = II()
for _ in range(t):
    solve()