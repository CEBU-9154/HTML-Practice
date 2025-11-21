def loes(arr):
    n=len(arr)
    if n==0:
        return 0
    
    max_len=1
    curr_len=1

    for i in range(1, n):
        if (arr[i] % 2) != (arr[i-1] % 2):
            curr_len +=1
            max_len=max(max_len, curr_len)
        else:
            curr_len=1
    return max_len

n=int(input("Enter the number of elements in the array: "))
arr=[]
for _ in range(n):
    arr.append(int(input()))

result=loes(arr)
print("Length of the longest odd-even alternating subarray: ", result)