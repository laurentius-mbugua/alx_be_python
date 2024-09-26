def perform_operation(num1,num2,operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        case _:
            return "Invalid operation selected."

    perform_operation()
