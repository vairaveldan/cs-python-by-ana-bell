# string arithmetic operations 
str1 = "run"
str2 =  "baby"
# 1)concatenation 
print (str1 + " " + str2)
# 2)repetition
print ((str1+' ')* 3)


# string has 2 ONES- indexing and slicing 
str3 = "python"
# indexing - accessing - acessing a specific single character in the string using its index
# POSITIVE INDEXING 
for i in range(6):
    print (str3[i],end=' ') # i -> 0,1,2,3,4,5
print() # output : p y t h o n
# NEGATIVE INDEXING
for i in range(-6,0):
    print (str3[i],end=' ') # i -> -6,-5,-4,-3,-2,-1
print() # output : p y t h o n
for i in range(-1,-7,-1):
    print (str3[i],end=' ') # i -> -6,-5,-4,-3,-2,-1
print() # output : n o h t y p

# slicing - access a subset of characters in the string
# syntax : str[start : stop-1 : step]
# example 1
print(str3[0:6:1])
# output : python
# example 2
print(str3[0::2])
# output : pto 
# example 3
print(str3[::-1])
# output : nohtyp
# example 4
print(str3[5:0:-1])
# output : nohty
# example 5
print(str3[-1:-5]) # step is always 1 if not specified
# output : empty string
# example 6
print(str3[-1:-6:-1])
# output : nohtyp
# example 7
a="1234567890"
print(a[10:-11:-1])
# output : 0 9 8 7 6 5 4 3 2 1


#Len function
str4 = "python"
print(len(str4)) # output : 6