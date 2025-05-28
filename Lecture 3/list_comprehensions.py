# Initialize the list
list = []
for I in range (0,11):
    list.append(I)
# List comprehension
list = [I for I in range (0,11) if I%2 == 0]
print(list)