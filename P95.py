def repeat():
    n=int(input("Enter a number (enter a negative number to stop): "))
    if n==0 or n>0:
        repeat()
    else:
        print("That is a negative number.")
        return
repeat()