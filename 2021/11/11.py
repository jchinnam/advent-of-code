#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [list(map(int, list(l.rstrip()))) for l in lines]

    return lines


def trigger_neighbor(data, stack, flashed, coord):
    (i, j) = coord

    if coord not in flashed and coord not in stack:
        data[i][j] += 1
        if data[i][j] > 9:
            stack.append(coord)

    return


def part_one(data):
    flashes = 0

    for step in range(100):
        stack = []

        # all octopus up by 1
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1

                # if a 9, add coords to stack
                if data[i][j] > 9:
                    stack.append((i,j))

        # flash anything > 9
        flashed = []
        while len(stack) > 0:
            (i, j) = stack.pop()
            flashed.append((i,j))
            flashes += 1

            # increase neighbors by 1 as long as they haven't flashed already
            # 1 2 3
            # 4 ! 5
            # 6 7 8
            if i > 0 and j > 0: # pos 1
                trigger_neighbor(data, stack, flashed, (i - 1, j - 1))

            if i > 0: # pos 2
                trigger_neighbor(data, stack, flashed, (i - 1, j))

            if i > 0 and j < len(data[0]) - 1: # pos 3
                trigger_neighbor(data, stack, flashed, (i - 1, j + 1))

            if j > 0: # pos 4
                trigger_neighbor(data, stack, flashed, (i, j - 1))

            if j < len(data[0]) - 1: # pos 5
                trigger_neighbor(data, stack, flashed, (i, j + 1))

            if i < len(data) - 1 and j > 0: # pos 6
                trigger_neighbor(data, stack, flashed, (i + 1, j - 1))

            if i < len(data) - 1: # pos 7
                trigger_neighbor(data, stack, flashed, (i + 1, j))

            if i < len(data) - 1 and j < len(data[0]) - 1: # pos 8
                trigger_neighbor(data, stack, flashed, (i + 1, j + 1))

        # reset flashed
        for (i, j) in flashed:
            data[i][j] = 0

    return flashes


def part_two(data):
    sync = None
    step = 0

    while not sync:
        step += 1
        stack = []

        # all octopus up by 1
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] += 1

                # if a 9, add coords to stack
                if data[i][j] > 9:
                    stack.append((i,j))

        # flash anything > 9
        flashed = []
        while len(stack) > 0:
            (i, j) = stack.pop()
            flashed.append((i,j))

            # increase neighbors by 1 as long as they haven't flashed already
            # 1 2 3
            # 4 ! 5
            # 6 7 8
            if i > 0 and j > 0: # pos 1
                trigger_neighbor(data, stack, flashed, (i - 1, j - 1))

            if i > 0: # pos 2
                trigger_neighbor(data, stack, flashed, (i - 1, j))

            if i > 0 and j < len(data[0]) - 1: # pos 3
                trigger_neighbor(data, stack, flashed, (i - 1, j + 1))

            if j > 0: # pos 4
                trigger_neighbor(data, stack, flashed, (i, j - 1))

            if j < len(data[0]) - 1: # pos 5
                trigger_neighbor(data, stack, flashed, (i, j + 1))

            if i < len(data) - 1 and j > 0: # pos 6
                trigger_neighbor(data, stack, flashed, (i + 1, j - 1))

            if i < len(data) - 1: # pos 7
                trigger_neighbor(data, stack, flashed, (i + 1, j))

            if i < len(data) - 1 and j < len(data[0]) - 1: # pos 8
                trigger_neighbor(data, stack, flashed, (i + 1, j + 1))

        if len(flashed) == 100:
            return step

        # reset flashed
        for (i, j) in flashed:
            data[i][j] = 0


print("part one:", part_one(parse_input("input.txt"))) # 1793
print("part two:", part_two(parse_input("input.txt"))) # 247
