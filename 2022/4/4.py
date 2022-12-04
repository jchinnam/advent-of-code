#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [(l.rstrip()).split(',') for l in lines]

    print(lines)
    return lines


def part_one(data):
    overlaps = 0  # full overlaps

    for pair in data:
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')

        if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):  # does elf1 cover all of elf2
            overlaps += 1
            print('OVERLAP:', elf1, elf2)
        elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):  # does elf2 cover all of elf1
            overlaps += 1
            print('OVERLAP:', elf1, elf2)

    return overlaps


def part_two(data):
    overlaps = 0  # partial overlaps

    for pair in data:
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')

        if int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1]):  # elf1[0] <= elf2[0] <= elf1[1]
            overlaps += 1
        elif int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]):  # elf2[0] <= elf1[0] <= elf2[1]
            overlaps += 1

    return overlaps


data = parse_input("input.txt")
print("part one:", part_one(data))  # 542
print("part two:", part_two(data))  # 900
