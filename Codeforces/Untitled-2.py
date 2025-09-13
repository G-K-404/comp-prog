def find_storage_key(n, x):
    bits = []
    bit_position = 0
    while x > 0:
        if x & 1:
            bits.append(1 << bit_position)
        x >>= 1
        bit_position += 1
    
    if len(bits) >= n:
        print(*bits[:n])
        return
    

    extra_values = set(bits)  
    bit_list = bits[:]
    
    for i in range(len(bit_list)):
        for j in range(i + 1, len(bit_list)):
            extra_values.add(bit_list[i] | bit_list[j])
            if len(extra_values) >= n:  # Stop early if we have enough numbers
                break
        if len(extra_values) >= n:
            break
    
    # Convert set to list and print the first n values
    result = list(extra_values)[:n]
    print(*result)

# Read input
t = int(input().strip())
for _ in range(t):
    n, x = map(int, input().split())
    find_storage_key(n, x)
