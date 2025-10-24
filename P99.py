def Len_ofList(a):
    if a == []:
        return 0
    return 1 + Len_ofList(a[1:])
    

a=[1,2,4,7,3]
print("Length of list = ", Len_ofList(a))