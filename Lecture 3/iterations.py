# type 1
n = 10
print("normal iteration:")
for i in range (1,n+1):
    print(i , end = " ")
print("\nstring based iteration using index:")
str = "python"
for i in range (len(str)):
    print(str[i], end = " ")
print("\nList based iteration using index:")
list = [1,2,3,4,5]
for i in range(len(list)):
    print (list[i], end = " ")

# type 2
print("\ndirect access of the characters in the string using for loop :")
for char in str :
    print(char, end = " ")
print("\ndirect access of the elements in the list using for loop :")
for elements in list :
    print(elements, end = " ")
print("\ndirect access of the key and values in the dictionary using for loop :")
dict = {'a':1, 'b':2, 'c':3}
print("key : value :")
for key in dict :
    print(key,"     ",dict[key])
