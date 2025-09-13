import sys
def input(): return sys.stdin.readline().rstrip("\r\n")
def solve():
    n,a,b = list(map(int,input().split()))
    photo = [list(input()) for _ in range(n)]
    if a==0 and b==0:
        cnt = 0
        for x in photo:
            for v in x:
                cnt+=(v=="B" or v=="G")
        return cnt
    result  = 0 
    for i in range(n):
        for j in range(n):
            if photo[i][j]=='B':
                if 0<=i-b<n and 0<=j-a<n:
                    if photo[i - b][j - a]=="W": return -1
                    elif photo[i - b][j - a]=="G":
                        result+=1
                        photo[i - b][j - a]="W"
                        photo[i][j] = "G"
                    else:
                        return -1
                else:
                    return -1
    for i in range(n):
        for j in range(n):
            if photo[i][j]=='G':
                if 0<=i+b<n and 0<=j+a<n and photo[i+b][j+a]=='G':
                    photo[i][j]='W'
                    photo[i+b][j+a]='W'
                    result+=1
                else :
                    result+=1
                    photo[i][j]="W"
    return result        
for _ in range(int(input())):
    t  = solve()
    print(t)