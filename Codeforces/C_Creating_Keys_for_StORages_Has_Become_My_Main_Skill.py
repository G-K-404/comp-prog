I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())

def solve():
    n, x = MII()
    
    # Step 1: Extract set bits
    bits = []
    bit_position = 0
    temp_x = x
    while temp_x > 0:
        if temp_x & 1:
            bits.append(1 << bit_position)
        temp_x >>= 1
        bit_position += 1

    k = len(bits)  # Number of set bits
    res = set(bits)  # Store unique numbers
    res.add(x)  # Always include x

    # Step 2: If we need more numbers, generate them safely
    if len(res) < n:
        extra = set()  # Extra elements to be added
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                new_val = bits[i] | bits[j]
                if new_val not in res:
                    extra.add(new_val)
                if len(res) + len(extra) >= n:
                    break
            if len(res) + len(extra) >= n:
                break
        
        res.update(extra)

    # Step 3: Ensure `n` numbers are returned
    res = sorted(res)[:n]  # Sort for consistency

    print(*res)

t = II()
for _ in range(t):
    solve()
