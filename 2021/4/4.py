#!/usr/bin/env

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip().split() for l in lines]

    numbers = lines[0][0].split(',')

    # build bingo boards
    boards = []
    for i in range(2, len(lines), 6):
        board = []
        board.extend([lines[i], lines[i + 1], lines[i + 2], lines[i + 3], lines[i + 4]])
        boards.append(board)

    # build map from input numbers to board locations [board, row, col]
    locs = {}
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, val in enumerate(row):
                if val not in locs:
                    locs[val] = []
                locs[val].append([i, j, k])

    return numbers, boards, locs


def bingo(to_check):
    '''
    Check a list for a bingo by validating type.
    If any elements are still strings, there is no bingo.
    '''
    is_bingo = True
    for x in to_check:
        if isinstance(x, str):
            is_bingo = False

    return is_bingo


def score_board(num, boards, board_i):
    unmarked = 0
    board = boards[board_i]
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if isinstance(val, str):
                unmarked += int(val)

    return unmarked * int(num)


def part_one(numbers, boards, locs):
    for i in numbers:
        if i not in locs: continue

        targets = locs[i]
        for t in targets:
            boards[t[0]][t[1]][t[2]] = int(boards[t[0]][t[1]][t[2]])  # "mark" by casting to int

            # check row for bingo
            row = boards[t[0]][t[1]]
            if bingo(row):
                return score_board(i, boards, t[0])

            # check column for bingo
            column = [row[t[2]] for row in boards[t[0]]]
            if bingo(column):
                return score_board(i, boards, t[0])


def part_two(numbers, boards, locs):
    boards_complete = [False]*len(boards)
    last_board = None

    for i in numbers:
        if i not in locs: continue

        # check if only one board left
        if boards_complete.count(False) == 1:
            last_board = boards_complete.index(False)

        targets = locs[i]
        for t in targets:
            boards[t[0]][t[1]][t[2]] = int(boards[t[0]][t[1]][t[2]])  # "mark" by casting to int

            # check row for bingo
            row = boards[t[0]][t[1]]
            if bingo(row):
                boards_complete[t[0]] = True

                if t[0] == last_board:
                    return score_board(i, boards, t[0])

            # check column for bingo
            column = [row[t[2]] for row in boards[t[0]]]
            if bingo(column):
                boards_complete[t[0]] = True

                if t[0] == last_board:
                    return score_board(i, boards, t[0])



numbers, boards, locs = parse_input("input.txt")
print("part one:", part_one(numbers, boards, locs)) # 44088
numbers, boards, locs = parse_input("input.txt")
print("part two:", part_two(numbers, boards, locs)) # 23670
