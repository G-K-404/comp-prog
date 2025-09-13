from collections import deque
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

t = II()
def solve():
    qs = II()
    q,rq = deque(), deque()
    suff = 0
    rsuff = 0
    total_sum = 0
    for _ in range(qs):
        s = LII()
        if s[0]==3:
            q.append(s[1])
            rq.appendleft(s[1])
            suff+=len(q)*s[1]
            total_sum+=s[1]
            rsuff+=total_sum
        elif s[0]==2:
            q,rq = rq,q
            suff,rsuff=rsuff,suff
        else:
            suff-=(len(q))*q[-1]
            suff+=total_sum
            rsuff+=(len(q))*q[-1]
            rsuff-=total_sum
            q.appendleft(q.pop())
            rq.append(rq.popleft())
        print(suff)
for _ in range(t):
    solve()

