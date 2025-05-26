secret_number = 5
a = int(input("Enter a number for a guess(0-9):"))
if a < secret_number :
    print("your guess is low")
elif a > secret_number :
    print("your guess is high")
else :
    print("your guess is correct")