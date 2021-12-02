#!/usr/bin/env

filename = "../input/1_sea_floor.txt"

# read in input
with open(filename) as file:
    depths = file.readlines()
    depths = [int(d.rstrip()) for d in depths]

# print("input size: ", len(depths))


# PART 1

increase = 0
for i, d in enumerate(depths):
    if i == 0: continue

    if d > depths[i - 1]:
        increase += 1

print("part 1 answer: ", increase)


# PART 2: sliding window

# in comparing 2 windows, 2 middle values are shared
# i.e. in [199 200 208 210] it only matters that 210 > 199

increase = 0
for i in range(3, len(depths)):
    if depths[i] > depths[i - 3]:
        increase += 1

print("part 2 answer: ", increase)
