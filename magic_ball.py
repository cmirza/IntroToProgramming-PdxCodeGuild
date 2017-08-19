#Magic 8 Ball game

import random

magic_response = ('It is certain.','It is decidedly so.','Reply hazy try again.', 'Ask again later.', 'Don\'t count on it.', 'My reply is no.')

play = True

while play:

    magic_question = input('Ask the Magic Ball anything!\n')

    magic_answer = random.choice(magic_response)

    print(magic_answer)

    play_again=str(input("Play again? Type 'yes' or 'no': "))
    play_again = play_again.lower()
    if play_again == "no":
        play = False
