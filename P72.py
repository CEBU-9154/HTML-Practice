def rightmost_set_bit(num):
    if num==0:
        return -1

    return num & -num

n=int(input("Enter a number: "))
result=rightmost_set_bit(n)
if result==-1:
    print("No set bit found (number is 0)")
else:
    print("Rightmost set bit value is: ", result)