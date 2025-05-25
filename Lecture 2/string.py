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
print() # output : n o h t y p

# slicing - access a subset of characters in the string
# syntax : str[start : stop-1 : step]
# example 1
print(str3[0:6:1])
# output : python
# example 2
print(str3[0:6:2])


a="1234567890"
print(a[10:-11:-1])
print(a[-1:-11:-1])