I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def solve():
    s = I()
    check = 0
    sr = "hello"
    for x in s:
        if(check == 5):
            print("YES")
            return
        if(x==sr[check]):
            check+=1
    if(check == 5):
        print("YES")
    else:
        print("NO")
solve()