#!/usr/bin/env

class Directory:
    def __init__(self, name, contents, size, parent):
        self.name = name
        self.contents = contents
        self.size = size
        self.parent = parent

    def __str__(self):
        return f"{self.name} ({self.size}): {self.contents}"

    def __repr__(self):
        return str(self)


def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [l.rstrip().split() for l in lines]

    # start at root (create / dir and remove related instruction)
    root = Directory('/', [], 0, None)
    current = root
    lines.pop(0)

    for line in lines:
        # handle bash commands
        if line[0] == '$':          
            if line[1] == 'cd':

                # cd ..: move up a dir & propogate up the size
                if line[2] == '..': 
                    child_size = current.size
                    current = current.parent
                    current.size += child_size

                # cd x: move into line[2] (find dir in current directory)
                else:
                    for x in current.contents:
                        if isinstance(x, Directory) and x.name == line[2]:
                            current = x
                            break

        # handle populating directory contents
        else:
            # read in a directory: create dir and append to current contents
            if line[0] == 'dir':    
                d = Directory(line[1], [], 0, current)
                current.contents.append(d)

            # read in a file: update dir size and append value to current contents
            else:                   
                file_size = int(line[0])
                current.size += file_size
                current.contents.append(file_size)

    # get back to root
    while current != root:
        child_size = current.size
        current = current.parent
        current.size += child_size

    return root


def part_one(root):
    delete_sum = 0

    # in order BFS for all directories with size <= 100000
    queue = [root]
    while len(queue) > 0:
        d = queue.pop(0)

        if d.size <= 100000:
            delete_sum += d.size

        for x in d.contents:
            if isinstance(x, Directory):
                queue.append(x)

    return delete_sum


def part_two(root):
    min_delete_dir_size = 30000000 - (70000000 - root.size)

    # in order BFS for all potential directories with size >= min_delete_dir_size
    candidates = []
    queue = [root]
    while len(queue) > 0:
        d = queue.pop(0)

        if d.size >= min_delete_dir_size:
            candidates.append(d.size)

        for x in d.contents:
            if isinstance(x, Directory):
                queue.append(x)

    return min(candidates)


tree = parse_input("input.txt")
print("part one:", part_one(tree))  # 1243729
print("part two:", part_two(tree))  # 4443914
