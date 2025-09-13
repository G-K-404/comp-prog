I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    lis = LII()
    for i in range(5):
        min = inf
        minindex = 0
        for j in range(len(lis)):
            if(min>lis[j]):
                min = lis[j]
                minindex = j
        lis[minindex]+=1
    res = 1
    for i in range(len(lis)):
        res*=lis[i]
    print(res)




t = II()

for _ in range(t):
    solve()