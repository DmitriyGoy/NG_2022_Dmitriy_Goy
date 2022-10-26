Text = input("Enter the math action you want to do(+,-,*,/,^ or sqrt); type 'exit' to finish: ")
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
if Text == "^":
    print("The square of a number: " + str(first_number ** second_number))
elif Text == "sqrt":
    print("The square root of a number: " + str((first_number * second_number) ** 0.5))
elif Text == "+":
    print("Sum: " + str(first_number + second_number))
elif Text == "-":
    print("Difference: " + str(first_number - second_number))
elif Text == "*":
    print("Product: " + str(first_number * second_number))
elif Text == "/":
    print("Quotient: " + str(first_number / second_number))
else:
    print("Error")