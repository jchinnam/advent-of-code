#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        data = file.readlines()
        crabs = data[0].strip()

    crabs = crabs.split(",")
    crabs = [int(c) for c in crabs]

    return crabs


def part_one(crabs):
    min_pos = min(crabs)
    max_pos = max(crabs)

    min_fuel = float('inf')
    for pos in range(min_pos, max_pos + 1):
        fuel = 0
        for c in crabs:
            fuel += abs(pos - c)
        min_fuel = min(min_fuel, fuel)

    return min_fuel


def part_two(crabs):
    min_pos = min(crabs)
    max_pos = max(crabs)

    min_fuel = float('inf')
    for pos in range(min_pos, max_pos + 1):
        fuel = 0
        for c in crabs:
            n = abs(pos - c)
            fuel += (n * (n + 1) // 2)
        min_fuel = min(min_fuel, fuel)

    return min_fuel


crabs = parse_input("input.txt")
print("part one:", part_one(crabs)) # 344297
print("part two:", part_two(crabs)) # 97164301
