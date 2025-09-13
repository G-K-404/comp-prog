I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
from math import sqrt

inf = float('inf')

def solve():
    n = II()
    squares = [i*i for i in range(0,100)]
    squares = set(squares)
    if n not in squares:
        print(-1)
        return
    print(int(sqrt(n))//2, int(sqrt(n))//2 + int(int(sqrt(n))%2!=0))
    return 


t = II()
for _ in range(t):
    solve()