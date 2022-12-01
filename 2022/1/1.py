#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]

    lines.append('')
    return lines


def part_one(data):
    max_calories = 0

    current_calories = 0
    for l in data:
        if l == '':  # starting a new elf
            max_calories = max(max_calories, current_calories)
            current_calories = 0
        else:
            current_calories += int(l)

    return max_calories


def part_two(data):
    max_calories_1 = max_calories_2 = max_calories_3 = 0  # 1 is highest, 3 is lowest

    current_calories = 0
    for l in data:
        if l == '':  # starting a new elf
            if current_calories > max_calories_1:
                max_calories_3 = max_calories_2
                max_calories_2 = max_calories_1
                max_calories_1 = current_calories
            elif current_calories > max_calories_2:
                max_calories_3 = max_calories_2
                max_calories_2 = current_calories
            elif current_calories > max_calories_3:
                max_calories_3 = current_calories
            current_calories = 0
        else:
            current_calories += int(l)

    return max_calories_1 + max_calories_2 + max_calories_3


data = parse_input("input.txt")
print("part one:", part_one(data))  # 72478
print("part two:", part_two(data))  # 210367