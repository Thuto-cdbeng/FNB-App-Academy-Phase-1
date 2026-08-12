# The program shows the a secure hint to the user who has forgotten their password

# Welcome message
print("Welcome to the Secure Password Hint Tool. Follow the prompts to follow to be able to receive a secure hint to your forgotten password.")\

# Ask the user to input their secret password and Strip leading/trailing whitespace
password = input("Please input your secret password: ").strip()

# Grab the first and last letter of the password and Display the hint 
print(f"Your password hint: It starts with {password[0].upper()} and ends with {password[-1].upper()}")
# Alternatively
print(f"Your password hint: {password[0]}{'*'*(len(password)-2)}{password[-1]}")

# End of program 
print("Program has ended. Goodbye")