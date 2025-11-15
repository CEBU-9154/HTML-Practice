def pushZerosToEnd(a,a_size):
    zero=0
    non_zero=0
    while(non_zero!=a_size):
        if a[non_zero]!=0:
            a[non_zero], a[zero]=a[zero],a[non_zero]
            zero+=1
        #else:
        non_zero+=1
a=[1,0,3,6,0,0,0,2,355,0,72]
a_size=len(a)
print(a)
pushZerosToEnd(a,a_size)
print("Array after pushing all zeros to end of array: ")
print(a)