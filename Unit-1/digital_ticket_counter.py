# Welcome message
print("Welcome to the Digital Ticlet Counter. Follow the prompts to follow to successfully book your concert ticket for your artist of choice. \n")

# Ask user for their name
user_name = input("Please enter your name: ")

# Ask user for the band/artist they want to see
band_artist = input("Please enter the name of the band/artist you want to see: ")

# Print formatted string using collected information
print(f"Hey {user_name.title()}! Your ticket to see {band_artist.title()} is booked successfully! Enjoy the show.")
