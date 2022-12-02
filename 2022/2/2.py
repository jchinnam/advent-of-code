#!/usr/bin/env


def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [(l.rstrip()).split() for l in lines]

    return lines


def part_one(data):
    # A X ROCK
    # B Y PAPER
    # C Z SCISSORS

    rules = {}  # winner: loser
    rules['A'] = 'Z'
    rules['C'] = 'Y'
    rules['B'] = 'X'

    shape = 0
    outcome = 0

    for game in data:
        opponent = game[0]
        you = game[1]

        # shape
        if you == 'X':
            shape += 1
        elif you == 'Y':
            shape += 2
        else:
            shape += 3

        # outcome
        if rules[opponent] == you:  # you lose
            outcome += 0
        elif ord(you) - 23 == ord(opponent):  # draw
            outcome += 3
        else:  # you win
            outcome += 6
    
    return shape + outcome


def part_two(data):
    # X: LOSE
    # Y: DRAW
    # Z: WIN

    rules = {}  # opponent: [you win, you lose]
    rules['A'] = ['B', 'C']
    rules['C'] = ['A', 'B']
    rules['B'] = ['C', 'A']

    shapes = {}
    shapes['A'] = 1
    shapes['B'] = 2
    shapes['C'] = 3

    you = 0
    outcome = 0

    for game in data:
        opponent = game[0]
        rig = game[1]

        if rig == 'X':  # you lose
            you += shapes[rules[opponent][1]]
            outcome += 0
        elif rig == 'Y':  # draw
            you += shapes[opponent]
            outcome += 3
        else:  # you win
            you += shapes[rules[opponent][0]]
            outcome += 6
        
    return you + outcome


data = parse_input("input.txt")
print("part one:", part_one(data))  # 10310
print("part two:", part_two(data))  # 14859
