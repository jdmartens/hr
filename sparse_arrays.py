def matchingStrings(strings, queries):
    # Write your code here
    ret_arr = []
    
    for qs in queries:
        num = 0
        pos = -1
        looper = True
        while looper:
            print('tryng qs-{}, {}'.format(qs, pos))
            try:
                pos = strings.index(qs, pos + 1)
                num = num + 1
            except ValueError:
                ret_arr.append(num)
                looper = False
                
    print("res", ret_arr)        
    return ret_arr
