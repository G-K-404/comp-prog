def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    def solve_matching(arr_a, arr_b):
        n = len(arr_a)
        if n == 0:
            return 0
        
        reachable_a = [set() for _ in range(n)]
        reachable_b = [set() for _ in range(n)]
        
        for i in range(n):
            reachable_a[i].add(arr_a[i])
            reachable_b[i].add(arr_b[i])
        
        changed = True
        while changed:
            changed = False
            for i in range(n - 1):
                old_size_a = len(reachable_a[i])
                reachable_a[i] |= reachable_b[i + 1]
                if len(reachable_a[i]) > old_size_a:
                    changed = True
                
                old_size_b = len(reachable_b[i])
                reachable_b[i] |= reachable_a[i + 1]
                if len(reachable_b[i]) > old_size_b:
                    changed = True
        
        matches = 0
        for i in range(n):
            if reachable_a[i] & reachable_b[i]:
                matches += 1
        
        return matches
    
    max_result = solve_matching(a, b)
    
    for i in range(n):
        new_a = a[:i] + a[i+1:]
        new_b = b[:i] + b[i+1:]
        result = solve_matching(new_a, new_b)
        max_result = max(max_result, result)
    
    return max_result

def main():
    t = int(input())
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()