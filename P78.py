def power4(num):
    count=0
    if (num & (~(num & (num-1)))):
        while(num>1):
            num>>=1
            count+=1
        if (count%2==0):
            return True
        else:
            return False
        
number=int(input("Enter a power of 4, or not: "))
if(power4(number)):
    print(number, 'is a power of 4')
else:
    print(number, "is not a power of 4")