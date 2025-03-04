def isValid(s):
    # Write your code here
    if len(s) == 1:
        return "YES"
    counts = {}
    for x in s:
        cnt = counts.get(x, 0)
        cnt = cnt + 1
        counts[x] = cnt
    
    count = 0
    remove_used = False
    print("counts", counts)
    for val in counts.values():
        print("loop, count-{}, val_count-{}".format(count, val))
        if count == 0:
            count = val
        else:
            if count == val:
                continue
            if remove_used:
                return "NO"
            if val == 1:
                remove_used = True
                continue
            if abs(count - val) > 1:
                return "NO"
            
            remove_used = True