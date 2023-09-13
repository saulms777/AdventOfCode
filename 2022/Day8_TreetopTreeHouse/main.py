def printlist(array):
    for line in array:
        print(line)
    print()


def part1(file):
    with open(file, "r") as f:
        trees = tuple([tuple(map(int, line)) for line in f.read().split("\n")])
        # printlist(trees)

    directions = [[[False] * len(trees[0]) for _ in range(len(trees))] for _ in range(4)]
    for direction in range(4):
        for row_index, row in enumerate(trees):
            for item_index, item in enumerate(row):
                if item_index == 0:
                    directions[direction][row_index][item_index] = True
                else:
                    directions[direction][row_index][item_index] = True if max(row[:item_index]) < item else False

        trees = tuple(zip(*reversed(trees)))
        for index in range(4):
            directions[index] = [list(elem) for elem in zip(*reversed(directions[index]))]

    visible = [[False] * len(trees[0]) for _ in range(len(trees))]
    count = 0
    for row in range(len(trees)):
        for item in range(len(trees[0])):
            for direction in range(4):
                visible[row][item] |= directions[direction][row][item]
            if visible[row][item]:
                count += 1

    # printlist(visible)
    print(count)


def part2(file):
    with open(file, "r") as f:
        trees = tuple([tuple(map(int, line)) for line in f.read().split("\n")])
        # printlist(trees)

    directions = [[[0] * len(trees[0]) for _ in range(len(trees))] for _ in range(4)]
    for direction in range(4):
        for row_index, row in enumerate(trees):
            for item_index, item in enumerate(row):
                if item_index == 0:
                    directions[direction][row_index][item_index] = 0
                else:
                    for tree in reversed(row[:item_index]):
                        directions[direction][row_index][item_index] += 1
                        if tree >= item:
                            break

        trees = tuple(zip(*reversed(trees)))
        for index in range(4):
            directions[index] = [list(elem) for elem in zip(*reversed(directions[index]))]

    scenic = 0
    for row in range(len(trees)):
        for item in range(len(trees[0])):
            score = 1
            for direction in range(4):
                score *= directions[direction][row][item]
            scenic = max(scenic, score)

    print(scenic)


if __name__ == "__main__":
    part1("Day8Input.txt")
    part2("Day8Input.txt")
