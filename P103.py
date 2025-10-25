def Power_of2(n):
    if n==0:
        return 1
    else:
        return 2 * Power_of2(n-1)
n=int(input("Enter a non-negative integer: "))

if n < 0:
    print("Enter a non-negative integer.")
else:
    result=Power_of2(n)
    print(f"2^{n} = {result}")