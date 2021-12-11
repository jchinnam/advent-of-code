#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [list(l.rstrip()) for l in lines]

    return lines


def part_one(data):
    match = {')':'(','}':'{', ']':'[', '>': '<'}
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

    points = 0
    for line in data:
        stack = []
        for i in range(len(line)):
            char = line[i]

            if char == '(' or char == '{' or char == '[' or char == '<': # if start append, can't match
                stack.append(char)
            elif len(stack) != 0 and stack[-1] == match[char]: # if top is match, pop stack
                stack.pop()
            else:
                points += scores[char] # corrupted
                break # exit this line

    return points


def part_two(data):
    close_to_open = {')':'(','}':'{', ']':'[', '>': '<'}
    open_to_close = {'(':')','{':'}', '[':']', '<': '>'}
    scores = {')': 1, ']': 2, '}': 3, '>': 4}

    points_all = []
    for line in data:
        stack = []
        points = 0
        corrupted = False
        for i in range(len(line)):
            char = line[i]

            if char == '(' or char == '{' or char == '[' or char == '<': # if start append, can't match
                stack.append(char)
            elif len(stack) != 0 and stack[-1] == close_to_open[char]: # if top is match, pop stack
                stack.pop()
            else:
                corrupted = True # corrupted, exit this line
                break

        # if stack not empty when loop completes, it is incomplete
        if not corrupted and len(stack) != 0:

            # build completion string and calculate points
            while len(stack) > 0:
                char = stack.pop()
                points *= 5
                points += scores[open_to_close[char]]

            points_all.append(points)

    points_all.sort()

    return points_all[len(points_all) // 2]


data = parse_input("input.txt")
print("part one:", part_one(data)) # 394647
print("part two:", part_two(data)) # 2380061249
