def checkIfSame(num1, num2):
    if ((num1 ^ num2) != 0):
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

num1=int(input("Enter the first number to compare: "))
num2=int(input("Enter the second number to compare: "))

checkIfSame(num1,num2)