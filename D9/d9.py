import requests
from functools import reduce


def find_next(seq):
    if all(n == 0 for n in seq):
        return 0
    sub_seq = []
    for i in range(len(seq)-1):
        sub_seq.append(seq[i+1] - seq[i])
    return seq[-1] + find_next(sub_seq)


def find_prev(seq):
    if all(n == 0 for n in seq):
        return 0
    sub_seq = []
    for i in range(len(seq)-1):
        sub_seq.append(seq[i+1] - seq[i])
    return seq[0] - find_prev(sub_seq)


if __name__ == "__main__":
    cookies = {"session": "<Enter session-cookie>"}
    source_string = requests.get("https://adventofcode.com/2023/day/9/input", cookies=cookies)

    # Remove the last \n
    source_string = source_string.text[:-1]
    source = source_string.split("\n")
    sequences = list(map(lambda a: list(map(int, a.split(" "))), source))

# Part 1
    next_values = map(find_next, sequences)
    print(reduce(lambda a, b: a + b, next_values, 0))

# Part 2
    prev_values = map(find_prev, sequences)
    print(reduce(lambda a, b: a + b, prev_values, 0))
