#!/usr/bin/env


def parse_input(filename):
    with open(filename) as file:
        data = file.readlines()
        fish = data[0].strip()

    fish = fish.split(",")
    fish = [int(f) for f in fish]

    return fish


def breed_fish(fish, days):
    fish_val_to_count = [0]*9  # index = timer values (0, 1, 2, etc); value = number of fish with that timer

    # read in fish timers
    for f in fish:
        fish_val_to_count[f] += 1

    for i in range(1, days + 1):
        # count how many to spawn
        spawn = fish_val_to_count[0]

        # reduce everyone by 1
        for i in range(1, 9):
            fish_val_to_count[i - 1] = fish_val_to_count[i]

        # reset parent fish timers
        fish_val_to_count[6] += spawn

        # spawn babies
        fish_val_to_count[8] = spawn


    # count total fish
    total = 0
    for c in fish_val_to_count:
        total += c

    return total


def part_one(fish):
    return breed_fish(fish, 80)


def part_two(fish):
    return breed_fish(fish, 256)


fish = parse_input("input.txt")
print("part one:", part_one(fish)) # 390923
print("part two:", part_two(fish)) # 1749945484935
