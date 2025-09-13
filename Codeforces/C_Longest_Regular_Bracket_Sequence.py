I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

s = I()
stack = []
maxi = 0
cnt = 0
overcnt = 0
tempmax = 0
for x in s:
    if x == '(':
        stack.append(x)
        tempmax+=1
        cnt+=1
    elif (stack and ((stack[-1]=='(' and x != ')') or stack[-1] ==')')) or not stack:
        tempmax = 0
        stack.append(x)
    if (stack[-1]=='(' and x == ')'):
        stack.pop()
        cnt-=1
        if cnt == 0:
            if tempmax == maxi:
                overcnt+=1
        else:
            tempmax+=1
        maxi = max(tempmax, maxi)
print(maxi, overcnt+1)        