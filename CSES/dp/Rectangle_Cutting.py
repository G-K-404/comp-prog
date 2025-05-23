I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

a,b = LII()
def go(r,c):
    if r==1:
        return c-1
    if c==1:
        return r-1
    a = inf
    for i in range(r):
        a = min(a, go(r-i, c)+go(i,c))
    b = inf
    for i in range(c):
        b = min(b, go(r,c-i)+go(r,i))
    return min(a,b)+1
print(go(a,b))
