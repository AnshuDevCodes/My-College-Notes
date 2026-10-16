# Number Guessing Game

import random

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 10)

    def play(self):
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == self.number:
            print("Congratulations! You guessed correctly.")
        elif guess < self.number:
            print("Your guess is too low.")
            print("The correct number was:", self.number)
        else:
            print("Your guess is too high.")
            print("The correct number was:", self.number)


# Creating an object
game = GuessingGame()
game.play()


OUTPUT
Guess a number between 1 and 10: 5
Your guess is too low.
The correct number was: 8
