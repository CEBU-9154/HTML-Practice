num=int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number.")
else:
    i=2
    while i <= num // 2:
        if num % i == 0:
            print(num, "is not a prime number")
            break
        i += 1
    else:
        print(num, "is a prime number")