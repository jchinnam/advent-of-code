#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        depths = file.readlines()
        depths = [int(d.rstrip()) for d in depths]

    return depths


def part_one(depths):
    increase = 0
    for i, d in enumerate(depths):
        if i == 0: continue

        if d > depths[i - 1]:
            increase += 1

    return increase


def part_two(depths):
    # in comparing the 2 windows, 2 middle values are shared
    # i.e. in [199 200 208 210] it only matters that 210 > 199

    increase = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i - 3]:
            increase += 1

    return increase


data = parse_input("../input/1_sonar_sweep.txt")
print("part one:", part_one(data)) # 1722
print("part two:", part_two(data)) # 1748
