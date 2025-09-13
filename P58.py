numLargest=int(input("Enter the largest number: "))
numSmallest=int(input("Enter the smallest number: "))

while(numSmallest):
    numStore=numSmallest
    numSmallest=numLargest%numSmallest
    numLargest=numStore

print(f"HCF is: ", numLargest)