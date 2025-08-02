lst=['Apple', 'Guava', 'Banana', 'Watermelon', 'Orange']

print("Length of list: ", len(lst))
print("First Element: ", lst[0])
print("Last Element: ", lst[4])

lst.append('Papaya')
print("Updated List: ", lst)

lst.remove('Guava')
print("Updated List (2.0): ", lst)

lst.sort()
print("Sorted List: ", lst)

lst.pop(1)
print("Updated List: ", lst)

lst.reverse()
print("Reversed List: ", lst)

print("Multiplication on list: ", lst*2)

lst=lst[:4]
print("Sliced list: ", lst)