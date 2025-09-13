def GCD(a, b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a

def LCM(a,b):
    product=a*b
    if product<0:
        product=-product
    return product//GCD(a,b)

num1=12
num2=18
print("LCM of", num1, "and", num2, "is", LCM(num1,num2))