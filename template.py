#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]

    return lines


def part_one(data):
    pass


def part_two(data):
    pass


data = parse_input("input.txt")
print("part one:", part_one(data))  #
print("part two:", part_two(data))  #
