I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

n = II()
while(n>1):
    if n%2 !=0:
        print(n, end=" ")
        n = 3*n + 1
    else:
        print(n, end=" ")
        n = n//2
print(n)