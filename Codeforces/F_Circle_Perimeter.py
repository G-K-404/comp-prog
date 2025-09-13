I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))



inf = float('inf')

def solve():
    k = II()
    c = 0
    l = int(((k+1)/(2)**0.5))
    for i in range(l+2):
        for j in range(l+2):
            if((i**2 + j**2)**0.5 >= k and (i**2 + j**2)**0.5 < k+1):
                c+=1
    c*=4
    c-=4    
    
    print(c)

t = II()

for _ in range(t):
    solve()