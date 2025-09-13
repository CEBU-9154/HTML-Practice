def ex(a,b):
    result=1

    if b==0:
        return 1
    elif b>0:
        for _ in range(b):
            result=result*a
    else:
        for _ in range(-b):
            result=result*a
        result=1/result

    return result

print("2 cubed: ", ex(2,3))
print("2 to the power of 0: ", ex(2,0))
print("2 to the power of -2: ", ex(2,-2))