keypad=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def print_combos(nums,curr,output):
    if curr==len(nums):
        print(",".join(output))
        return
    
    digit=nums[curr]
    if digit == 0 or digit == 1:
        return
    
    for ch in keypad[digit]:
        output.append(ch)
        print_combos(nums,curr+1,output)
        output.pop()

numbers=[4,2,3]
print_combos(numbers, 0, [])