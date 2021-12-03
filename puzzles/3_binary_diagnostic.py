#!/usr/bin/env

import numpy as np
import numpy.ma as ma
from scipy import stats


def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [list(l.rstrip()) for l in lines]

    return lines


# converts list of chars representing binary to int
# i.e. ['1', '0'] -> 2
def bin_array_to_int(chars):
    binary = ''.join(chars)
    val = int(binary, 2)

    return val


def part_one(data):
    data = np.array(data)
    modes = stats.mode(data)[0][0]
    modes_opposite = ['1' if m == '0' else '0' for m in modes]

    gamma = bin_array_to_int(modes)
    epsilon = bin_array_to_int(modes_opposite)

    return gamma * epsilon


def filter_down(active, prioritize_common):
    val = None

    for i in range(12): # input line size = 12
        if len(active) == 1: # break if down to 1 remaining line
            val = active[0]
            break

        ones = [line for line in active if line[i] == '1']
        zeros = [line for line in active if line[i] == '0']

        if prioritize_common:
            if len(ones) < len (zeros):
                active = zeros
            else:
                active = ones
        else:
            if len(ones) < len (zeros):
                active = ones
            else:
                active = zeros

    return (val if val else active[0])


def part_two(lines):
    oxygen = bin_array_to_int(filter_down(lines, True))
    co2 = bin_array_to_int(filter_down(lines, False))

    return oxygen * co2


data = parse_input("../input/3_binary_diagnostic.txt")
print("part one:", part_one(data)) # 841526
print("part two:", part_two(data)) # 4790390
