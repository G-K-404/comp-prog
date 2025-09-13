I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))

stack = []
inf = float('inf')

def solve():
    s = I()
    if s == "pwd":
        print('/', end="")
        for x in stack:
            print(x, end="")
            print('/', end="")
        print()
        return
    else:
        if(s[3] == '/'):
            lis = s[4:].strip().split('/')
            if(lis[0]!='..'):
                while(stack and stack[-1]!=lis[0]):
                    stack.pop()
        else:
            lis = s[3:].strip().split('/')
        for x in lis:
            if x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
                
        return 

t = II()

for _ in range(t):
    solve()
    
    