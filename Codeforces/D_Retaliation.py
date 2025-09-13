def can_explode_array(n, a):
    if n == 1:
        return True
    
    d = a[1] - a[0]  
    for i in range(n):
        expected = a[0] + i * d  
        if a[i] != expected:
            return False
    
    a1 = a[0]  
    
    if (a1 - d) % (n + 1) != 0:
        return False
    
    y = (a1 - d) // (n + 1)
    x = d + y
    return x >= 0 and y >= 0

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        if can_explode_array(n, a):
            print("YES")
        else:
            print("NO")

solve()