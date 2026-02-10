print("CALCULATOR")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
    
def calculator():
    num_1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num_2 = float(input("What's the second number?: "))
        result = operations[operation_symbol](num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}," 
            " or type 'n' to start a new calculation: ")

        if choice == "y":
            num_1 = result
        else:
            should_continue = False
            calculator()

calculator()

