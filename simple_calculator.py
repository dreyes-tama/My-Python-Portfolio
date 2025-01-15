#Diana Reyes Tamayo
#Simple Calculator

#Init

#Function
#defines five functions, one for each mathematical operation.
def add(num1,num2):
    result1 = num1 + num2
    print(result1)

def subtract(num1, num2):
    result2 = num1 - num2
    print(result2)

def multiply(num1, num2):
    result3 = num1 * num2
    print(result3)

def divide(num1, num2):
    result4 = num1/num2
    print(result4)

def simple_calculator():
#Introduce the game and displays options.
    print("Welcome Preschoolers to Simple Calculator")
    while True:
        print("Enter an operation: ")
        print("""1.Addition
        2.Substraction
        3.Multiplication
        4.Division
        5.Quit""")
#Asks players to choose from five mathematical operations
        operation = int(input("(1-5)Operation: "))

#Takes two parameters (two numbers players input) and returns the result of the operation.
#Allows player to play again until player quits.
        if operation == 1: #True
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            add(int1 , int2)

        if operation == 2:
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            subtract(int1, int2)

        if operation == 3:
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            multiply(int1, int2)

        if operation == 4:
            int1 = int(input("Enter your first number:"))
            int2 = int(input("Enter your second number:"))
            divide(int1, int2)
        if operation == 5:
            print("Thank you for using the calculator!")
            break

#MAIN
simple_calculator()
