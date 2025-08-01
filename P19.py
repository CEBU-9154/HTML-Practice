def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def divide(x, y):
    return x/y
num1=int(input("Enter number one: "))
num2=int(input("Enter number two: "))
print("Sum: ", add(num1,num2))
print("Difference: ", sub(num1,num2))
print("Product: ", mul(num1,num2))
print("Quotient: ", divide(num1,num2))