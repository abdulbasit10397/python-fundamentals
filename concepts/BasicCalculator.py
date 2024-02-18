def basic_calculator():
    num1 = float(input("Please Enter Number 1: "))
    operation = input("Please Enter Operation: ")
    num2 = float(input("Please Enter Number 2: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid Operator")

    print("\n******** Result ********* ")
    print("Result: " + str(result))


try:
    basic_calculator()
except UnboundLocalError:
    print("Oops!  That was an error.  Try again...")
