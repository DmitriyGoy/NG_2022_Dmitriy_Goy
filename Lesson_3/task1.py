def math_action():
    action = (input("Enter the math action you want to do(+,-,*,/,^ or sqrt); type 'exit' to finish: "))
    return(action)
    
def number1():
    first_number = int(input("Enter first number: "))
    return(first_number)

def number2():
    second_number = int(input("Enter second number: "))
    return(second_number)

def result(action):
    if action == "^":
        print(f"The square of a number: {number1() ** number2()}")
    elif action == "sqrt":
        print(f"The square root of a number: {number1() ** 0.5}")
    elif action == "+":
        print(f"Sum: " + str(number1() + number2()))
    elif action == "-":
        print(f"Difference: " + str(number1() - number2()))
    elif action == "*":
        print(f"Product: " + str(number1() * number2()))
    elif action == "/":
        print(f"Quotient: " + str(number1() / number2()))
    else:
        print("Error")

result(math_action())