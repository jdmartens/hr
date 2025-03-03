def plusMinus(arr):
    # Write your code here
    num_elements = len(arr)
    num_pos = 0
    num_neg = 0
    num_zero = 0
    for element in arr:
        if element == 0:
            num_zero = num_zero + 1
        elif element < 0:
            num_neg = num_neg + 1
        else:
            num_pos = num_pos + 1
    print(num_pos / num_elements)
    print(num_neg / num_elements)
    print(num_zero / num_elements)
