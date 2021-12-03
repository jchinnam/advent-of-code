#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        dirs = file.readlines()
        dirs = [d.rstrip() for d in dirs]

    return dirs


def part_one(dirs):
    # forward: horiz + X
    # down: depth + X
    # up: depth - X

    horiz = 0
    depth = 0
    for d in dirs:
        direction = d.split()[0]
        val = int(d.split()[1])

        if direction == "forward":
            horiz += val
        elif direction == "down":
            depth += val
        else: # up
            depth -= val

    return horiz * depth


def part_two(dirs):
    # forward: horiz + X, depth + aim*X
    # down: aim + X
    # up: aim - X

    horiz = 0
    depth = 0
    aim = 0
    for d in dirs:
        direction = d.split()[0]
        val = int(d.split()[1])

        if direction == "forward":
            horiz += val
            depth += aim * val
        elif direction == "down":
            aim += val
        else: # up
            aim -= val

    return horiz * depth


data = parse_input("input.txt")
print("part one:", part_one(data)) # 1989265
print("part two:", part_two(data)) # 2089174012
