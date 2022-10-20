Text = ("Enter the math action you want to do(+,-,*,/,^ or sqrt); type 'exit' to finish: ")
action = input(Text)
while action != "exit":
    if action == "^":
        number = int(input("Enter number: "))
        print("The square of a number: " + str(number ** 2))
        action = input(Text)
    elif action == "sqrt":
        number = int(input("Enter number: "))
        print("The square root of a number: " + str(number ** 0.5))
        action = input(Text)
    else:
        if action == "+":
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            print("Sum: " + str(first_number + second_number))
            action = input(Text)
        elif action == "-":
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            print("Difference: " + str(first_number - second_number))
            action = input(Text)
        elif action == "*":
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            print("Product: " + str(first_number * second_number))
            action = input(Text)
        elif action == "/":
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            print("Quotient: " + str(first_number / second_number))
            action = input(Text)
        else:
            print("Error")
            action = input(Text)