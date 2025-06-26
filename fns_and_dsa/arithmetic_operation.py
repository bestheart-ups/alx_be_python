#defininig a function name 
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multilpy":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            raise ZeroDivisionError("division by zero is not allowed")
        return num1 / num2
    else:
        print("invalid operation")
    result = perform_operation(3, 0, "divide")
    print(result)