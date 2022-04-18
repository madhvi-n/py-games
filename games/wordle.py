import random
from rich import print
from collections import defaultdict


words = [
    "awake",
    "blush",
    "focal",
    "evade",
    "serve",
    "grade",
    "quiet",
    "ocean",
    "dream",
    "drawn",
    "rapid",
    "pitch",
    "reverie",
    "moonlight"
]


class Wordle:
    def __init__(self):
        self.word = random.choice(words)
        self.length = len(self.word)
        self.num_guesses = self.length
        self.guess_dict = defaultdict(list)
        self.guess_dict.update((k, [" "] * self.length) for k in range(self.length))

    def draw(self):
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("----" * (self.length - 1))
        print()

    def user_input(self):
        print(f"Guesses remaining: {self.num_guesses}")
        user_guess = input(f"Enter a {self.length} letter word: ")

        while len(user_guess) != self.length:
            user_guess = input(f"Invalid input. Enter a {self.length} letter word: ")

        user_guess = user_guess.lower()
        for index, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[index]:
                    char = f"[magenta]{char.upper()}[/]"
                else:
                    char = f"[yellow]{char}[/]"
            self.guess_dict[self.length - self.num_guesses][index] = char

        self.num_guesses -= 1
        return user_guess

    def play(self):
        print(f"[bold magenta]Welcome to Wordle![/]")
        print(f"[bold magenta]Chosen word is a {self.length} letter word. You have {self.length} guesses[/] \n")

        while True:
            self.draw()
            user_guess = self.user_input()
            print()

            if user_guess == self.word:
                self.draw()
                print(f"[bold green]You won. The word was {self.word}[/]")
                break

            if self.num_guesses == 0:
                self.draw()
                print(f"[bold red]You lost! The word was {self.word}[/]")
                break


def main():
    game = Wordle()
    game.play()


if __name__ == '__main__':
    main()
