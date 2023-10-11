from pair_of_dice import PairOfDice

WIN_NUMBER = [7, 11]
LOSE_NUMBER = [2, 3, 12]
SEVEN = 7


class GameController:

    def start_game(self):
        self.value = PairOfDice()
        self.point = self.value.current_value()
        if self.point in WIN_NUMBER:
            print(f"You rolled {self.point}. You win!")
        elif self.point in LOSE_NUMBER:
            print(f"You rolled {self.point}. You lose.")
        else:
            print(f"Your point is {self.value.current_value()}")
            self.last_round()

    def last_round(self):
        while True:
            self.prompt_to_roll()
            if self.value.current_value() == self.point:
                print(f"You rolled {self.value.current_value()}. You win!")
                break
            elif self.value.current_value() == SEVEN:
                print(f"You rolled {self.value.current_value()}. You lose.")
                break
            print(f"You rolled {self.value.current_value()}.")

    def prompt_to_roll(self):
        input("Press enter to roll the dice...\n")
        self.value.roll_dice()
