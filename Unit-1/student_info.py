# Collect user information: first name, surname, (int)age, and (float)favorite number
first_name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
age = int(input("Please enter your age (in years): "))
favorite_number = float(input("Please enter your favorite number:"))
full_name = first_name + " " + surname
# Display formatted greeting using f-string
print(f"\nWelcome, {full_name}!")

# Display the name in upper case and title case
print(f"Your name in upper case: {full_name.upper()}")
print(f"Your name in title case: {full_name.title()}")

# Calculate and dispaly theh age in months
age_in_months = age*12
print(f"Your age in months is: {age_in_months}")

# Round the favorite number to 2 decimal places
favorite_number_rounded = round(favorite_number, 2)
print(f"Your favorite number rounded to two decimal places is: {favorite_number_rounded} \n")

# Print the data type of each collected value 
print(f"Data type of your first name is: {type(first_name)}")
print(f"Data type of your surname is: {type(surname)}")
print(f"Data type of your age is: {type(age)}")
print(f"Data type of your favorite_number is: {type(favorite_number)} \n")

# End of program 
input("Press enter to end program")
print("Program ended. Goodbye")