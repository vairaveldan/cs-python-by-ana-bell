n = int(input ("enter the range for the factorial :"))
m = 1
fact = 1
# loop through the range
for i in range(2,n+1):
    fact *= i
    m += 1
    if m == n:
        print(f"I going to break out on {m-1}th loop")
        break
    else :
        print(f"I am still inside the {m-1}th loop")
print(f"Factorial of {n} is",fact)