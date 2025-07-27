# #Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition: ", addition)
print("subtraction: ", subtraction)
print("multiplication: ", multiplication)
print("Division: ", division)


#Output:
# Enter the first number: 10
# Enter the second number: 5
# Addition:  15.0
# subtraction:  5.0
# multiplication:  50.0
# Division:  2.0