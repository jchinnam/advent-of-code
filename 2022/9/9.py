#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()

    instructions = []
    for line in lines:
        instr = line.rstrip().split()
        for i in range(int(instr[1])):
            instructions.append(instr[0])

    return instructions


def move_head(d, head):
    if d == 'L':    # left
        head[0] -= 1
    elif d == 'R':  # right
        head[0] += 1
    elif d == 'U':  # up
        head[1] += 1
    else:           # down
        head[1] -= 1

    return head


# takes in a head [x, y] and a tail [x, y] and adjusts the tail accordingly
def adjust_tail(head, tail):
    # if head is 2 directly up, down, left, or right from tail,
    # tail moves 1 step in that direction so it remains close enough
    # else if the head and tail aren't touching (distance of 2) & not in same row or column
    # tail always moves 1 step diagonally to keep up

    if (head[0] - tail[0]) == 2:    # head 2 R of tail
        tail[0] += 1
        if head[1] > tail[1]:         # head U of tail
            tail[1] += 1
        elif head[1] < tail[1]:       # head D of tail
            tail[1] -= 1
    elif (tail[0] - head[0]) == 2:  # head 2 L of tail
        tail[0] -= 1
        if head[1] > tail[1]:         # head U of tail
            tail[1] += 1
        elif head[1] < tail[1]:       # head D of tail
            tail[1] -= 1
    elif (head[1] - tail[1]) == 2:  # head 2 U of tail
        tail[1] += 1
        if head[0] > tail[0]:         # head R of tail
            tail[0] += 1
        elif head[0] < tail[0]:       # head L of tail
            tail[0] -= 1
    elif (tail[1] - head[1]) == 2:  # head 2 D of tail
        tail[1] -= 1
        if head[0] > tail[0]:         # head R of tail
            tail[0] += 1
        elif head[0] < tail[0]:       # head L of tail
            tail[0] -= 1

    return tail


def part_one(data):
    visited = set()

    head = [0, 0]
    tail = [0, 0]
    visited.add((tail[0], tail[1]))

    for d in data:
        head = move_head(d, head)
        tail = adjust_tail(head, tail)
        visited.add((tail[0], tail[1]))

    return len(visited)


def part_two(data):
    visited = set()

    knots = []
    for i in range(10):
        knots.append([0, 0])

    visited.add((knots[9][0], knots[9][1]))

    for d in data:
        knots[0] = move_head(d, knots[0])
        for i in range(1, 10):
            knots[i] = adjust_tail(knots[i - 1], knots[i])

        visited.add((knots[9][0], knots[9][1]))

    return len(visited)


data = parse_input("input.txt")
print("part one:", part_one(data))  # 6087
print("part two:", part_two(data))  # 2493
