action = input("Enter the math action you want to do(+,-,*,/,^ or sqrt):")
if action == "^":
    number = int(input("Enter number: "))
    print("The square of a number: " + str(number ** 2))
elif action == "sqrt":
    number = int(input("Enter number: "))
    print("The square root of a number: " + str(number ** 0.5))
else:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    if action == "+":
        print("Sum: " + str(first_number + second_number))
    elif action == "-":
        print("Difference: " + str(first_number - second_number))
    elif action == "*":
        print("Product: " + str(first_number * second_number))
    elif action == "/":
        print("Quotient: " + str(first_number / second_number))
    else:
        print("Error")