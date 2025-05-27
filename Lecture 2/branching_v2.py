guess = int(input("enter your guess(0-9): "))
secret_number = 7
condition_status = guess == secret_number
if condition_status:
    print("you won")
else :
    print("you lost")