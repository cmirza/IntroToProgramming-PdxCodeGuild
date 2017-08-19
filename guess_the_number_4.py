#Number guessing game, allows unlimited guesses, keeps track of guesses,
#tells user if their previous guess is closer than their last guess

import random

playCount = 0
chosenNumber = random.randint(1, 10)
playGame = True
previousGuess = 0

while playGame:

    playCount += 1
    numberGuess = int(input("Guess a number between 1 and 10.\n"))

    if numberGuess != chosenNumber:

        if abs(numberGuess - chosenNumber) > abs(previousGuess - chosenNumber):
            print("You're getting colder.")
        if abs(numberGuess - chosenNumber) < abs(previousGuess - chosenNumber):
            print("You're getting warmer.")
        previousGuess = numberGuess

    if numberGuess == chosenNumber:
        print("You win! It took you", playCount, "guesses.")
        break
