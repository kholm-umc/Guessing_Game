# Ken Holm
# Purpose:
#  Guessing Game
#  Randomly choose a number between 1 and 100.
#  Have the player enter a guess
#  Tell the player the guess is high, low, or on the money
#  If high or low, allow another guess
#  Give the player an option to quit at any time
#  Reward the player for a correct guess
#  Tell the player how many guesses it took to guess correctly

# See https://docs.python.org/3/library/random.html#random.randint
from random import randint

# Initialize our variables
someNumber = randint(1, 100)
numberOfGuesses = 0
playerGuess = ""
correctGuess = 0

# Print our instructions
print(f"Guess-a-Number")
print(f"Enter a guess between 1 and 100")
print(f"Guess again if your guess is high or low")
print(f"You can enter the letter 'q' to quit")
print(f"Good luck!")
print()

# Begin our guessing loop
while correctGuess == 0:
    playerGuess = input("What is your guess? ")

    # Is the guess a number?  If so, we can process it as such
    if str.isnumeric(playerGuess):

        # Each time a valid guess is taken, increment our guess
        #  counter
        numberOfGuesses = numberOfGuesses + 1

        # Test for a low guess
        if int(playerGuess) < someNumber:
            print(f"{playerGuess} is too low.  Guess again.")

        # Test for a high guess
        elif int(playerGuess) > someNumber:
            print(f"{playerGuess} is too high.  Guess again.")

        # Woohoo!  Correct guess.  Winner, winner, chicken dinner!
        else:
            print(f"{playerGuess} IS CORRECT!")
            print(f"It took you {numberOfGuesses} guesses.")
            correctGuess = 1

    # If the guess is not a number, does the player want to quit?
    elif playerGuess == "q":
        correctGuess = 1

    # Not a number?  Not quitting?  Remind the player to guess
    #  a number between 1 and 100
    else:
        print(f"Please choose an integer between 1 and 100")

print(f"Game finished")
