#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]

    return lines


def part_one(data):
    output = [l.split('|')[1].split() for l in data]

    unique = 0
    for row in output:
        for s in row:
            if len(s) in [2, 3, 4, 7]:
                unique += 1

    return unique


def part_two(data):
    # Using the following capital letters to indicate positions:

    #  HHHH
    # I    J
    # I    J
    #  KKKK
    # L    M
    # L    M
    #  NNNN

    # We see the following subsets of positions per number:

    #                    chars
    # 0: H I J   L M N   6
    # 1:     J     M     2
    # 2: H   J K L   N   5
    # 3: H   J K   M N   5
    # 4:   I J K   M     4
    # 5: H I   K   M N   5
    # 6: H I   K L M N   6
    # 7: H   J     M     3
    # 8: H I J K L M N   7
    # 9: H I J K   M N   6

    patterns = [l.split('|')[0].split() for l in data]
    output = [l.split('|')[1].split() for l in data]

    total = 0
    for index in range(len(data)):
        digit_to_chars = {} # map digit : set of chars
        unknown_digits = patterns[index]

        # deduce 1, 4, 7, 8
        for i, d in enumerate(unknown_digits):
            if not d: continue

            if len(d) == 2:
                digit_to_chars[1] = set(d)
                unknown_digits[i] = None
            elif len(d) == 4:
                digit_to_chars[4] = set(d)
                unknown_digits[i] = None
            elif len(d) == 3:
                digit_to_chars[7] = set(d)
                unknown_digits[i] = None
            elif len(d) == 7:
                digit_to_chars[8] = set(d)
                unknown_digits[i] = None

        # deduce 9 from 4
        for i, d in enumerate(unknown_digits):
            if not d: continue

            if len(d) == 6 and digit_to_chars[4].issubset(set(d)):
                digit_to_chars[9] = set(d)
                unknown_digits[i] = None

        # deduce 0 from 7 (requires 9 to be removed)
        for i, d in enumerate(unknown_digits):
            if not d: continue

            if len(d) == 6 and digit_to_chars[7].issubset(set(d)):
                digit_to_chars[0] = set(d)
                unknown_digits[i] = None

        # deduce 6 (requres 9 and 0 to be removed)
        for i, d in enumerate(unknown_digits):
            if not d: continue

            if len(d) == 6:
                digit_to_chars[6] = set(d)
                unknown_digits[i] = None

        # deduce 5 from 6
        for i, d in enumerate(unknown_digits):
            if not d: continue

            if set(d).issubset(digit_to_chars[6]):
                digit_to_chars[5] = set(d)
                unknown_digits[i] = None

        # deduce 3 (requires 5 to be removed), 2
        for i, d in enumerate(unknown_digits):
            if not d: continue

            if set(d).issubset(digit_to_chars[9]):
                digit_to_chars[3] = set(d)
                unknown_digits[i] = None
            else:
                digit_to_chars[2] = set(d)
                unknown_digits[i] = None

        # build output number
        output_digits = []
        for digit in output[index]:
            for k in digit_to_chars.keys():
                if digit_to_chars[k] == set(digit):
                    output_digits.append(k)

        total += int(''.join(map(str, output_digits)))

    return total


data = parse_input("input.txt")
print("part one:", part_one(data)) # 525
print("part two:", part_two(data)) # 1083859
