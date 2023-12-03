import requests
from functools import reduce


class Game:

    def __init__(self, input_string: str, bag_content: dict):

        self.id = 0
        self.sets = []
        self.valid = False
        self.bag_content = bag_content

        self.process_input(input_string)

    def process_input(self, string: str):
        split_string = string.split(": ")
        split_string[0] = split_string[0].replace("Game ", "")
        try:
            self.id = int(split_string[0])
        except ValueError:
            return

        self.valid = True
        self.sets = split_string[1].split("; ")

    def evaluate_game(self) -> bool:
        if not self.valid:
            return False

        for set in self.sets:
            colors = set.split(", ")
            for color in colors:
                kv = color.split(" ")
                key = kv[1]
                count = int(kv[0])

                if key not in self.bag_content.keys():
                    return False

                elif count > self.bag_content[key]:
                    return False
        return True


if __name__ == "__main__":
    content = {"red": 12, "green": 13, "blue": 14}

    cookies = {"session": "<Enter session-cookie>"}
    source = requests.get("https://adventofcode.com/2023/day/2/input", cookies=cookies)
    part_list = source.text.split("\n")

    games = list(map(lambda string: Game(string, content), part_list))
    valid_games = list(filter(lambda g: g.evaluate_game(), games))
    valid_game_ids = list(map(lambda g: g.id, valid_games))
    print(reduce(lambda a, b: a+b, valid_game_ids, 0))

