def b_to_d(binary_str):
    decimal=0
    length=len(binary_str)
    for i in range(length):
        digit=int(binary_str[i])
        power=length-i-1
        decimal+=digit*(2**power)
    return decimal

binary=input("Enter a binary number: ")
print("Decimal Value: ", b_to_d(binary))