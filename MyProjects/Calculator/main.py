from base import Calculator

calc = Calculator()

while True:
    x = int(input("Enter your First number:\t"))
    y = int(input("Enter your Second number:\t"))
    operation = input("Operation ':', '*', '+', '-':\t")

    if operation == "*":
        result = calc.multiply(x, y)
        print("Calculated:", result)
    elif operation == ":":
        result = calc.divide(x, y)
        print("Calculated:", result)
    elif operation == "+":
        result = calc.add(x, y)
        print("Calculated:", result)
    elif operation == "-":
        result = calc.substract(x, y)
        print("Calculated:", result)
    else:
        print("Invalid Operation, try again")

    repeat = input("Press 'Enter' to continue or type 'q' to quit: ")
    if repeat.lower() == "q":
        break
