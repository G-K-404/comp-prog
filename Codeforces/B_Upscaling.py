I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    size = II()
    if size%2 == 0:
        l = int(size/2)
    else:
        l = int(size/2) + 1
    for i in range(2*size):
        count = 0
        while(True):
            if(int(i/2)%2 == 0):
                if(count < 2*size):
                    print("##", end="")
                    count+=2
                else:
                    break
                if(count < 2*size):
                    print("..", end="")
                    count+=2
                else:
                    break
            else:
                if(count < 2*size):
                    print("..", end="")
                    count+=2
                else:
                    break
                if(count < 2*size):
                    print("##", end="")
                    count+=2
                else:
                    break
        print()
    

t = II()
for _ in range(t):
    solve()