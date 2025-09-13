from collections import deque
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    n= II()
    lis = deque(sorted(LII()))
    turn =  0
    while(len(lis)!=1):
        if(turn%2 == 0):
            lis.popleft()
        else:
            lis.pop()
        turn += 1
    print(lis[0])
    return
t=II()
for _ in range(t):
    solve()