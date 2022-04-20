import random
from rich import print


DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


class RollDice:
    def __init__(self):
        self.counter = 6

    def user_input(self):
        input_string = int(input("How many dice do you want to roll? [1-6] "))

        if input_string in [1, 2, 3, 4, 5, 6]:
            return input_string
        else:
            print("Please enter a number from 1 to 6.")
            raise SystemExit(1)

    def roll_dice(self, num_dice):
        """Return a list of integers with length `num_dice`.

        Each integer in the returned list is a random number between
        1 and 6, inclusive.
        """
        roll_results = []
        for _ in range(num_dice):
            roll = random.randint(1, 6)
            roll_results.append(roll)
        self.counter -= 1
        return roll_results

    def print_dice(self, dice_values):
        """Return an ASCII diagram of dice faces from `dice_values`.

        The string returned contains an ASCII representation of each die.
        For example, if `dice_values = [4, 1, 3, 2]` then the string
        returned looks like this:

        ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
        ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
        │  ●   ●  │ │         │ │  ●      │ │  ●      │
        │         │ │    ●    │ │    ●    │ │         │
        │  ●   ●  │ │         │ │      ●  │ │      ●  │
        └─────────┘ └─────────┘ └─────────┘ └─────────┘
        """
        # Generate a list of dice faces from DICE_ART
        dice_faces = []
        for value in dice_values:
            dice_faces.append(DICE_ART[value])

        # Generate a list containing the dice faces rows
        dice_faces_rows = []
        for row_idx in range(DIE_HEIGHT):
            row_components = []
            for die in dice_faces:
                row_components.append(die[row_idx])
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)

        # Generate header with the word "RESULTS" centered
        width = len(dice_faces_rows[0])
        diagram_header = "[bold red]~~~~~ REMAINIING ROLLS: {} ~~~~~ [/]".format(self.counter).center(10)

        dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
        return dice_faces_diagram

    def play(self):
        print("""[bold magenta]
        ~~~~~~~~~~~~~~~ WELCOME TO ROLL DICE ~~~~~~~~~~~~~~~
        ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
        │  ●   ●  │ │         │ │  ●      │ │  ●      │
        │         │ │    ●    │ │    ●    │ │         │
        │  ●   ●  │ │         │ │      ●  │ │      ●  │
        └─────────┘ └─────────┘ └─────────┘ └─────────┘
        [/]""")
        print()

        while True:
            num_dice = self.user_input()
            roll_results = self.roll_dice(num_dice)
            dice_face_diagram = self.print_dice(roll_results)
            print(f"\n{dice_face_diagram}")

            if self.counter == 0:
                break


def main():
    game = RollDice()
    game.play()


if __name__ == '__main__':
    main()
