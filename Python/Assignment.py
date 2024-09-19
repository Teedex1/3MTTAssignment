def Addition():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    result = num1 + num2
    print("The sum is:", result)

def Subtraction():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    result = num1 - num2
    print("The difference is:", result)

def Multiplication():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    result = num1 * num2
    print("The answer is:", result)

def Division():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    if num2 != 0:
        result = num1 / num2
        print("The quotient is:", result)
    else:
        print("Error: Division by zero is not allowed.")

def ask_operation():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter your choice: ")

    if choice == 'Addition':
        Addition()
    elif choice == 'Subtraction':
        Subtraction()
    elif choice == 'Multiplication':
        Multiplication()
    elif choice == 'Division':
        Division()
    else:
        print("Choose a valid option.")

ask_operation()
