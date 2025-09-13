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
    cnt = 2
    for _ in range(n):
        l = LI()
        tcnt = 0
        if l.count('x') == 2:
            tcnt += (cnt-1)*max(int(l[1]), int(l[3]))
        elif l.count('+') == 2:
            tcnt += int(l[1])+int(l[3])
        else:
            if l[0]=='+' and l[2]=='x':
                tcnt+=int(l[1])
                tcnt+=(cnt-1)*int(l[3])
            elif l[2]=='+' and l[0]=='x':
                tcnt+=int(l[3])
                tcnt+=(cnt-1)*int(l[1])
        cnt+=tcnt
    print(tcnt)

t = II()

for _ in range(t):
    solve()
 