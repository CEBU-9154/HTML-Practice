def EvenorOdd(n):
    if (n^1==n+1):
        return True
    else:
        return False
    
num=int(input("Enter your number: "))
if EvenorOdd(num):
    print(num, "is Even.")
else:
    print(num, "is Odd.")