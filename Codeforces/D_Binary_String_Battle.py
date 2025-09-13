I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n,k = MII()
    s = I()
    c = s.count('1')
    if n<k*2:
        print("Alice")
        return
    else:
        print("Alice" if c<=k else "Bob")
        return 


t = II()

for _ in range(t):
    solve()