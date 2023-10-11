from game_controller import GameController


def main():
    print("--------------------------------")
    print("Welcome to street craps!\n\nRules:\nIf you roll 7 or 11 on your \
first roll, you win.")
    print("If you roll 2, 3, or 12 on your first role, you lose.")
    print("If you roll anything else, that's your 'point', and")
    print("you keep rolling until you either roll your point\nagain (win) or \
roll a 7 (lose)\n")
    gc = GameController()
    input("Press enter to roll the dice...\n")
    gc.start_game()


main()
