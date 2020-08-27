# Custom Calculator by Tristan Thompson
# 8/27/20
# This will have two functions, a small menu with two calculations
# one part will do a calculation based on two numbers and an operator
# one calculation for finding BMI (body mass index)

def performCalculation():
    print("hi")

def calculateBMI():
    print("hello")

print("Hello, Welcome to my Calculation Program!\n" +
    "What would you like to do?\n\n")

selection = input("1) Perform a calculation\n" +
    "2) Calculate your BMI\n")

if (selection == "1"):
    performCalculation()
elif (selection == "2"):
     calculateBMI()
else: exit()

