def max_diff(arr):
    if len(arr) < 2:
        return 0
    min_val=arr[0]
    max_diff=arr[1] - arr[0]
    
    for i in range(1, len(arr)):
        max_diff=max(max_diff, arr[i] - min_val)
        min_val=max(min_val, arr[i] if arr[i] < min_val else min_val)
    
    return max_diff
arr=[2,3,10,6,4,8,1]
print("Maximum difference: ", max_diff(arr))