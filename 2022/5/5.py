#!/usr/bin/env

def parse_stacks(lines, split):
    stack_data = lines[:split - 1]
    stack_data = [list(d) for d in stack_data]

    num_stacks = len(stack_data[0]) // 4
    stacks = {}
    for i in range(num_stacks):
        stacks[i + 1] = []

        for row in stack_data:
            # stack i + 1 needs to be built from chars in the (i * 4) + 1 column
            el = row[(i * 4) + 1]
            if el != ' ':
                stacks[i + 1].append(el)
        
        stacks[i + 1].reverse()
    
    return stacks


def parse_instructions(lines, split):
    instructions_data = lines[(split + 1):]
    instructions_data = [i.rstrip() for i in instructions_data]

    instructions = []  # will be a list of instructions in [number_of_elements_to_move, from_stack_num, to_stack_num] format
    for i, instruction in enumerate(instructions_data):
        instructions.append([])

        ss_after_move = instruction.split('move')[1]
        ss_after_from = ss_after_move.split('from')[1]

        # grab how many need to be moved
        instructions[i].append(ss_after_move.split('from')[0])

        # grab from and to stacks
        instructions[i].append(ss_after_from.split('to')[0])
        instructions[i].append(ss_after_from.split('to')[1])

    return instructions


def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()

    # find break row (empty row between stack data and instructions data)
    split = None
    for i in range(len(lines)):
        if lines[i] == '\n':
            split = i
            break

    # build stacks dict
    stacks = parse_stacks(lines, split)

    # build instructions list
    instructions = parse_instructions(lines, split)

    return stacks, instructions


def part_one(stacks, instructions):
    tops = ''

    # run all instructions
    for instruction in instructions:
        num_elements_to_move = int(instruction[0])
        from_stack = int(instruction[1])
        to_stack = int(instruction[2])

        # move crates one by one
        for i in range(num_elements_to_move):
            popped = stacks[from_stack].pop()
            stacks[to_stack].append(popped)

    # build string from tops of all stacks
    for stack in stacks:
        tops += stacks[stack].pop()

    return tops


def part_two(stacks, instructions):
    tops = ''

    # run all instructions
    for instruction in instructions:
        num_elements_to_move = int(instruction[0])
        from_stack = int(instruction[1])
        to_stack = int(instruction[2])

        # load crates onto the crane
        on_crane = []
        for i in range(num_elements_to_move):
            on_crane.append(stacks[from_stack].pop())

        # reverse the crate order and move to to_stack
        on_crane.reverse()
        stacks[to_stack].extend(on_crane)

    # build string from tops of all stacks
    for stack in stacks:
        tops += stacks[stack].pop()

    return tops


stacks, instructions = parse_input("input.txt")
print("part one:", part_one(stacks, instructions))  # JDTMRWCQJ

stacks, instructions = parse_input("input.txt")
print("part two:", part_two(stacks, instructions))  # VHJDDCWRD
