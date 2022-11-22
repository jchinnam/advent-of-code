#!/usr/bin/env

from collections import Counter

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        template = lines[0].rstrip()
        rules = [l.rstrip() for l in lines[2:]]

    rules = [r.split(' -> ') for r in rules]

    return template, rules


def run_rules(template, rules, steps):
    for i in range(steps):

        for rule in rules:

            # continue to replace while rule subtring exists
            while rule[0] in template:

                # insert new chars but as lowercase (so as not to be used in other matches this turn)
                template = template.replace(rule[0], rule[0][0] + rule[1].lower() + rule[0][1])

        # convert back to uppercase at end of turn
        template = template.upper()

    counter = Counter(list(template))
    frequencies = counter.most_common()

    return frequencies[0][1] - frequencies[-1][1]


def part_one(template, rules):
    return run_rules(template, rules, 10)


def part_two(template, rules):
    return run_rules(template, rules, 40)


template, rules = parse_input("input.txt")
print("part one:", part_one(template, rules)) # 2360
print("part two:", part_two(template, rules)) #
