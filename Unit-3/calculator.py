# The program takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations.

# Welcome message
print("\nWelcoome to the Calculator. Please follow the prompts to be able to view the results of 6 arithmetic operations on two numbers of your choice.\n")

# Collect two float numbers from the user
num1 = float(input("Please enter the first number here: "))
num2 = float(input("Please enter the second number here: "))
 
# Calculate and Display all results rounded to two decimal laces  
print("\nThe arithmetic operation and their results are as follows:")
print('-'*50)
print("Operation: \t|\t Result:")
print('-'*50)
addition = num1 + num2
print(f"Addition:\t {num1} + {num2} = {addition: .2f}")
subtraction = num1 - num2
print(f"Subtraction:\t {num1} - {num2} = {subtraction: .2f}")
multiplication = num1 * num2
print(f"Multiplication:\t {num1} x {num2} = {multiplication: .2f}")

# Handle division by zero error
if (num2 != 0):
    division = num1 / num2
    print(f"Division:\t {num1} ÷ {num2} = {division: .2f}")
    floor_division = num1 // num2
    print(f"Floor division:\t {num1} // {num2} = {floor_division: .2f}")
    modulus = num1 % num2
    print(f"Modulus:\t {num1} % {num2} = {modulus: .2f}")

else: 
    print(f"Division:\t [Error: Second number is 0]")
    print(f"Floor division:\t [Error: Second number is 0]")
    print(f"Modulus:\t [Error: Second number is 0]")

# End of program 
print("\nProgram has ended. Goodbye")