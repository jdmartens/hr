def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minn = arr[0] + arr[1] + arr[2] + arr[3] 
    maxx = arr[1] + arr[2] + arr[3] + arr[4]
    print(minn, maxx)
