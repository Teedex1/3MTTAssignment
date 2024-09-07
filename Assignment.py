def Addition():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))

    result = num1 + num2
    print("The sum is:", result)

Addition()

def Subtraction():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))

    result = num1 - num2
    print("The difference is:", result)

Subtraction()

def Multiplication():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))

    result = num1 * num2
    print("The Answer is:", result)

Multiplication()

def Division():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))

    if num2 != 0:
        result = num1 / num2
        print("The quotient is:", result)
    
Division()