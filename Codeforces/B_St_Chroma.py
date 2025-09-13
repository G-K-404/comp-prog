I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,x = MII()
    lis = [k for k in range(n)]
    if n==x:
        return ' '.join(map(str,lis))
    lis.remove(x)
    lis.append(x)
    return ' '.join(map(str,lis))

t = II()
for _ in range(t):
    print(solve())