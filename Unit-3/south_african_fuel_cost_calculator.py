# The program calculates the cost of driving a distance specified
# by the user, given the current price for petrol

# Welcome message
print("\nWelcome to the Fuel Cost Calculator!")

# Ask user amount of kilomneters they want to drive
kilometers = float(input("Please enter how many kilometers you want to drive: "))
# Ask the current petrol price per liter
petrol_price = float(input("Please enter the current petrol price per liter (in Rands): "))

# Assume the car uses exactly 1 liter per 10 km
# Formula: liters_needed = kilometres/10
# Calculate the total cost (liters_needed * petrol_price)
liters_needed = kilometers / 10
total_cost = round(liters_needed * petrol_price,2)

# Display final results rounded to 2 decimal places
print(f"\nGiven that you want to travel {kilometers} kilometers, with petrol priced at R{petrol_price} per liter your total cost is: R{total_cost: .2f}")

# End of program 
print("\nProgram has ended. Goodbye") 