def power8(num):
    if num <=0 or (num &(num - 1)) != 0:
        return False
    count=0
    while num>1:
        num>>=1
        count+=1
    
    return count%3==0
num=int(input("Enter a number: "))
if power8(num):
    print(f"{num} is a power of 8.")
else:
    print(f"{num} is NOT a power of 8.")