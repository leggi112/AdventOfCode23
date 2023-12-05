import requests


def parse_array(array: list) -> int:
    result = 0
    for y in range(len(array)):
        for x in range(len(array[y])):

            result += process_char(array, x, y)
    return result


def is_digit(char: chr) -> bool:
    return '0' <= char <= '9'


def process_char(array: list, x: int, y: int) -> int:

    result = 0
    if is_digit(array[y][x]) or array[y][x] == '.':
        return 0

    result = 0
    result += process_neighbour(array, x - 1, y)
    result += process_neighbour(array, x + 1, y)

    left = process_neighbour(array, x - 1, y - 1)
    mid = process_neighbour(array, x, y - 1)
    right = process_neighbour(array, x + 1, y - 1)

    if left == mid == right:
        result += mid

    elif left == mid:
        result += mid + right

    elif right == mid:
        result += left + right
    else:
        result += left + mid + right

    left = process_neighbour(array, x - 1, y + 1)
    mid = process_neighbour(array, x, y + 1)
    right = process_neighbour(array, x + 1, y + 1)

    if left == mid == right:
        result += mid

    elif left == mid:
        result += mid + right

    elif right == mid:
        result += left + right
    else:
        result += left + mid + right

    return result


def process_neighbour(array: list, x: int, y: int) -> int:

    if not 0 <= y < len(array) or not 0 <= x < len(array[y]):
        return 0

    if array[y][x] == '.':
        return 0

    if is_digit(array[y][x]):
        value_str = get_int_string(array, x, y)
        return int(value_str)


def get_int_string(array: list, x: int, y: int):
    if not 0 <= y < len(array) or not 0 <= x < len(array[y]):
        return "0"
    return parse_to_left(array, x  - 1, y) + array[y][x] + parse_to_right(array, x + 1, y)


def parse_to_left(array: list, x: int, y: int):
    if not 0 <= y or not 0 <= x:
        return ""

    if not is_digit(array[y][x]):
        return ""

    return parse_to_left(array, x-1, y) + array[y][x]


def parse_to_right(array: list, x: int, y: int):
    if not y < len(array) or not x < len(array[y]):
        return ""
    if not is_digit(array[y][x]):
        return ""

    return parse_to_right(array, x + 1, y) + array[y][x]


if __name__ == "__main__":
    cookies = {"session": "<Enter session-cookie>"}
    source = requests.get("https://adventofcode.com/2023/day/3/input", cookies=cookies)
    part_list = source.text.split("\n")
    part_list = part_list[:-1]

    array = list(map(lambda a: list(a), part_list))
    print(parse_array(array))
