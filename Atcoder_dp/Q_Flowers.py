I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')


n = II()
h = LII()
a = LII()

def go(i,prev):
    if i==n:
        return 0
    b = 0
    c = 0
    if h[i]<prev:
        b = go(i+1,prev)
    else:  
        c = go(i+1,h[i])+a[i]
    return max(c,b)
print(go(0,-1))