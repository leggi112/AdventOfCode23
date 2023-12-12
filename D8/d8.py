import requests
import math


class Node:

    def __init__(self, name):
        self.name = name
        self.left = self
        self.right = self

    def __str__(self):
        return self.name


if __name__ == "__main__":
    cookies = {"session": "<Enter session-cookie>"}
    source_string = requests.get("https://adventofcode.com/2023/day/8/input", cookies=cookies)

    # Remove the last \n
    source_string = source_string.text[:-1]

    source = source_string.split("\n")
    inputs = source.pop(0)
    source.pop(0)

    node_dict = {}

    source = list(map(lambda a: a.replace(" ", "").split("="), source))

    for node, unused in source:
        node_dict[node] = Node(node)

    for node, children in source:
        ch = children.replace("(", "").replace(")", "").split(",")
        left = ch[0]
        right = ch[1]

        node_dict[node].left = node_dict[left]
        node_dict[node].right = node_dict[right]

    current = node_dict["AAA"]
    counter = 0
    outer_flag = True

    while outer_flag:
        for step in inputs:
            if current.name == "ZZZ":
                outer_flag = False
                break

            if step == "L":
                current = current.left

            elif step == "R":
                current = current.right

            counter += 1
    print(f"Task 1: {counter}")

# Part 2
    current_nodes = [node_dict[node] for node in node_dict.keys() if node[-1] == 'A']
    counters = []
    for node in current_nodes:
        current = node
        counter = 0
        outer_flag = True

        while outer_flag:
            for step in inputs:
                if current.name[-1] == 'Z':
                    outer_flag = False
                    break

                if step == "L":
                    current = current.left

                elif step == "R":
                    current = current.right

                counter += 1
        counters.append(counter)
    print(f"Task 2: {math.lcm(*counters)}")
