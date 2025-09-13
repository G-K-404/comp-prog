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
    t = ""
    ans = 0
    while '1' in s or '0' in t:
        for i,x in enumerate(s):
            if x == '1':
                t = s[i:]
                s = s[:i]
                ans+=1
                break
        for i,x in enumerate(t):
            if x == '0':
                s = t[i:]
                t = t[:i]
                ans+=1
                break
    print(ans)

t  = II()
for _ in range(t):
    solve()