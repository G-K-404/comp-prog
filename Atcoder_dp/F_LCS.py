I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

s=I()
s1=I()
s2=[]
# def construct(i,j):
#     if(i>=len(s) or j>=len(s1)):
#         return 
#     if(s[i]==s1[j]):

#         construct(i+1, j+1)
#     elif():
#         construct(i+1, j)
#     else:
#         construct(i, j+1)

# memo = {}
# def solve(i,j):
#     if(i>=len(s) or j>=len(s1)):
#         return 0
#     state = (i,j)
#     if(state in memo):
#         return memo[state]
#     if(s[i]==s1[j]):
#         memo[state] = 1+solve(i+1,j+1)
#         return(memo[state])
#     else:
#         memo[state] = max(solve(i+1,j), solve(i,j+1))
#         return memo[state]

dp = [[0]*(len(s1)+1) for _ in range(len(s)+1)]
for i in reversed(range(len(s)+1)):
    for j in reversed(range(len(s1)+1)):
        if(i >= len(s) or j>= len(s1)):
            dp[i][j]=0
            continue
        if(s[i] == s1[j]):
            dp[i][j] = 1+dp[i+1][j+1]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j+1])
i=0
j=0
while(True):
    if(i>=len(s) or j>=len(s1)):
        break
    if(s[i]==s1[j]):
        s2.append(s[i])
        i+=1
        j+=1
        continue
    elif(dp[i+1][j] > dp[i][j+1]):
        i+=1
        continue
    else:
        j+=1
print("".join(s2))