def divide(dividend, divisor):
    sign=(-1 if((dividend < 0)^ (divisor < 0)) else 1)
    dividend=abs(dividend)
    divisor=abs(divisor)

    quotientNumber=0
    tempNumber=0

    for i in range(31, -1, -1):
        if (tempNumber+(divisor<<i)<=dividend):
            tempNumber+=divisor<<i
            quotientNumber|= 1<<i
        
    if sign==-1:
        quotientNumber=-quotientNumber
    return quotientNumber

a=int(input("Enter number 1 for a/b: "))
b=int(input("Enter number 2 for a/b: "))
print("Result of ",a,"/",b,"is", divide(a, b))