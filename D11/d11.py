from functools import reduce
import aoc_utils


def transpose(array):
    result = [[] for _ in range(len(array[0]))]
    for height, row in enumerate(array):
        for width, element in enumerate(row):
            result[width].append(element)
    return result


def expand_universe(u):
    result = []
    for height, line in enumerate(u):
        result.append(line)
        if '#' not in line:
            result.append(line)
    return result


def shortest_path(p, coords):

    start = coords[p[0]]
    end = coords[p[1]]
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def get_empty_lines(u):
    result = []

    for k, row in enumerate(u):
        if '#' not in row:
            result.append(k)

    return result


def get_expanded_coords(coords, factor, gap_list):
    result = {}
    for key, value in coords.items():
        result[key] = [*value]

    for g in gap_list[0]:
        for key, value in coords.items():
            if value[1] > g:
                result[key][1] += 1 * factor - 1

    for g in gap_list[1]:
        for key, value in coords.items():
            if value[0] > g:
                result[key][0] += 1 * factor - 1
    return result


if __name__ == '__main__':
    source_string = aoc_utils.get_puzzle_string(11)
    source_string = source_string.splitlines()

    universe = list(map(lambda a: list(a), source_string))
    gaps = []
    for i in range(2):
        gaps.append(get_empty_lines(universe))
        universe = transpose(universe)

    i = 1
    coordinates = {}
    for y, line in enumerate(universe):
        for x, element in enumerate(line):
            if element == '#':
                universe[y][x] = i
                coordinates[i] = (x, y)
                i += 1

    expanded_coordinates_1 = get_expanded_coords(coordinates, 2, gaps)

    pairs = []
    for x in range(1, i - 1):
        for y in range(x, i):
            if x == y:
                continue
            pairs.append((x, y))

    print("Task 1:", reduce(lambda a, b: a + b, map(lambda a: shortest_path(a, expanded_coordinates_1), pairs)))

    expanded_coordinates_2 = get_expanded_coords(coordinates, 1_000_000, gaps)

    print("Task 2:", reduce(lambda a, b: a + b, map(lambda a: shortest_path(a, expanded_coordinates_2), pairs)))
