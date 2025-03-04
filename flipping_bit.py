def flippingBits(n):
    # Write your code here
    binary_string = bin(n)[2:].zfill(32)
    # binary_string = binary_string.zfill(32)
    flip = ""
    for bit in binary_string:
        if bit == "1":
            flop = "0"
        else:
            flop = "1"
        flip = flip + flop
    print("this", n, binary_string, flip)
    return int(flip, 2)