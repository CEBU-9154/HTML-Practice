num=int(input("Enter a number: "))
if num < 50:
    print(num, "is smaller than 50")
elif num == 50:
    print("These numbers are the same.")
else:
    if num%2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number.")