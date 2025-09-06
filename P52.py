def myFunc(n):
    count=0
    for i in range(0, n+1):
        count+=1
    
    count2=0
    j=1
    while j==n+1:
        count2+=1
        j*=2

    count3=0
    for i in range(0,100):
        count3+=1
    
    print("First Loop Interactions:", count, "=> Time Complexity: O(n)")
    print("Second Loop Interactions:", count2, "=> Time Complexity: O(log n)")
    print("Third Loop Interactions:", count3, "=> Time Complexity: O(n)")

n=16
myFunc(n)