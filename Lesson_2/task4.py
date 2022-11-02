number = int(input("Enter number: "))

factor = 1
for a in range(1,number + 1):
    factor = factor * a
#formula for finding the factorial

print(f"The factorial of {number} is: {factor}")