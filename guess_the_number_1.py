#Number guessing game, allows user 10 tries

import random

playCount = 0
playGame = True
chosenNumber = random.randint(1, 10)

while playGame:

    playCount += 1
    numberGuess = int(input('Guess a number between 1 and 10.\n'))

    if numberGuess == chosenNumber:
        print("You win!")
        playGame = False
    elif playCount == 10:
        print ("The number was", numberGuess)
        playGame = False
