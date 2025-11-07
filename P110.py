def print2L(a, a_size):
    largest=secondLargest = -214783648
    for i in range(a_size):
        if (a[i] > largest):
            secondLargest = largest
            largest= a[i]
        elif (a[i] > secondLargest and a[i] != largest):
            secondLargest=a[i]

    print(secondLargest)

a=[1,2,3,4,5,6,7,8,9]
a_size=len(a)
print2L(a,a_size)