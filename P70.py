def total(n):
    count=0
    while(n):
        if(n&1==1) or (n&1==0):
            count+=1
        n = n >> 1
    print("Total: ", count)

num=int(input("Enter your number: "))
total(num)