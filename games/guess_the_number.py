import random
from rich import print


class GuessNumber:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 5

    def user_input(self):
        number = int(input("Guess the number: "))
        self.guesses -= 1
        return number

    def play(self):
        print("""[bold magenta]
        ~~~~~~~~~~~~~~~ GUESS THE NUMBER ~~~~~~~~~~~~~~~
        [/]""")
        print(f"The number can be anything from range 1 to 100. You have {self.guesses} chances")

        while True:
            num = self.user_input()
            if num > self.number:
                print(f"Guessed number is too high.")

            elif num == self.number // 2:
                print(f"You are halfway there. Do you think you can double it?")

            elif num < self.number:
                print(f"Guessed number is low. Go high.")

            elif num == self.number:
                print(f"You guessed it right! The number was {self.number}")
                break

            if self.guesses == 0:
                print(f"[bold yellow]You lost! The number was {self.number}.\n Good luck next time! :D[/]")
                break


def main():
    game = GuessNumber()
    game.play()


if __name__ == '__main__':
    main()
