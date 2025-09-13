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
    bul = False
    cnt = 0
    for i,x in enumerate(s):
        if x=='.':
            cnt+=1
        else:
            cnt= 0
        if cnt==3:
            print(2)
            return
    print(s.count('.'))

t = II()
for _ in range(t):
    solve()