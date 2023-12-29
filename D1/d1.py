from functools import reduce
import aoc_utils


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
    source = aoc_utils.get_puzzle_string(1)
    part_list = source.split("\n")

    cal_values = map(isolate_calibration, part_list)
    print("Part 1:", reduce(lambda a, b: a+b, cal_values, 0))

    part_list = map(sanitize_string, part_list)
    cal_values = map(isolate_calibration, part_list)
    print("Part 2:", reduce(lambda a, b: a + b, cal_values, 0))
