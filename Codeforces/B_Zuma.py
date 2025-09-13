I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')
n = II()
s = LII()

def go(i,j):
    if i>j:
        return 0
    if i==j:
        return 1
    a = go(i+1,j)
    b = go(i+1, j-1)
    return min(a,b)
print(go(0,n))