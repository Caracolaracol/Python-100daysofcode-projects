from art import logo
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "_":substract,
    "*":multiply,
    "/":divide
}

num1 = int(input("What's the first number?"))

def calculator():
    print(logo)
    continue_calculation = True
    while continue_calculation:
        num2 = int(input("What's the second number?"))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation:")
        def allOperators():
            if operation_symbol == "+":
                return add(num1, num2)
            elif operation_symbol == "-":
                return substract(num1, num2)
            elif operation_symbol == "*":
                return multiply(num1, num2)
            elif operation_symbol == "/":
                return divide(num1, num2)
        answer = allOperators()
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with ${answer}, or type 'n' to exit.") == "y":
            num1 = answer
        else:
            continue_calculation = False
            calculator()
calculator()