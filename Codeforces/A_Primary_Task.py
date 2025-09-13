I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def answer() :
    num = I()

    if (len(num) >=3 and num[0] == '1' and num[1] == '0' and num[2] != '0') :
        exp = int(num[2:])
        if exp >= 2 :
            print("YES")
        else :
            print("NO")
        
        
    else :
        print("NO")



for _ in range(II()) :
    answer()