import random  # Bring in the random module so we can make random choices for the computer

def play_game():
    choices = ['rock', 'paper', 'scissors']  # These are the possible choices for the game

    while True:  # Keep the game going until the player decides to stop
        # Ask the user for their choice and convert it to lowercase to avoid case-sensitive issues
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # If the user didn't type 'rock', 'paper', or 'scissors', prompt them again
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue  # Go back to the start of the loop and ask again

        # Get a random choice for the computer using random.choice function
        computer_choice = random.choice(choices)

        # Show both choices to the user
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner based on the classic rules of Rock, Paper, Scissors
        if user_choice == computer_choice:
            print("It's a tie!")  # Both choices are the same
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'scissors' and computer_choice == 'paper') or \
                (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")  # User's choice beats the computer's choice
        else:
            print("Computer wins!")  # Computer's choice beats the user's choice

        # Ask if the player wants to play again; if they type anything other than 'yes', we break out of the loop
        if input("Play again? (yes/no): ").lower() != 'yes':
            break

    print("Thanks for playing!")  # End of the game, thank the player

# Start the game by calling the function
play_game()
