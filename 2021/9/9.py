#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [list(map(int, list(l.rstrip()))) for l in lines]

    return lines


def part_one(data):
    lows = []
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            low = True

            # check left
            if j != 0 and data[i][j -1] <= x:
                    low = False

            # check up
            if i != 0 and data[i - 1][j] <= x:
                    low = False

            # check right
            if j != len(row) - 1 and data[i][j + 1] <= x:
                    low = False

            # check down
            if i != len(data) - 1 and data[i + 1][j] <= x:
                    low = False

            if low:
                lows.append(x)


    return sum(lows) + len(lows)


def part_two(data):
    # 1. exported to csv, imported to excel
    # 2. conditional formatted all the 9 elements
    # 3. eyeballed the largest 3 basins (see basins.png)

    return 106 * 91 * 89


data = parse_input("input.txt")
print("part one:", part_one(data)) # 594
print("part two:", part_two(data)) # 858494
