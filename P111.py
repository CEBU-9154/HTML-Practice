def rev3rsing(a):
    if len(a) == 1:
        return a[0]
    return a[::-1]

a=[8,72,63,54,25,36,127,68,39]
print("Array is:", a)
print("\n", rev3rsing(a))