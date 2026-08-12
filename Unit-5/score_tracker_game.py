# The program continuously asks the arcade player for their game score

# Welcome message
print("\nWelcome to the high score tracker game. Plkease follow the prompts to be able to see if your current score beat the already-recorded high score\n")

high_score = 100
while True:
    user_input = input("Please enter your game score: ")
    if (user_input.strip().lower() == "stop"):
        print("Game session ended!")
        break
    else: 
        score = int(user_input)
        if (score > high_score):
            print("Wow! That's a new high score!\n")
            high_score = score
        else:
            print("Good try, keep playing!\n")