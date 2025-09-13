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
    s = I()
    if(s[0] != s[-1]):
        for i in range(1, n):
            if(s[i]!=s[0]):
                break
            elif(i == n-1):
                print("NO")
                return
        print("YES")
    else:
        print("NO")

t = II()
for _ in range(t):
    solve()