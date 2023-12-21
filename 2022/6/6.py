#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()

    return lines[0]


def solution(data, marker_size):
    for i in range(len(data)):
        candidates = set()
        for j in range(marker_size):
            candidates.add(data[i + j])
        
        if len(candidates) == marker_size:
            break
    
    return i + marker_size


data = parse_input("input.txt")
print("part one:", solution(data, 4))  # 1262
print("part two:", solution(data, 14))  # 3444