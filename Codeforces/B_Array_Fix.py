t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n):
        if arr[i] >= 10:
            arr[i] = [int(d) for d in str(arr[i])]
    
    flag = True
    for i in range(1, n):
        if (arr[i] < arr[i-1]):
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")
