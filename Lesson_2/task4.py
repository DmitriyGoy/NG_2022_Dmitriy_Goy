number = int(input("Enter number: "))

factor = 1
for value in range(1,number + 1):
    factor = factor * value
#formula for finding the factorial

print(f"The factorial of {number} is: {factor}")