#!/usr/bin/env

from itertools import combinations

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        banks = [l.rstrip() for l in lines]

    return banks


def part_one(data):
    joltage = 0

    for bank in data:

        highest = -1
        for i in range(0, len(bank) - 1): # exclusive & first digit can't be last number in bank
            for j in range(i + 1, len(bank)): # exclusive & second digit can go all the way to last number in bank
                num = str(bank[i]) + str(bank[j])
                highest = max(highest, int(num))

        joltage = joltage + highest

    return joltage


def part_two(data):
    joltage = 0

    for bank in data:
        stack = [] # greedy algo, here we go
        n = len(bank)

        for i, c in enumerate(bank):
            # Remove smaller digits from the end if enough digits remain
            # len(stack) = what we have so far
            # n - i = how many digits are left to look at
            while stack and len(stack) + (n - i) > 12 and stack[-1] < c:
                stack.pop()
            if len(stack) < 12:
                stack.append(c)

        # Convert stack to integer and add to total joltage
        joltage += int(''.join(stack))

            
    return joltage


data = parse_input("input.txt")
print("part one:", part_one(data))  # 17207
print("part two:", part_two(data))  # 170997883706617
