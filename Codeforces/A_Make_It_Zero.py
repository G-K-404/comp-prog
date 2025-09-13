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
    lis = LII()
    if n%2==0:
        print(2)
        print("1 "+ str(n))
        print("1 "+str(n))
        return
    else:
        print(4)
        print("1 "+str(n-1))
        print("1 "+str(n-1))
        print(str(n-1)+" "+str(n))
        print(str(n-1)+" "+str(n))
        return

t = II()

for _ in range(t):
    solve()