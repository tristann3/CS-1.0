# Custom Calculator by Tristan Thompson
# 8/27/20
# This will have two functions, a small menu with two calculations
# one part will do a calculation based on two numbers and an operator
# one calculation for finding BMI (body mass index)

import os


def performCalculation():
    print("\n\nWelcome to my Calculator, in order for this to function, you may use one of the four operators: + - * /\n" +
          "So, tell me what you would like me to calculate")
    firstNum = int(input("First number: "))
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
    else:
        print("oh no! you cannot use that operator")
        os.system("clear")
        startingMenu()
    print(answer)


def calculateBMI():
    print("hello")


def startingMenu():
    print("Hello, Welcome to my Calculation Program!\n" +
          "What would you like to do?\n\n")
    selection = input("1) Perform a calculation\n" +
                      "2) Calculate your BMI\n")
    if (selection == "1"):
        performCalculation()
    elif (selection == "2"):
        calculateBMI()
    else:
        exit()

startingMenu()
