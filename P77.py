def power2(num):
    if (num==0):
        return 0
    if ((num & (~(num-1))) == num):
        return 1
    return 0

number=int(input("Enter a power of 2, or not: "))
if (power2(number)):
    print("\nThe number is power of 2.")
else:
    print("\nThe number is not power of 2.")