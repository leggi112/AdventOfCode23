import requests
from functools import reduce


class Game:

    def __init__(self, input_string: str, card_dict):

        self.id = 0
        self.winning_numbers = []
        self.game_numbers = []

        self.parse_input(input_string)

        card_dict[self.id] = 1

    def parse_input(self, string):
        split_string = string.split(": ")

        self.id = int(split_string[0]. replace("Card", ""))

        numbers = split_string[1]

        numbers = numbers[1:] if numbers[0] == " " else numbers
        numbers = numbers.replace("  ", " ")

        split_numbers = numbers.split(" | ")
        self.winning_numbers = list(map(lambda a: int(a), split_numbers[0].split(" ")))
        self.game_numbers = list(map(lambda a: int(a), split_numbers[1].split(" ")))

    def evaluate(self, card_dict: dict):
        result = len(list(filter(lambda a: a in self.winning_numbers, self.game_numbers)))
        for i in range(1, result+1):
            if self.id + i in card_dict.keys():
                card_dict[self.id + i] += 1
        return result


if __name__ == "__main__":
    cookies = {"session": "<Enter session-cookie>"}

    source = requests.get("https://adventofcode.com/2023/day/4/input", cookies=cookies)

    part_list = source.text.split("\n")
    part_list = part_list[:-1]

    cards = {}

    games = list(map(lambda s: Game(s, cards), part_list))

    for game in games:
        for i in range(cards[game.id]):
            game.evaluate(cards)

    print(reduce(lambda a, b: a+b, cards.values(), 0))
