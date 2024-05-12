continue_calculations = "yes"

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add, "-": subtract, "*": multiply, "/": divide,
}

def calculate(num1, num2, math_operation):

    for key in operations:
        print(key, end=' ')

    answer = operations[math_operation](num1,num2)

    return answer

while continue_calculations == 'yes':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    
    math_operation = input("Pick an operation from the line above: ")
    result = calculate(num1, num2, math_operation)
    print("",end='\n')
    print(f"{num1} {math_operation} {num2} = {result}")

    continue_calculations = input("Add a calculation? Type 'yes' or 'no': ")
