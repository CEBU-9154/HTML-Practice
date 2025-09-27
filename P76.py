def reverse_bits(num):
    binary_str=bin(num)[2:]
    reversed_str=binary_str[::-1]
    reversed_num=int(reversed_str, 2)
    return reversed_num

num=int(input("Enter a number: "))
result=reverse_bits(num)
print(f"Numver after reversing bits: {result}")