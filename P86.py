def find_all(s):
    n=len(s)
    subsequences=[]

    for i in range(1,1 << n):
        subseq=''
        for j in range(n):
            if i & (1 << j):
                subseq+=s[j]
        subsequences.append(subseq)
    
    return subsequences
input_string=input("Enter a string: ")
all_subsequences=find_all(input_string)
print("\nAll subsequences: ")
for seq in all_subsequences:
    print(seq)