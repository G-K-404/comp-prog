I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def sovle():
    n = I()
    c = n.count('0')
    c1 = n.count('1')
    if c==c1:
        print(0)
        return
    ans = len(n)
    for x in n:
        if x=='0' and c1>0:
            c1-=1
            ans-=1
        elif x=='1' and c>0:
            c-=1
            ans-=1
        else:
            break
    print(ans)

t = II()
for _ in range(t):
    sovle()