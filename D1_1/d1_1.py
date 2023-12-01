import requests
from functools import reduce


def is_digit(char: chr) -> bool:
    return '0' <= char <= '9'


def isolate_calibration(input_string: str) -> int:
    first = last = None
    for i in input_string:
        if is_digit(i):
            if first is None:
                first = int(i)

            last = int(i)

    if first is None:
        return 0

    return first * 10 + last


if __name__ == "__main__":
    cookies = {"session": "<Enter session-cookie>"}
    source = requests.get("https://adventofcode.com/2023/day/1/input", cookies=cookies)
    part_list = source.text.split("\n")

    cal_values = list(map(isolate_calibration, part_list))
    print(reduce(lambda a,b: a+b, cal_values, 0))
