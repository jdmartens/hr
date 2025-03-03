def lonelyinteger(a):
    # Write your code here
    if len(a) == 1:
        return a[0]
    a.sort()
    print("xxx", a)
    i = 0
    while i < len(a):
        print("trying index-{}, value-{}".format(i, a[i]))
        try:
            second_idx = a.index(a[i], i + 1)
            print("2nd", second_idx)
            i = i + 1
        except ValueError:
            print('no pair', a[i])
            return a[i]
        i = i + 1