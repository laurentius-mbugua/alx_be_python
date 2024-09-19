num1 = int (input ("Enter first number: "))
num2 = int (input ("Enter second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        print("The result is", num1 + num2, ".")
    case "-":
        print("The result is", num1 - num2, ".")
    case "*":
        print("The result is", num1 * num2, ".")
    case "/":
        if num2 != 0:
            print("The result is", num1 / num2, ".")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation selected.")
