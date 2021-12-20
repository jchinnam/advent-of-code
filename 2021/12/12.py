#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]
        lines = [l.split('-') for l in lines]

    cave_system = {} # map from cave : everywhere you can reach from that cave
    for line in lines:
        # add forward path 0->1
        if line[0] in cave_system:
            cave_system[line[0]].append(line[1])
        else:
            cave_system[line[0]] = [line[1]]

        # add backward path 0<-1
        if line[1] in cave_system:
            cave_system[line[1]].append(line[0])
        else:
            cave_system[line[1]] = [line[0]]

    cave_system.pop('end')

    return cave_system


def valid_one(path):
    small_caves = []
    for cave in path:
        if cave.islower():
            small_caves.append(cave)

    return len(set(small_caves)) == len(small_caves)


def dfs_one(cave_system, paths, p):
    if p[-1] == 'end': # base case: reached the end
        paths.append(p)
        return

    for next in cave_system[p[-1]]:
        if valid_one(p + [next]): # verify small caves are only visited once
            dfs_one(cave_system, paths, p + [next])


def part_one(cave_system):
    paths = []

    dfs_one(cave_system, paths, ['start'])

    return len(paths)


def valid_two(path): # Verify any small caves are only present once.
    if len(path) > 1 and path[-1] == 'start': # do not allow us to return to start
        return False

    small_caves = []
    for cave in path:
        if cave.islower():
            small_caves.append(cave)

    return len(set(small_caves)) == len(small_caves) or len(set(small_caves)) + 1 == len(small_caves)


def dfs_two(cave_system, paths, p):
    if p[-1] == 'end': # base case: reached the end
        paths.append(p)
        return

    for next in cave_system[p[-1]]:
        if valid_two(p + [next]): # verify small caves are only visited once (with one exception)
            dfs_two(cave_system, paths, p + [next])


def part_two(cave_system):
    paths = []

    dfs_two(cave_system, paths, ['start'])

    return len(paths)


cave_system = parse_input("input.txt")
print("part one:", part_one(cave_system)) # 4775
print("part two:", part_two(cave_system)) # 152480
