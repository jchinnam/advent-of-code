#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]

    return lines


def part_one(data):
    i = 50 # dial starts at 50
    zeroes = 0 # count for how many times we landed on 0

    for d in data:
        direction = d[0]
        shift = int(d[1:])
        remainder = int(shift) % 100 # full rotation is 100 clicks
    
        if direction == "L": # left
            target = i - remainder

            if target >= 0: # can never be >99 if we start 0-99 and go left
                i = target
            else: # target < 0 -> we need to loop
                i = 100 + target

        else: # right
            target = i + remainder

            if target <= 99: # can never be negative if we start 0-99 and go right
                i = target
            else: # target > 99 -> we need to loop
                i = target - 100

        if i == 0:
            zeroes = zeroes + 1

    return zeroes


def part_two(data):
    i = 50 # dial starts at 50
    zeroes = 0 # count for how many times we landed on 0

    for d in data:
        start = i
        direction = d[0]
        shift = int(d[1:])
        remainder = int(shift) % 100 # full rotation is 100 clicks
    
        if direction == "L": # left
            target = i - remainder

            if target >= 0: # can never be >99 if we start 0-99 and go left
                i = target
            else: # target < 0 -> we need to loop
                i = 100 + target
                if start != 0 and i != 0: # if loop we want to increment zeroes, but if we start or end at 0, we don't want to double count
                    zeroes = zeroes + 1


        else: # right
            target = i + remainder

            if target <= 99: # can never be negative if we start 0-99 and go right
                i = target
            else: # target > 99 -> we need to loop
                i = target - 100
                if start != 0 and i != 0: # if loop we want to increment zeroes, but if we start or end at 0, we don't want to double count
                    zeroes = zeroes + 1

        if i == 0:
            zeroes = zeroes + 1
    
        # add any full loops we took which would have each crossed 0
        loops = int(shift) // 100
        zeroes = zeroes + loops

    return zeroes


data = parse_input("input.txt")
print("part one:", part_one(data))  # 1158
print("part two:", part_two(data))  # 6860
