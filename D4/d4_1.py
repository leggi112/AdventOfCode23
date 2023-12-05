import requests
from functools import reduce


class Game:

    def __init__(self, input_string: str):

        self.winning_numbers = []
        self.game_numbers = []

        self.parse_input(input_string)

    def parse_input(self, string):
        numbers = string.split(": ")[1]

        numbers = numbers[1:] if numbers[0] == " " else numbers
        numbers = numbers.replace("  ", " ")

        split_numbers = numbers.split(" | ")
        self.winning_numbers = list(map(lambda a: int(a), split_numbers[0].split(" ")))
        self.game_numbers = list(map(lambda a: int(a), split_numbers[1].split(" ")))

    def evaluate(self):
        numbers = list(filter(lambda a: a in self.winning_numbers, self.game_numbers))
        if len(numbers) == 0:
            return 0

        return 2 ** (len(numbers) - 1)


if __name__ == "__main__":
    cookies = {"session": "<Enter session-cookie>"}

    source = requests.get("https://adventofcode.com/2023/day/4/input", cookies=cookies)
    part_list = source.text.split("\n")
    part_list = part_list[:-1]

    games = list(map(lambda s: Game(s), part_list))

    scores = list(map(lambda g: g.evaluate(), games))
    print(reduce(lambda a, b: a+b, scores))

