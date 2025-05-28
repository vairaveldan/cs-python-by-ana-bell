a = input ("enter a word :").strip()
space_count = a.count(' ')
# check if it is word...
if space_count >= 1:
    print("please the word..")
    exit(1)
# find the no of vowels in the word
n = 0
for i in a :
    if i in "aeiou" or i in "AEIOU" :
        n += 1    
print (f"no of vowels in the '{a}' word is : ", n)