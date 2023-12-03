import requests
from functools import reduce


def sanitize_string(string: str) -> list:
    values = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = string
    for i in range(len(values)):
        result = result.replace(values[i], values[i][0] + str(i+1) + values[i][-1])
    return result


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

    part_list = list(map(sanitize_string, part_list))
    cal_values = list(map(isolate_calibration, part_list))
    print(reduce(lambda a, b: a+b, cal_values, 0))
