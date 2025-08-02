import random
while True:
    guess=int(input("Enter a number from 1 to 100: "))
    num=random.randint(1, 100)
    if guess > 100:
        print("Please make your number smaller. \n")
    elif guess != num:
        print("Oops! The number was ", num )
        print("\n")
    elif num < 1:
        print("Please enter a bigger number. \n")
    else:
        print("Congrats! You guessed it :D \n")