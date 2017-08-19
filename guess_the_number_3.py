#Number guessing game, allows unlimited guesses, keeps track of guesses,
#tells user if their guess is too high or low

import random

playCount = 0
chosenNumber = random.randint(1, 10)
playGame = True

while playGame:

    playCount += 1
    numberGuess = int(input("Guess a number between 1 and 10.\n"))

    if numberGuess > chosenNumber:
        print("Too high.")
    if numberGuess < chosenNumber:
        print("Too low.")

    if numberGuess == chosenNumber:
        print("You win! It took you", playCount, "guesses.")
        break
