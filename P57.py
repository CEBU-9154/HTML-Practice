num=int(input("Enter your number: "))
og_num=num
rev_num=0

while num > 0:
    digit = num % 10
    rev_num=rev_num*10+digit
    num//=10

if og_num == rev_num:
    print(f"{og_num} is a palindrome")
else:
    print(f"{og_num} is not a palindrome")