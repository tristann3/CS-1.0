# Custom Calculator by Tristan Thompson
# 8/27/20
# This will have two functions, a small menu with two calculations
# one part will do a calculation based on two numbers and an operator
# one calculation for finding BMI (body mass index)


import os # used for clearing screen
import math # used for rounding


#This function asks user for what they would like to do
def startingMenu():
    os.system("clear")

    print("Hello, Welcome to my Calculation Program!\n\n")
    print("What would you like to do?\n\n")
    selection = input("1) Perform a calculation\n" +
                      "2) Calculate your BMI\n" +
                      "3) Exit\n")
    if (selection == "1"):
        performCalculation()
    elif (selection == "2"):
        calculateBMI()
    elif (selection == "3"):
        exit()
    else:
        startingMenu()

        
# performs a calcuation based on two numbers and one of the four operators
def performCalculation(): 
    os.system("clear")
    print("Welcome to my Calculator\nYou may use one of the four operators: + - * /\n")
    firstNum = int(input("First number: ")) #converts input to int
    operator = input("Operator: ")
    secondNum = int(input("Second number: "))

    

    if (operator == "+"):
        answer = firstNum + secondNum
    elif (operator == "-"):
        answer = firstNum - secondNum
    elif (operator == "*"):
        answer = firstNum * secondNum
    elif (operator == "/"):
        answer = firstNum / secondNum
    else: #error handler if user enters an invalid operator
        print("\noh no! you cannot use that operator")
        input("\n\nPress Enter...")
        os.system("clear")
        startingMenu()

    print(f"\n\n{firstNum} {operator} {secondNum} is {answer}") #f print allows type conversion
    input("\n\nPress Enter...")

    startingMenu()

# takes in 2 inputs and calculates BMI
def calculateBMI():
    os.system("clear")
    print("Welcome to my BMI Calculator\n\n")

    height = int(input("Enter your height(in inches)"))
    weight = int(input("Enter your weight(in pounds)"))
    BMI = round((weight / (height**2) * 703),2) # rounds the calculation of BMI to 2 decimal points
    
    print(f"\n\nYour BMI is {BMI}")
    input("\n\nPress Enter...")

    startingMenu()

#Program start, clears screen for friendly UX
os.system("clear")

startingMenu()

