I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def binary_checker(num):
    while(num>=1):
        if(num%10 == 1 or num%10 == 0):
            num = int(num/10)
        else:
            return False
    return True
def solve(val):
    if(binary_checker(val)):
        return True
    flag = False
    for i in range(1, int(val**(0.5))+1):
        if(binary_checker(i)):
            if(val%i == 0):
                che = int(val/i)
                if(binary_checker(che)):
                    flag = True
                    break
                elif(che!=val and solve(che)):
                    flag = True
                    break
    if(flag):
        return True
    else:
        return False
t = II()
for _ in range(t):
    val = II()
    if(solve(val)):
        print("YES")
    else:
        print("NO")