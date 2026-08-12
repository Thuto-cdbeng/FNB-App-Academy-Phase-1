# The program stores contacts as a list of dictionaries and allows the user to add, search, view, and delete contacts

# Set up an empty list to store contacts
contact_book = []

# Function definitions
def add_contact():
    # Collect contact information from the user
    name = input("Please enter the contact's name: ")
    phone = input("Please enter the contact's phone number: ")
    email = input("Please enter the contact's email address: ")
    
    # Create a dictionary for the contact and add it to the contact book
    contact = {"name": name, "phone": phone, "email": email}
    contact_book.append(contact)
    print(f"\nContact {name} added successfully!\n")

def search_contact(name):
    #Search contact by name and return the contact if found
    for contact in contact_book:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    # Delete contact by name if found
    for contact in contact_book:
        if contact["name"].lower() ==name.lower():
            print(f"{contact["name"]} successfully deleted")
            del contact_book(name)
        else:
            print("Contact not found")

    
def view_all():
    #Access all contacts and print in formatted method
    for contact in contact_book:
        print(f"Name: {contact["name"]} \t Phone: {contact["phone"]} \t Email: {contact["email"]}")

# Welcome message
print("\nWelcome to the Contact Book program. Please follow the prompts to be able to add, search, view, and delete contacts.\n")

# User menu 
while True:
    print("1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit")
    action = int(input("Please select an action by entering the corresponding number: "))

    if (action == 1):
        add_contact()
    elif (action == 2):
        name = input("Please enter name of contact you would like to search for: ")
        search_contact(name)
    elif (action == 3):
        name = input("Please enter name of contact you would like to delete: ")
        delete_contact(name)
    elif (action == 4):
        print("Your list of contacts is as follows: ")
        view_all()
    else:
        print("Program has ended. Goodbye")
        break
    
