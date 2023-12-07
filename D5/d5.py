import requests
from multiprocessing import Pool
import time
from functools import reduce


def rule_from_string(string):
    d, s, l = tuple(map(int, string.split(" ")))
    return Rule(d, s, l)


class Rule:

    def __init__(self,dest, source, length):

        self.dest = dest
        self.source = source
        self. length = length

    def execute(self, n: int):
        temp = n - self.source
        if 0 <= temp < self.length:
            return self.dest + temp
        return n


class Mapper:

    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def execute(self, n: int):
        for rule in self.rules:
            current = rule.execute(n)
            if current != n:
                return current
        return n


def create_maps(prt_list):
    mings = {}
    mers = {}

    for part in prt_list:
        m = part.split("\n")

        s, f, dest = m.pop(0).replace(" map:", "").split("-")
        mings[s] = dest
        mers[dest] = Mapper()

        for rule_string in m:
            mers[dest].add_rule(rule_from_string(rule_string))

    return mings, mers


def mapping_for_valuelist(input_values, start, mings: dict, mers: dict):

    current = start
    current_values = input_values
    new_values = []
    while current in mings.keys():

        for i, src in enumerate(current_values):
            new_values.append(mers[mings[current]].execute(src))

        current_values = new_values
        new_values = []
        current = mings[current]

    return current_values


def mapping_for_value(input_value, start, mings: dict, mers: dict):

    current = start
    current_value = input_value

    while current in mings.keys():
        new_value = mers[mings[current]].execute(current_value)

        current_value = new_value
        current = mings[current]

    return current_value


def mapping_lowest_in_range(task_index, start_value, range_value, start, mings: dict, mers: dict):
    result = 2**30
    for i in range(range_value):
        x = start_value + i
        n = mapping_for_value(x, start, mings, mers)
        if n < result:
            result = n
    print(f"Process {task_index}: {(start_value, range_value)} finished!")
    return result


class Worker:

    def __init__(self, start, ming, mers):
        self.start = start
        self.mappings = ming
        self.mappers = mers

    def work(self, inp):
        return mapping_lowest_in_range(inp[0], inp[1], inp[2], self.start, self.mappings, self.mappers)


def normalize_inputs(inp, chunk_size=1_000_000):
    res = []
    index = 0
    for part in inp:
        i, start, _range = part
        if _range <= chunk_size:
            res.append((index, start, _range))
            index += 1
        else:
            while _range > chunk_size:
                res.append((index, start, chunk_size))
                index += 1
                start += chunk_size
                _range -= chunk_size

            res.append((index, start, _range))
            index += 1

    return res


if __name__ == "__main__":

    cookies = {"session": "<Enter session-cookie>"}
    source_string = requests.get("https://adventofcode.com/2023/day/5/input", cookies=cookies)

    # Remove the last \n
    source_string = source_string.text[:-1]


# Part 1
    part_list = source_string.split("\n\n")
    seed_string = part_list.pop(0)
    seeds = list(map(int, seed_string.replace("seeds: ", "").split(" ")))
    mappings, mappers = create_maps(part_list)
    results = mapping_for_valuelist(seeds, "seed", mappings, mappers)

    print("Task 1:", min(results), end="\n\n")


# Part 2
    vals = list(map(int, seed_string.replace("seeds: ", "").split(" ")))
    inputs = []
    for v in range(0, len(vals), 2):
        inputs.append((v//2, vals[v], vals[v+1]))
    inputs = normalize_inputs(inputs)

    print(f"Starting {len(inputs)} processes")

    p = Pool(12)
    w = Worker("seed", mappings, mappers)
    s_time = time.time()
    with p:
        r = p.map(w.work, inputs)
    print(f"Task 2:", min(r))
