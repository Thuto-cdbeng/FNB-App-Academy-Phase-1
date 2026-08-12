# The program takes a user’s first name, last name, and a short bio message as input, then 
# applies multiple string transformations to produce a formatted user profile output.

# Welcome message
print("Welcome to the String Formatter program. Please follow the prompts to follow to be able to view your username and bio.")
# Collect user first name, last name, and bio message
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
bio = input("Please enter a short bio about yourself: ")

# Create a username combining first initial and last name in lowercase
username = f"{first_name[0].lower()}{last_name.lower()}"

# Display the full name in title case
full_name = f"{first_name} {last_name}".title()
print(f"Your full name is: {full_name}")

# Strip leading and trailing whitespace from the bio before displaying it
bio = bio.strip()

# Count and display the number of characters in the bio
print(f"Your bio has {len(bio)} characters without formatting (i.e., 'I am' not yet replaced with 'I'm')")

# Replace any occurence of 'I am' with 'I'm' 
bio_formatted = bio.replace("i am", "I'm")
bio_formatted = bio_formatted.replace("I am", "I'm")

# Display all output 
print("\nUser Profile: ")
print(f"Your full name is: {full_name}")
print(f"Username: {username}")
print(f"Bio: {bio_formatted}")
print(f"Your bio has {len(bio_formatted)} characters with formatting (i.e., 'I am' replaced with 'I'm')")

# End of program
print("Program has ended. Goodbye")