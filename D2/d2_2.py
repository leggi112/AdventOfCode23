from functools import reduce
import aoc_utils


class Game:

    def __init__(self, input_string: str):
        self.id = 0
        self.sets = []
        self.valid = False

        self.min_bag_content = {}

        self.process_input(input_string)
        self.evaluate_game()

    def process_input(self, string: str):
        split_string = string.split(": ")
        split_string[0] = split_string[0].replace("Game ", "")
        try:
            self.id = int(split_string[0])
        except ValueError:
            return

        self.valid = True
        self.sets = split_string[1].split("; ")

    def evaluate_game(self):
        if not self.valid:
            return

        for set in self.sets:
            colors = set.split(", ")
            for color in colors:
                kv = color.split(" ")
                key = kv[1]
                count = int(kv[0])

                if key in self.min_bag_content.keys():
                    record = self.min_bag_content[key]
                    self.min_bag_content[key] = record if record > count else count
                else:
                    self.min_bag_content[key] = count

    def get_min_bag_content_product(self):
        if not self.valid:
            return 0

        result = 1
        for value in self.min_bag_content.values():
            result *= value
        return result


if __name__ == "__main__":

    source = aoc_utils.get_puzzle_string(2)
    part_list = source.split("\n")

    games = map(lambda string: Game(string), part_list)

    bag_sizes = map(lambda g: g.get_min_bag_content_product(), games)

    print("Task 2:", reduce(lambda a, b: a+b, bag_sizes, 0))
