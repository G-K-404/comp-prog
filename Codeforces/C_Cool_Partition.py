def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    segments = 0
    i = 0
    
    while i < n:
        # Start a new segment
        current_segment = set()
        
        # Find the earliest position where we can end this segment
        for j in range(i, n):
            current_segment.add(a[j])
            
            # Check if we can end the segment at position j
            can_end = True
            if j < n - 1:  # Not the last position
                # Check if all elements in current segment appear in a[j+1:]
                remaining_elements = set(a[j+1:])
                can_end = current_segment.issubset(remaining_elements)
            
            if can_end:
                segments += 1
                i = j + 1
                break
    
    return segments

t = int(input())
for _ in range(t):
    print(solve())