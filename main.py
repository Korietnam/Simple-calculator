from art import logo
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
  
    calculation = True
    while calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        ending = input(f"Type 'y' to continue calculating with {answer}, or type 'end' to end the program, or type 'new' start a new calculation: ")
        if ending == "end":
            calculation = False
            print(f"Final result is {answer}")
        elif ending == "new":
            calculator()


calculator()