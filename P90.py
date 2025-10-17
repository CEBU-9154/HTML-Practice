def fwc(n):
    if n==0 or n==1:
        return 1,1
    else:
        fact, count=fwc(n-1)
        return n*fact, count +1
n=5
fact_result, operations=fwc(n) 
print(f"Factorial {n} = {fact_result}")
print(f"Number of operations (multiplications) done: {operations}")  
print(f"Which corresponds to Time Complexity: 0(n)") 