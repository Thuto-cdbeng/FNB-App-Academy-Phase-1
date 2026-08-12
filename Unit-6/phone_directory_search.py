# The program allows the user to search for a contact eithin their contact list

def search_contact(name):
    found = False
    for contact in contacts:
        if (contact["name"].lower() == name):
            print(f"Found! {contact["name"]}'s number is {contact["number"]}")
            found = True
            break
    return found

# Create dictionary where the keys are friends' names and the values are their phone numbers as strings
contacts = [
    {"name": "Lululemon", "number": "0147852369"},
    {"name": "Rebecca", "number": "0639258741"},
    {"name": "Ricki", "number": "0741369852"}
]

# Ask the user to input the name of the contact to be searched
user_contact = input("Please enter the name of the contact: ")
user_contact = user_contact.strip().lower()

# Use a conditional check to see if the name matches a key in records
if (search_contact(user_contact) == False):
    print("Contact not found")

# End of program 
print("\nProgram has ended. Goodbye")