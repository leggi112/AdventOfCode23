import requests


def find_start(lab):
    for y in range(len(lab)):
        for x in range(len(lab[y])):
            if lab[y][x] == "S":
                return x, y


def find_direction_from_start(lab, x, y):
    # Top
    n_y = y-1
    if 0 < n_y < len(lab):
        if lab[n_y][x] in ['|', '7', 'F']:
            return 0

    # Left
    n_x = x - 1
    if 0 < n_x < len(lab[y]):
        if lab[y][n_x] in ['-', 'F', 'L']:
            return 3

    # Right
    n_x = x + 1
    if 0 < n_x < len(lab[y]):
        if lab[y][n_x] in ['-', 'J', '7']:
            return 1

    # Bottom
    n_y = y + 1
    if 0 < n_y < len(lab):
        if lab[n_y][x] in ['|', 'J', 'L']:
            return 2
    return -1


def match_element(element, direction):
    match element:
        case '|':
            return direction
        case '-':
            return direction
        case 'L':
            return 1 if direction == 2 else 0
        case 'J':
            return 3 if direction == 2 else 0
        case 'F':
            return 1 if direction == 0 else 2
        case '7':
            return 3 if direction == 0 else 2
        case 'S':
            return direction


def find_next(lab, curr):
    x, y, d = curr
    d = match_element(lab[y][x], d)
    match d:
        case 0:
            return x, y-1, d
        case 1:
            return x+1, y, d
        case 2:
            return x, y+1, d
        case 3:
            return x-1, y, d


def trace_path(lab, start_point):
    start_x = start_point[0]
    start_y = start_point[1]
    current = find_next(lab, start_point)
    i = 1
    while current[0] != start_x or current[1] != start_y:
        current = find_next(lab, current)
        i += 1
    return i


if __name__ == "__main__":
    cookies = {"session": "<Enter session-cookie>"}
    source_string = requests.get("https://adventofcode.com/2023/day/10/input", cookies=cookies)

    # Remove the last \n
    source_string = source_string.text[:-1]
    labyrinth = source_string.splitlines()
    labyrinth = list(map(list, labyrinth))
    s = find_start(labyrinth)
    start = (*s, find_direction_from_start(labyrinth, *s))
    print(start)

    steps = trace_path(labyrinth, start)
    print(steps//2 if steps % 2 == 0 else steps//2 + 1)
