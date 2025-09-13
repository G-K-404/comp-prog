import sys

def min_ops(n: int) -> int:
    if n == 0:
        return 0
    # iterative application of recurrence from MSB down
    ans = 0
    L = n.bit_length()
    while L > 0:
        top = 1 << (L - 1)
        if n >= top:
            # MSB is 1: apply D_L(2^{L-1}+m) = (2^L - 1) XOR D_{L-1}(m)
            ans = ((1 << L) - 1) ^ ans
            n -= top
        # else MSB 0: nothing to ans, just drop MSB
        L -= 1
    return ans

if __name__ == "__main__":
    data = sys.stdin.read().strip()
    if not data:
        raise SystemExit
    n = int(data.strip())
    print(min_ops(n))
