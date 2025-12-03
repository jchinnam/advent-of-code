#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        ranges = lines[0].split(',')

    return ranges


def part_one(data):
    total = 0

    for d in data:
        ran = d.split('-')
        start, end = ran[0], ran[1]

        # loop through each number in the range
        for num in range(int(start), int(end) + 1):
            length = len(str(num))

            if length % 2 != 0: # if odd num chars, it can't be a perfect repeat
                continue
            else:
                half = int(length / 2)

                # grab first and second halves and compare them
                first = int(str(num)[0:half])
                second = int(str(num)[half:])

                if first == second:
                    total = total + num

    return total


def part_two(data):
    total = 0

    for d in data:
        ran = d.split('-')
        start, end = ran[0], ran[1]

        # loop through each number in the range
        for num in range(int(start), int(end) + 1):
            length = len(str(num))

            if length == 1:
                continue

            # we have to check all the possible # of parts starting with 2 parts
            for parts in range(2, length + 1):
                if length % parts == 0: # if not a perfect split of chars, it can't be a perfect repeat
                    chunk = int(length / parts)
                    split = [str(num)[i:i + chunk] for i in range(0, length, chunk)]

                    # check that all parts of the split are equal
                    if len(set(split)) == 1:
                        total = total + num
                        
                        # we don't want to add the same num multiple times, so exit to the next number in the range
                        break

    return total


data = parse_input("input.txt")
print("part one:", part_one(data))  # 38437576669
print("part two:", part_two(data))  # 49046150754
