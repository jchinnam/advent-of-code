#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip().split() for l in lines]

    return lines


def update_strength(signal_strength_sum, cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength_sum += (cycle * x)

    return signal_strength_sum


def part_one(data):
    signal_strength_sum = 0

    cycle = 1
    x = 1

    for d in data:
        if d[0] == 'noop':
            cycle += 1
            # finish noop
            signal_strength_sum = update_strength(signal_strength_sum, cycle, x)
        elif d[0] == 'addx':
            cycle += 1
            signal_strength_sum = update_strength(signal_strength_sum, cycle, x)
            cycle += 1
            x += int(d[1])  # finish add
            signal_strength_sum = update_strength(signal_strength_sum, cycle, x)
            
    return signal_strength_sum


# reset cycle from 41 to 1 to shift down a row in the crt image
def check_cycle(cycle):
    if cycle == 41:
        return 1
    else:
        return cycle


def get_pixel(crt_position, sprite_position):
    if crt_position in sprite_position:
        return '#'
    else:
        return '.'
            

def part_two(data):
    crt = []

    cycle = 1  # crt position is cycle - 1
    x = 1  # center of sprite, i.e. right now sprite is at [0, 1, 2]

    for d in data:
        if d[0] == 'noop':
            crt.append(get_pixel(cycle - 1, [x - 1, x, x + 1]))  # draw
            cycle += 1
            # finish noop
            cycle = check_cycle(cycle)
        elif d[0] == 'addx':
            crt.append(get_pixel(cycle - 1, [x - 1, x, x + 1]))  # draw
            cycle += 1
            cycle = check_cycle(cycle)
            crt.append(get_pixel(cycle - 1, [x - 1, x, x + 1]))  # draw
            cycle += 1
            x += int(d[1])  # finish add
            cycle = check_cycle(cycle)

    # print out crt image
    print(crt[0:39])    
    print(crt[40:79])
    print(crt[80:119])
    print(crt[120:159])
    print(crt[160:199])
    print(crt[200:239])
    
    return 'see image above'


data = parse_input("input.txt")
print("part one:", part_one(data))  # 14820
print("part two:", part_two(data))  # RZEKEFHA
