import math
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    s1 = I()
    s2 = I()
    a = len(s1)
    b = len(s2)
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    res1 = ""
    for i in range(lcm//a):
        res1 += s1
    res2 = ""
    for i in range(lcm//b):
        res2 += s2
    if(res1 == res2):
        print(res1)
        return
    else:
        print(-1)
t = II()
for _ in range(t):
    solve()