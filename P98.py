def MaxElementArray(a):
    length=len(a)
    if length==1:
        return a[0]
    
    return max(a[0],MaxElementArray(a[1:]))

a=[1,2,234,745,3,6,653]

print("Largest element of array: ", MaxElementArray(a))