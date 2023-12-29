import aoc_utils
from d7_1 import Hand


def compare_cards(card1, card2):
    ranks = ["J", "2", "3", "4", "5", "6", "7", "8",
             "9", "T", "Q", "K", "A"]
    rank1 = ranks.index(card1)
    rank2 = ranks.index(card2)
    if rank1 < rank2:
        return -1
    elif rank1 == rank2:
        return 0
    else:
        return 1


class AdoptedHand(Hand):
    def calculate_rank(self):
        values = {}
        for card in self.hand:
            if card in values.keys():
                values[card] += 1
            else:
                values[card] = 1

        if "J" in values.keys():
            j_count = values.pop("J")
            if len(values) == 0:
                return 6

            max_cards = max(values.values())
            for key, val in values.items():
                if val == max_cards:
                    values[key] += j_count
                    break

        if 5 in values.values():
            return 6
        elif 4 in values.values():
            return 5
        elif 3 in values.values() and 2 in values.values():
            return 4
        elif 3 in values.values():
            return 3
        elif len(values.values()) == 3:
            return 2
        elif len(values.values()) == 4:
            return 1
        else:
            return 0

    def compare_hands(self, other):
        for i in range(5):
            x = compare_cards(self.hand[i], other.hand[i])
            if x != 0:
                return x
        return 0


if __name__ == "__main__":
    source_string = aoc_utils.get_puzzle_string(7)
    source_string = source_string.split("\n")

    hand_list = list(map(lambda a: AdoptedHand(a[0], int(a[1])),
                         map(lambda a: a.split(" "), source_string)))
    hand_list = sorted(hand_list)

    result = 0
    for i, hand in enumerate(hand_list):
        result += (i+1) * hand.bid

    print(result)
