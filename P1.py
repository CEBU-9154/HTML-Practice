num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
if num1 < num2:
    if num1 < num3:
        print(num1, "is the smallest number.")
elif num2 < num3:
        print(num2, "is the smallest number.")
else:
    print(num3, "is the smallest number.")