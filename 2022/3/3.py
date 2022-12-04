#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]

    return lines


def calculate_priority(element):
    if element.islower():
        return (ord(element) - 96)  # - 97 (ascii value for 'a') + 1
    else:
        return (ord(element) - 38)  # - 65 (ascii value for 'A') + 27

    

def part_one(data):
    priorities = 0

    for rucksack in data:
        i = int(len(rucksack) / 2)
        elf1 = set(rucksack[:i])
        elf2 = set(rucksack[i:])

        intersection = elf1.intersection(elf2)
        element = intersection.pop()

        priorities += calculate_priority(element)

    return priorities


def part_two(data):
    priorities = 0

    for i in range(0, len(data), 3):
        elf1 = set(data[i])
        elf2 = set(data[i + 1])
        elf3 = set(data[i + 2])

        intersection = elf1 & elf2 & elf3
        element = intersection.pop()

        priorities += calculate_priority(element)
        
    return priorities


data = parse_input("input.txt")
print("part one:", part_one(data))  # 8085
print("part two:", part_two(data))  # 2515
