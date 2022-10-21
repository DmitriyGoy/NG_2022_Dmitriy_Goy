Text = ("Enter the math action you want to do(+,-,*,/,^ or sqrt); type 'exit' to finish: ")
user_number = ("Enter number: ")
user_first_number = ("Enter first number: ")
user_second_number = ("Enter second number: ")
action = input(Text)
while action != "exit":
    if action == "^":
        number = int(input(user_number))
        print("The square of a number: " + str(number ** 2))
        action = input(Text)
    elif action == "sqrt":
        number = int(input(user_number))
        print("The square root of a number: " + str(number ** 0.5))
        action = input(Text)
    else:
        if action == "+":
            first_number = int(input(user_first_number))
            second_number = int(input(user_second_number))
            print("Sum: " + str(first_number + second_number))
            action = input(Text)
        elif action == "-":
            first_number = int(input(user_first_number))
            second_number = int(input(user_second_number))
            print("Difference: " + str(first_number - second_number))
            action = input(Text)
        elif action == "*":
            first_number = int(input(user_first_number))
            second_number = int(input(user_second_number))
            print("Product: " + str(first_number * second_number))
            action = input(Text)
        elif action == "/":
            first_number = int(input(user_first_number))
            second_number = int(input(user_second_number))
            print("Quotient: " + str(first_number / second_number))
            action = input(Text)
        else:
            print("Error")
            action = input(Text)
