LONGEST_PLAYER = 0

class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.bench = []

    def send_to_bench(self, player_name):
        # TODO: Put the player "onto the bench"
        return self.bench.append(player_name)

    def get_from_bench(self):
        # TODO: Return the name of the player who has
        # been on the bench longest.
        return self.bench.pop(LONGEST_PLAYER)

    # TODO: Write the function that will display the
    # current list of players on the bench
    def show_bench(self):
        if len(self.bench) != 0:
            print("The bench currently includes:\n")
            for name in self.bench:
                print(name)
        else:
            print("The bench is empty.")

    # TODO: Write any other methods that might be used
    # by the methods above.
    def cut_player(self, cut_name):
        if cut_name in self.bench:
            self.bench.remove(cut_name)
