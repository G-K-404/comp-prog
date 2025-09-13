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
    maxi = -1
    prev = ""
    cnt = 1
    for x in s:
        if x==prev:
            cnt+=1
        else:
            cnt=1
        maxi = max(maxi,cnt)
        prev = x
    return maxi+1
    

t = II()

for _ in range(t):
    print(solve())