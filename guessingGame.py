# Set the correct answer for the game
answer = 5

# Ask the user to guess a number between 1 and 10
print("Please guess a number between 1 and 10: ")
guess = int(input())  # Take the user's guess and turn it into a number

# Check if their guess is lower than the answer
if guess < answer:
    print("Please guess higher")  # Tell them to guess a bigger number
    guess = int(input())  # Let them guess again
    # Check if they got it right this time
    if guess == answer:
        print("You got it right!")  # They guessed correctly!
    else:
        print("Sorry, that's incorrect")  # Still wrong

# Check if their guess is higher than the answer
elif guess > answer:
    print("Please guess lower")  # Tell them to guess a smaller number
    guess = int(input())  # Let them guess again
    # Check if they got it right this time
    if guess == answer:
        print("Nice, you did it!")  # They guessed correctly!
    else:
        print("Nope. Not it.")  # Still wrong

# If their first guess was right
else:
    print("You got it!")  # Congrats, they nailed it on the first try!
