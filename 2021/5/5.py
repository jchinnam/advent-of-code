#!/usr/bin/env

import collections


def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]

    max_val = 0

    # convert to coords [[x1, y1, x2, y2]]
    coords = []
    for l in lines:
        one, two = l.split(" -> ")[0], l.split(" -> ")[1]
        coord = [int(one.split(",")[0]), int(one.split(",")[1]), int(two.split(",")[0]), int(two.split(",")[1])]

        max_val = max(coord + [max_val]) # update max
        coords.append(coord)

    return coords, max_val


def part_one(coords, max_val):
    # initialize map with zeros
    map = []
    for i in range(max_val + 1):
        map.append([0 for i in range(max_val + 1)])

    # fill map and track
    for coord in coords:

        # horizontal
        if coord[1] == coord[3]:
            xs = [coord[0], coord[2]]
            xs.sort()
            for x in range(xs[0], xs[1] + 1):
                map[x][coord[1]] += 1

        # vertical
        elif coord[0] == coord[2]:
            ys = [coord[1], coord[3]]
            ys.sort()
            for y in range(ys[0], ys[1] + 1):
                map[coord[0]][y] += 1

    c = collections.Counter()
    for row in map:
        c.update(row)

    danger = 0
    for k in c.keys():
        if k >= 2:
            danger += c[k]

    return danger


def part_two(coords, max_val):
    # initialize map with zeros
    map = []
    for i in range(max_val + 1):
        map.append([0 for i in range(max_val + 1)])

    # fill map and track
    for coord in coords:

        # horizontal
        if coord[1] == coord[3]:
            xs = [coord[0], coord[2]]
            xs.sort()
            for x in range(xs[0], xs[1] + 1):
                map[x][coord[1]] += 1

        # vertical
        elif coord[0] == coord[2]:
            ys = [coord[1], coord[3]]
            ys.sort()
            for y in range(ys[0], ys[1] + 1):
                map[coord[0]][y] += 1

        # diagonal
        else:
            x_pos = (coord[2] - coord[0]) >= 0  # figure out if x shift is +/-
            y_pos = (coord[3] - coord[1]) >= 0  # figure out if y shift is +/-

            x, y = coord[0], coord[1]
            for i in range(abs(coord[0] - coord[2]) + 1):
                map[x][y] += 1
                x += 1 if x_pos else -1
                y += 1 if y_pos else -1

    c = collections.Counter()
    for row in map:
        c.update(row)

    danger = 0
    for k in c.keys():
        if k >= 2:
            danger += c[k]

    return danger


coords, max_val = parse_input("input.txt")
print("part one:", part_one(coords, max_val)) # 5373
print("part two:", part_two(coords, max_val)) # 21514
