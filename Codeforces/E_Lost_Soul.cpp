def solve_case():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    def solve_with_arrays(arr_a, arr_b):
        n = len(arr_a)
        if n == 0:
            return 0
        if n == 1:
            return 1 if arr_a[0] == arr_b[0] else 0
        
        # For each position i, we want to know what values a[i] and b[i] can take
        # after performing any sequence of valid operations
        
        # Build the reachability sets
        can_be_a = [set([arr_a[i]]) for i in range(n)]
        can_be_b = [set([arr_b[i]]) for i in range(n)]
        
        # Keep applying operations until no more changes
        # We need to iterate until convergence
        for iteration in range(n):  # At most n iterations should be enough
            changed = False
            
            # Try all possible operations
            for i in range(n - 1):  # i from 0 to n-2
                # Operation 1: a[i] := b[i+1]
                before_size = len(can_be_a[i])
                can_be_a[i].update(can_be_b[i + 1])
                if len(can_be_a[i]) > before_size:
                    changed = True
                
                # Operation 2: b[i] := a[i+1]
                before_size = len(can_be_b[i])
                can_be_b[i].update(can_be_a[i + 1])
                if len(can_be_b[i]) > before_size:
                    changed = True
            
            if not changed:
                break
        
        # Count maximum possible matches
        matches = 0
        for i in range(n):
            # Position i can match if there exists a value that both a[i] and b[i] can take
            common_values = can_be_a[i] & can_be_b[i]
            if common_values:
                matches += 1
        
        return matches
    
    max_matches = 0
    
    # Case 1: Don't remove any element
    max_matches = max(max_matches, solve_with_arrays(a, b))
    
    # Case 2: Remove element at each possible position
    for remove_idx in range(n):
        new_a = a[:remove_idx] + a[remove_idx + 1:]
        new_b = b[:remove_idx] + b[remove_idx + 1:]
        max_matches = max(max_matches, solve_with_arrays(new_a, new_b))
    
    return max_matches

def main():
    t = int(input())
    for _ in range(t):
        print(solve_case())

if __name__ == "__main__":
    main()