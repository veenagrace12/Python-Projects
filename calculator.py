# Imports the necessary modules
import math
import random


def calculator():

    
    # Displays options for the user
    def options():
        print("\nOptions")
        print("1.'add'     => to add two numbers")
        print("2.'subtract'=> to subtract two numbers")
        print("3.'multiply'=> to multiply two numbers")
        print("4.'divide'  => to divide two numbers")
        print("5.'more'    => to see  a list of advance operations available")
        print("6.'quit'    => to end the program")
        
    options()
    
    while True:
        user_input = input("\nPlease input your command:")

        # Displays options again for the user
        if user_input == "options":
            pass

        # Displays a list of more operations
        elif user_input == "more":
            print("\nList of more operations")
            print("7.'power'   => to raise a number to the power of another")
            print("8.'sqr'     => to find the square of a number")
            print("9.'sqrt'    => to find the square root of a number")
            print("10.'percent'=> to calculate percentage of a number")
            print("11.'pi'     => to return value for pi")
            print("12.'e'      => to return value for e")
            print("13.'sin'    => to find sine of a number")
            print("14.'cos'    => to find cosine of a number")
            print("15.'tan'    => to find tangent of a number")
            print("16.'exp'    => to find the exponential of a number")
            print("17.'abs'    => to find the absolute value of a number")
            print("18.'log'    => to return a log value")
            print("19.'fact'   => to find a factorial of a number")
            continue
            
            
        # Exits the user from the calculator
        elif user_input == "quit":
            print("\nThank you for using this calculator ")
            break
               
        
        # Adds two numbers
        elif user_input == "add":
            input1 = float(input("Enter the first number:"))
            input2 = float(input("Enter the second number:"))
            output = input1 + input2
            print("\nThe Addition of 2 numbers is ", input1, "+", input2, "=",output)
           
        
        # Subtracts two numbers
        elif user_input == "subtract":
            input1 = float(input("Enter the first number:"))
            input2 = float(input("Enter the second number:"))
            output = input1 - input2
            print("\nThe Subtraction of 2 numbers is ", input1, "-", input2, "=",output)
        
        # Multiplies two numbers
        elif user_input == "multiply":
            input1 = float(input("Enter the first number:"))
            input2 = float(input("Enter the second number:"))
            output = input1 * input2
            print("\nThe Multiplication of 2 numbers is ", input1, "*", input2, "=",output)
        
        # Divides two numbers
        elif user_input == "divide":
            input1 = float(input("Enter the first number:"))
            input2 = float(input("Enter the second number:"))
            output = input1 / input2
            print("\nThe Division of 2 numbers is ", input1, "/", input2, "=",output)
                
        # Raises a number to the power of another
        elif user_input == "powers":
            input1 = float(input("Enter the first number:"))
            input2 = float(input("Enter the second number:"))
            output = input1 ** input2
            print("\nThe Power of 1st number to 2nd number is ", input1, "^", input2, "=",output)
                
        # Finds the square of a number
        elif user_input == "sqr":
            input1 = float(input("Enter the first number:"))
            output = input1 **2
            print("\nThe Square of a number is ", input1, "*", input1, "=",output)
            
        # Finds the square root of a number
        elif user_input == "sqrt":
            input1 = float(input("Enter the first number:"))
            output = str(math.sqrt(input1))
            print("\nThe Square root of a number is ", input1, "^","1/2",  "=",output)
            
        # Calculates percentage of a number
        elif user_input == "percent":
            input1 = float(input("Enter a number:"))
            output = str(input1 / 100)
            print("\nThe Percentage of a number is ", input1, "%",  "=",output)
    
        
        # Returns value for pi
        elif user_input == "pi":
            output = str(math.pi)
            print("\nThe value of pi is ", output)
        
        # Returns value for e
        elif user_input == "e":
            output = str(math.e)
            print("\nThe value of e is ",output)
        
        # Finds the sine of a number
        elif user_input == "sin":
            n = float(input("Enter a number:"))
            output = str(math.sin(n))
            print("\nThe value of sin",(n), "is ",output)
            
        
        # Finds the cosine of a number
        elif user_input == "cos":
            n = float(input("Enter a number:"))
            output = str(math.cos(n))
            print("\nThe value of cos",(n) ,"is ",output)
            
        
        # Finds the tangent of a number
        elif user_input == "tan":
            n = float(input("Enter a number:"))
            output = str(math.tan(n))
            print("\nThe value of tan",(n), "is ",output)
            
        
        # Exponential of a number e^x
        elif user_input == "exp":
            n = float(input("Enter a number:"))
            print("\nThe exponential of a number is ",math.exp(n))
            
        # Absolute value of a number
        elif user_input == "abs":
            n = float(input("Enter a number:"))
            print("\nThe Absolute value of a number is ",abs(n))
            
        # Logarithm value of a number math.log(number,base)
        elif user_input == "log":
            n = float(input("Enter a number:"))
            print("\nThe logarithm of a number is ",math.log(n))
            
        # Factorial of a number x!
        elif user_input == "fact":
            n = int(input("Enter a number:"))
            print("\nThe Factorial of a number is ",math.factorial(n))
        
        
        # Is displayed when an unknown input is entered
        else:
            print("Unknown input")

        # Displays the options for the user
        options()


# Runs the calculator
calculator()