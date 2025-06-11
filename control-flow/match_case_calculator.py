#prompt for user input
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("chose the operation (+, -, *, /): ")

#performing the calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"the result of {num1} + {num2} is {result}.")
    case "-":
        result = num1 - num2
        print(f"the result of {num1} - {num2} is {result}.")
    case "*":
        result = num1 * num2
        print(f"the result of {num1} * {num2} is {result}.")
    case "/":
        if num2 == 0:
            print("error: division by zero is not allowed.")
        else:
                result = num1 / num2
                print(f"the result of {num1} / {num2} is {result}.")
        