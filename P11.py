marks=int(input("Enter your marks: "))
if marks == 100:
    print("Perfect score! You pass.")
elif marks >= 60:
    print("Not that perfect, but you still pass :>")
elif marks==50:
    print("Right in the middle, and you passed! :o")
elif marks < 50:
    print("You didn't pass. Try better next time!")
else:
    print("Try again.")