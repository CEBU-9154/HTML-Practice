def min_flips(arr):
    count_0=0
    count_1=0
    for x in arr:
        if x==0:
            count_0+=1
        else:
            count_1+=1
    return min(count_0,count_1)

arr=list(map(int, input("Enter 0s and 1s seperated by spaces: ").split()))
print("Minimum flips needed =", min_flips(arr))