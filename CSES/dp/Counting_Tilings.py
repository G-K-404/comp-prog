I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n,m = MII()

def go(remi, remj):
    if remi<0 or remj<0:
        return 0
    if remi==0 and remj==0:
        return 1
    a = 0
    for i in range(n):
        a += go(remi-1,remj-2)
    b = go(remi-2,remj-1)
    return a+b
print(go(n,m))