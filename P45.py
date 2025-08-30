def mult_direct(N, M):
    return N * M

def mult_loop(N, M):
    result=0
    for _ in range(N):
        result+=M
    return result

N=int(input("Enter a number: "))
M=int(input("Enter a number: "))
print("Using direct multiplication: ", mult_direct(N,M))
print("Using N iterations: ", mult_loop(N,M))