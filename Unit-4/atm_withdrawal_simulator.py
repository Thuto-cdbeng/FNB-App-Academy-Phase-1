# The program simukates a bank transaction checking if a user has enough money

# Welcome message
print("\nWelcome to the Smart ATM Withdrawal Simulator. You have a bank balance of R1000. Please follow the prompts to be able to carry out a withdrawal transaction.")

# Set fixed variable representing bank balance
bank_balance = 1000
# Ask user how much they want to withdraw
withdraw = float(input("Please enter amount you would like to withdraw: "))
# If the request is less than on equal to the balance, deduct amount and print
if(bank_balance >= withdraw):
    bank_balance = round(bank_balance - withdraw, 2)
    print(f"\nWithdrawal successful! Remaining balance: R{bank_balance: .2f}")
# Elif branch for amoutn less than or equal to 0
elif(withdraw <= 0):
    print("\nInvalid amount entered. You must withdraw more than R0")
# Branch for insufficient funds
else:
    print("\nDeclined. Insufficient funds")

# End of program
print("Program has ended. Goodbye")