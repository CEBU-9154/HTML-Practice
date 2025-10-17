import time

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

def oneto10(n):
    if n>10:
        return
    print (n, end=' ')
    oneto10(n+1)

n_fact=5
sf=time.time()
fr=factorial(n_fact)
ef=time.time()

print("Factorial Function: ")
print(f"Factorial {n_fact} = {fr}")
print(f"Time Taken: {ef - sf: .6f} seconds")
print("Time Complexity: 0(n)")
print("Space Complexity: 0(n)\n")

start_print=time.time()
print("Print 1 to 10 Function:")
oneto10(1)
end_print=time.time()
print(f"\nTime taken: {end_print-start_print:.6f} seconds")
print("Time Complexity: 0(n)")
print("Space Complexity: 0(n)")