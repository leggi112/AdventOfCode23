from functools import reduce


def calculate_strategy(time, max_time):
    if time > max_time:
        raise ValueError
    return (max_time - time) * time


class Race:

    def __init__(self, time, record):
        self.time = time
        self.record = record

    def possible_strategies(self):
        return list(map(lambda a: calculate_strategy(a, self.time), range(self.time)))

    def record_beating_strategies(self):
        return list(filter(lambda a: a > self.record, self.possible_strategies()))


if __name__ == "__main__":

    # Part 1
    times = [56, 97, 78, 75]
    records = [546, 1927, 1131, 1139]

    races = map(lambda a, b: Race(a, b), times, records)
    winning_strategies = list(map(lambda a: a.record_beating_strategies(), races))
    print(reduce(lambda a, b: a * b, map(len, winning_strategies), 1))


    # Part 2
    race = Race(56977875, 546192711311139)
    print(len(race.record_beating_strategies()))
